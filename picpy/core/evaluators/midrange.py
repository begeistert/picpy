from .evaluator import Evaluator
from ..arch.midrange import *


class Pin(Evaluator):
    def __init__(self, register: str, bit: str, mode=1, has_tris=False):
        self.register = register
        self.bit = bit
        self.mode = mode
        if has_tris:
            self.tris = register.replace("PORT", "TRIS")

    def resolve(self, context):
        register = context[self.register]
        if int(self.bit) is not None:
            bit = int(self.bit)
        else:
            bit = context[self.bit]
        return Bsf(register, bit) if self.mode else Bcf(register, bit)

    def __repr__(self):
        return f"Pin({self.register}, {self.bit})"


