from .node import PyNode


class While(PyNode):
    def __init__(self, line, column, condition, body):
        super().__init__(line, column)
        self.condition = condition
        self.body = body

    def resolve(self):
        pass

    def __repr__(self):
        return f'While({self.condition}, {self.body})'

    def __eq__(self, other):
        return isinstance(other, While) and self.condition == other.condition and self.body == other.body

    def __hash__(self):
        return hash(self.line)

    def accept(self, visitor):
        return visitor.visit_while(self)
