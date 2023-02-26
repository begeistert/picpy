from .node import PyNode


class DeclareObject(PyNode):
    def __init__(self, line, column, name, reference, args=None):
        super().__init__(line, column)
        self.name = name
        self.reference = reference
        self.args = args

    def resolve(self):
        pass

    def __repr__(self):
        return f'DeclareObject({self.name}, {self.reference})'

    def __eq__(self, other):
        return isinstance(other, DeclareObject) and self.name == other.name and self.reference == other.value

    def __hash__(self):
        return hash((self.name, self.reference))

    def accept(self, visitor):
        return visitor.visit_declare(self)

