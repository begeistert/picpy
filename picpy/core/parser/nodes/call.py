from .node import PyNode


class Call(PyNode):
    def __init__(self, line, column, target, arguments=None):
        super().__init__(line, column)
        self.target = target
        self.arguments = arguments

    def resolve(self):
        pass

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
        pass

    def __repr__(self):
        return f'CallObjectFunction({self.target}, {self.function}, {self.arguments})'

    def __eq__(self, other):
        return isinstance(other, CallObjectFunction) and self.target == other.target and self.function == other.function and self.arguments == other.arguments

    def __hash__(self):
        return hash((self.target, self.function, self.arguments))

    def accept(self, visitor):
        return visitor.visit_call_object_function(self)
