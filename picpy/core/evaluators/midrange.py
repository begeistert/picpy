from .evaluator import Evaluator
from ..arch.midrange import *
from ..parser.nodes import Attribute, Constant, Name


class Pic(Evaluator):
    def __init__(self, arch, has_tris=False):
        self.arch = arch
        self.has_tris = has_tris

    def sleep(self, context):
        return Sleep()


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

    def value(self, context, val):
        return self.on(context) if val else self.off(context)

    def off(self, context):
        if self.bit.isnumeric():
            bit = int(self.bit)
        else:
            bit = context[self.bit]

        port = self.register.replace("TRIS", "PORT")
        return Bcf(context[port if self.has_tris else self.register], bit)

    def on(self, context):
        if self.bit.isnumeric():
            bit = int(self.bit)
        else:
            bit = context[self.bit]

        port = self.register.replace("TRIS", "PORT")
        return Bsf(context[port if self.has_tris else self.register], bit)

    def resolve(self, context):
        register = context[self.register]
        if self.bit.isnumeric():
            bit = int(self.bit)
        else:
            bit = context[self.bit]
        return Bsf(register, bit) if self.mode else Bcf(register, bit)

    def __repr__(self):
        return f"Pin({self.register}, {self.bit})"


