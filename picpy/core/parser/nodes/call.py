from .node import PyNode
from picpy.core.arch import base
from ...assembler.nodes.instructions import MnemonicNode
from ...assembler.nodes.expression import Value


class Call(PyNode):
    def __init__(self, line, column, target, arguments=None):
        super().__init__(line, column)
        self.target = target
        self.arguments = arguments

    def resolve(self):
        # TODO: Consider the arguments
        if self.target == 'assembly':
            return base.RawAssembly(self.arguments[0].value, self.label)
        return MnemonicNode("CALL", literal=Value(self.target))

    def __repr__(self):
        return f'Call({self.target}, {self.arguments})'

    def __eq__(self, other):
        return isinstance(other, Call) and self.target == other.target and self.arguments == other.arguments

    def __hash__(self):
        return hash((self.target, self.arguments))

    def accept(self, visitor):
        return visitor.visit_call(self)


class CallObjectFunction(PyNode):
    def __init__(self, line, column, target, function, arguments=None):
        super().__init__(line, column)
        self.target = target
        self.function = function
        self.arguments = arguments

    def resolve(self):
        context = self._context
        native = context.natives
        env = context.environment
        if self.arguments is not None and len(self.arguments) > 0:
            args = self.arguments.resolve(context)

        if self.target == 'Pic':
            match self.function:
                case 'sleep':
                    return MnemonicNode("SLEEP")

        if native.get(self.target) is not None:
            attr = getattr(native.get(self.target), self.function)
            if attr is not None:
                return attr()

    def __repr__(self):
        return f'CallObjectFunction({self.target}, {self.function}, {self.arguments})'

    def __eq__(self, other):
        return isinstance(other, CallObjectFunction) and self.target == other.target and self.function == other.function and self.arguments == other.arguments

    def __hash__(self):
        return hash((self.target, self.function, self.arguments))

    def accept(self, visitor):
        return visitor.visit_call_object_function(self)
