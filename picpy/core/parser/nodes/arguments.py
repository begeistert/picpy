from .node import PyNode


class Arguments(PyNode):
    def __init__(self, arguments, defaults=None, kw_defaults=None, kwarg=None, vararg=None,
                 kwonlyargs=None, posonlyargs=None):
        super().__init__(0, 0)
        self.arguments = arguments
        self.defaults = defaults
        self.kw_defaults = kw_defaults
        self.kwarg = kwarg
        self.vararg = vararg
        self.kwonlyargs = kwonlyargs
        self.posonlyargs = posonlyargs

    def resolve(self):
        pass

    def __repr__(self):
        return f'Arguments({self.arguments})'

    def __eq__(self, other):
        return isinstance(other, Arguments) and self.arguments == other.arguments

    def __hash__(self):
        return hash(self.arguments)

    def accept(self, visitor):
        return visitor.visit_arguments(self)