from .base import AssemblyNode


class MnemonicNode(AssemblyNode):
    """Base class for all assembly nodes that represent a mnemonic."""
    def __init__(self, mnemonic, register=None, bit=None, destination=None, literal=None):
        self.mnemonic = mnemonic
        self.register = register
        self.bit = bit
        self.destination = destination
        self.literal = literal

    def __repr__(self):
        return f"MnemonicNode({self.mnemonic}, {self.register}, {self.bit}, {self.destination}, {self.literal})"
