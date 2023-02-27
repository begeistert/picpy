from .node import PyNode
from ...assembler.nodes.expression import Value


class Constant(PyNode):
    def __init__(self, line, column, value):
        super().__init__(line, column)
        self.value = value

    def resolve(self):
        return Value(self.value)

    def __repr__(self):
        return f'Constant({self.value})'

    def __eq__(self, other):
        return isinstance(other, Constant) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def accept(self, visitor):
        return visitor.visit_constant(self)
