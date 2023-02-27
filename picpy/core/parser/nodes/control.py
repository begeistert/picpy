from .node import PyNode
from ...arch import midrange
from ...assembler.nodes.instructions import MnemonicNode
from ...assembler.nodes.expression import Value


class Goto(PyNode):
    def __init__(self, label):
        super().__init__(0, 0)
        self.label = label

    def resolve(self):
        return MnemonicNode("GOTO", literal=Value(self.label))

    def __str__(self):
        return f'Goto({self.label})'
