from .node import PyNode
from ...assembler.nodes.expression import Value


class Attribute(PyNode):
    def __init__(self, line, column, target, attribute):
        super().__init__(line, column)
        self.target = target
        self.attribute = attribute

    def resolve(self):
        pass

    def __repr__(self):
        return f'Attribute({self.target}, {self.attribute})'

    def __eq__(self, other):
        return isinstance(other, Attribute) and self.target == other.target and self.attribute == other.attribute

    def __hash__(self):
        return hash((self.target, self.attribute))

    def accept(self, visitor):
        return visitor.visit_attribute(self)


class Name(PyNode):
    def __init__(self, line, column, name):
        super().__init__(line, column)
        self.name = name

    def resolve(self):
        return Value(self.name)

    def __repr__(self):
        return f'Name({self.name})'

    def __eq__(self, other):
        return isinstance(other, Name) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def accept(self, visitor):
        return visitor.visit_name(self)
