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
