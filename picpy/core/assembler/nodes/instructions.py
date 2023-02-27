from .base import AssemblyNode


class MnemonicNode(AssemblyNode):
    """Base class for all assembly nodes that represent a mnemonic."""
    def __init__(self, mnemonic, register=None, bit=None, destination=None, literal=None):
        self.mnemonic = mnemonic
        self.register = register
        self.bit = bit
        self.destination = destination
        self.literal = literal

    def resolve(self, linker):
        env = linker.environment
        if self.register is not None:
            self.register = self.register.evaluate(env)
        if self.bit is not None:
            self.bit = self.bit.evaluate(env)
        if self.destination is not None:
            self.destination = self.destination.evaluate(env)
        if self.literal is not None:
            self.literal = self.literal.evaluate(env)

    def __repr__(self):
        return f"MnemonicNode({self.mnemonic}, {self.register}, {self.bit}, {self.destination}, {self.literal})"
