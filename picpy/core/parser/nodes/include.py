from .node import PyNode


class Include(PyNode):

    def __init__(self, line, column, module, name, alias):
        super().__init__(line, column)
        self.module = module
        self.name = name
        self.alias = alias

    def resolve(self):
        pass

    def __repr__(self):
        return f'Include({self.module}, {self.name})'

    def __eq__(self, other):
        return isinstance(other, Include) and self.name == other.name and self.alias == other.alias

    def __hash__(self):
        return hash((self.name, self.alias))

    def accept(self, visitor):
        return visitor.visit_import(self)