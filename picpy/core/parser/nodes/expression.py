from .node import PyNode


class Expr(PyNode):
    def __init__(self, line, column, expression):
        super().__init__(line, column)
        self.expression = expression

    def resolve(self):
        pass

    def __repr__(self):
        return f'Expression({self.expression})'

    def __eq__(self, other):
        return isinstance(other, Expression) and self.expression == other.expression

    def __hash__(self):
        return hash(self.expression)

    def accept(self, visitor):
        return visitor.visit_expression(self)