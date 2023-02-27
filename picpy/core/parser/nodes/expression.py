from .node import PyNode


class Expr(PyNode):
    def __init__(self, line, column, expression):
        super().__init__(line, column)
        self.expression = expression

    @property
    def label(self):
        match self.expression:
            case list():
                return self.expression[0].label
            case _:
                return self.expression.label

    @label.setter
    def label(self, value):
        match self.expression:
            case list():
                self.expression[0].label = value
            case _:
                self.expression.label = value

    def resolve(self):
        pass

    def __repr__(self):
        return f'Expression({self.expression})'

    def __eq__(self, other):
        return isinstance(other, Expr) and self.expression == other.expression

    def __hash__(self):
        return hash(self.expression)

    def accept(self, visitor):
        return visitor.visit_expression(self)