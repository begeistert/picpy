from.base import Mnemonic


class Midrange:
    def addwf(self, f, d):
        return 0b00_0111_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def andwf(self, f, d):
        return 0b00_0101_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def clrf(self, f):
        return 0b00_0001_1000_0000 | (f & 0x7f)

    def clrw(self):
        return 0b00_0001_0000_0000

    def comf(self, f, d):
        return 0b00_1001_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def decf(self, f, d):
        return 0b00_0011_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def decfsz(self, f, d):
        return 0b00_1011_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def incf(self, f, d):
        return 0b00_1010_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def incfsz(self, f, d):
        return 0b00_1111_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def iorwf(self, f, d):
        return 0b00_0100_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def movf(self, f, d):
        return 0b00_1000_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def movwf(self, f):
        return 0b00_0000_1000_0000 | (f & 0x7f)

    def nop(self):
        return 0b00_0000_0000_0000

    def rlf(self, f, d):
        return 0b00_1101_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def rrf(self, f, d):
        return 0b00_1100_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def subwf(self, f, d):
        return 0b00_0010_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def swapf(self, f, d):
        return 0b00_1110_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def xorwf(self, f, d):
        return 0b00_0110_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def bcf(self, f, b):
        return 0b01_0000_0000_0000 | ((b & 7) << 7) | (f & 0x7f)

    def bsf(self, f, b):
        return 0b01_0100_0000_0000 | ((b & 7) << 7) | (f & 0x7f)

    def btfsc(self, f, b):
        return 0b01_1000_0000_0000 | ((b & 7) << 7) | (f & 0x7f)

    def btfss(self, f, b):
        return 0b01_1100_0000_0000 | ((b & 7) << 7) | (f & 0x7f)

    def addlw(self, k):
        return 0b11_1110_0000_0000 | (k & 0xff)

    def andlw(self, k):
        return 0b11_1001_0000_0000 | (k & 0xff)

    def call(self, k):
        return 0b10_0000_0000_0000 | (k & 0x7ff)

    def clrwdt(self):
        return 0b00_0000_0110_0100

    def goto(self, k):
        return 0b10_1000_0000_0000 | (k & 0x7ff)

    def iorlw(self, k):
        return 0b11_1000_0000_0000 | (k & 0xff)

    def movlw(self, k):
        return 0b11_0000_0000_0000 | (k & 0xff)

    def retfie(self):
        return 0b00_0000_0000_1001

    def retlw(self, k):
        return 0b11_0100_0000_0000 | (k & 0xff)

    def sleep(self):
        return 0b00_0000_0110_0011

    def sublw(self, k):
        return 0b11_1100_0000_0000 | (k & 0xff)

    def xorlw(self, k):
        return 0b11_1010_0000_0000 | (k & 0xff)


class Movlw(Mnemonic):
    def __init__(self, k):
        super().__init__(constant=k)

    def emit(self):
        return 0b11_0000_0000_0000 | (self.constant & 0xff)


class Bcf(Mnemonic):
    def __init__(self, f, b):
        super().__init__(register=f, bit=b)

    def emit(self):
        return 0b01_0000_0000_0000 | ((self.bit & 7) << 7) | (self.register & 0x7f)


class Bsf(Mnemonic):
    def __init__(self, f, b):
        super().__init__(register=f, bit=b)

    def emit(self):
        return 0b01_0100_0000_0000 | ((self.bit & 7) << 7) | (self.register & 0x7f)


class Btfsc(Mnemonic):
    def __init__(self, f, b):
        super().__init__(register=f, bit=b)

    def emit(self):
        return 0b01_1000_0000_0000 | ((self.bit & 7) << 7) | (self.register & 0x7f)


class Btfss(Mnemonic):
    def __init__(self, f, b):
        super().__init__(register=f, bit=b)

    def emit(self):
        return 0b01_1100_0000_0000 | ((self.bit & 7) << 7) | (self.register & 0x7f)


class Movwf(Mnemonic):
    def __init__(self, f):
        super().__init__(register=f)

    def emit(self):
        return 0b00_0000_1000_0000 | (self.register & 0x7f)


class Call(Mnemonic):
    def __init__(self, k=0, label=None):
        super().__init__(constant=k)
        self.label = label

    def resolve(self, labels):
        if self.label is not None:
            self.constant = labels[self.label]

    def emit(self):
        return 0b10_0000_0000_0000 | (self.constant & 0x7ff)


class Goto(Mnemonic):
    def __init__(self, k=0, label=None):
        super().__init__(constant=k)
        self.label = label

    def resolve(self, labels):
        if self.label is not None:
            self.constant = labels[self.label]

    def emit(self):
        return 0b10_1000_0000_0000 | (self.constant & 0x7ff)


class Sleep(Mnemonic):
    def emit(self):
        return 0b00_0000_0110_0011


class RawAssembly(Mnemonic):
    def __init__(self, code):
        super().__init__(constant=code)

    def emit(self):
        return self.constant
