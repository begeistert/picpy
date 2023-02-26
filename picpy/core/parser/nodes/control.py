from .node import PyNode


class Goto(PyNode):
    def __init__(self, label):
        super().__init__(0, 0)
        self.label = label

    def resolve(self):
        return f'goto {self.label};'

    def __str__(self):
        return f'Goto({self.label})'
