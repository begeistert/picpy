from.base import InstructionSet, Mnemonic


class MidrangeSet(InstructionSet):
    def emit(self, mnemonic):
        mnem = getattr(self, mnemonic.mnemonic.lower())
        if not mnemonic:
            raise ValueError(f"Invalid mnemonic: {mnemonic}")
        return mnem(mnemonic)

    def addwf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_0111_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def andwf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_0101_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def clrf(self, mnemonic):
        f = mnemonic.register
        return 0b00_0001_1000_0000 | (f & 0x7f)

    def clrw(self, _):
        return 0b00_0001_0000_0000

    def comf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_1001_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def decf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_0011_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def decfsz(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_1011_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def incf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_1010_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def incfsz(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_1111_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def iorwf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_0100_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def movf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_1000_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def movwf(self, mnemonic):
        f = mnemonic.register
        return 0b00_0000_1000_0000 | (f & 0x7f)

    def nop(self, _):
        return 0b00_0000_0000_0000

    def rlf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_1101_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def rrf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_1100_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def subwf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_0010_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def swapf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_1110_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def xorwf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        return 0b00_0110_0000_0000 | ((d & 1) << 7) | (f & 0x7f)

    def bcf(self, mnemonic):
        f = mnemonic.register
        b = mnemonic.bit
        return 0b01_0000_0000_0000 | ((b & 7) << 7) | (f & 0x7f)

    def bsf(self, mnemonic):
        f = mnemonic.register
        b = mnemonic.bit
        return 0b01_0100_0000_0000 | ((b & 7) << 7) | (f & 0x7f)

    def btfsc(self, mnemonic):
        f = mnemonic.register
        b = mnemonic.bit
        return 0b01_1000_0000_0000 | ((b & 7) << 7) | (f & 0x7f)

    def btfss(self, mnemonic):
        f = mnemonic.register
        b = mnemonic.bit
        return 0b01_1100_0000_0000 | ((b & 7) << 7) | (f & 0x7f)

    def addlw(self, mnemonic):
        k = mnemonic.constant
        return 0b11_1110_0000_0000 | (k & 0xff)

    def andlw(self, mnemonic):
        k = mnemonic.constant
        return 0b11_1001_0000_0000 | (k & 0xff)

    def call(self, mnemonic):
        k = mnemonic.constant
        return 0b10_0000_0000_0000 | (k & 0x7ff)

    def clrwdt(self, _):
        return 0b00_0000_0110_0100

    def goto(self, mnemonic):
        k = mnemonic.constant
        return 0b10_1000_0000_0000 | (k & 0x7ff)

    def iorlw(self, mnemonic):
        k = mnemonic.constant
        return 0b11_1000_0000_0000 | (k & 0xff)

    def movlw(self, mnemonic):
        k = mnemonic.constant
        return 0b11_0000_0000_0000 | (k & 0xff)

    def retfie(self, _):
        return 0b00_0000_0000_1001

    def retlw(self, mnemonic):
        k = mnemonic.constant
        return 0b11_0100_0000_0000 | (k & 0xff)

    def sleep(self, _):
        return 0b00_0000_0110_0011

    def sublw(self, mnemonic):
        k = mnemonic.constant
        return 0b11_1100_0000_0000 | (k & 0xff)

    def xorlw(self, mnemonic):
        k = mnemonic.constant
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
