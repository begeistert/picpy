from .node import Node


class Assign(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Assign({self.left}, {self.right})'

    def __str__(self):
        return f'{self.left} = {self.right}'

    def accept(self, visitor):
        return visitor.visit_assign(self)
