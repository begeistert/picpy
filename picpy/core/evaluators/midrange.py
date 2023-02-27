from .evaluator import Evaluator
from ..parser.nodes import Attribute, Constant, Name
from ..assembler.nodes.instructions import MnemonicNode
from ..assembler.nodes.expression import Value


class Pic(Evaluator):

    def __init__(self, arch, has_tris=False):
        self.arch = arch
        self.has_tris = has_tris

    @staticmethod
    def sleep():
        return MnemonicNode("SLEEP")

    def resolve(self):
        pass


class Pin(Evaluator):
    def __init__(self, register: Name, bit: Name, mode, has_tris=False):
        self.register = register.name
        self.bit = bit.name
        self.mode = mode
        self.has_tris = has_tris
        match mode:
            case Attribute():
                if mode.target == 'Pin':
                    self.mode = mode.attribute == 'IN'
            case Constant():
                self.mode = mode.value
            case Name():
                self.mode = mode.name
        if self.has_tris:
            self.register = self.register.replace("PORT", "TRIS")

    def value(self, val):
        return self.on() if val else self.off()

    def off(self):
        if self.bit.isnumeric():
            bit = int(self.bit)
        else:
            bit = self.bit

        port = self.register.replace("TRIS", "PORT")
        return MnemonicNode("BCF", register=Value(port if self.has_tris else self.register), bit=Value(bit))

    def on(self):
        if self.bit.isnumeric():
            bit = int(self.bit)
        else:
            bit = self.bit

        port = self.register.replace("TRIS", "PORT")
        return MnemonicNode("BSF", register=Value(port if self.has_tris else self.register), bit=Value(bit))

    def resolve(self):
        register = self.register
        if self.bit.isnumeric():
            bit = int(self.bit)
        else:
            bit = self.bit
        mnem = "BSF" if self.mode else "BCF"
        return MnemonicNode(mnem, register=Value(register), bit=Value(bit))

    def __repr__(self):
        return f"Pin({self.register}, {self.bit})"
