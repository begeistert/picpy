from .node import PyNode
from ...arch import midrange


class Goto(PyNode):
    def __init__(self, label):
        super().__init__(0, 0)
        self.label = label

    def resolve(self, context):
        return midrange.Goto(self.label)

    def __str__(self):
        return f'Goto({self.label})'
