from ..base import DeviceDebugger


class MidrangeDebugger(DeviceDebugger):

    def __init__(self, program, symbols):
        super().__init__()
        self._opcodes = {
            0b0000: self._nop,
            0b0001: self._movwf,
            0b0010: self._clrf,
            0b0011: self._subwf,
            0b0100: self._decf,
            0b0101: self._iorwf,
            0b0110: self._andwf,
            0b0111: self._xorwf,
            0b1000: self._addwf,
            0b1001: self._movf,
            0b1010: self._comf,
            0b1011: self._incf,
            0b1100: self._decfsz,
            0b1101: self._rrf,
            0b1110: self._rlf,
            0b1111: self._incfsz,
        }
        self._program = program
        self._symbols = symbols
        self._memory = {i: 0 for i in range(256)}
        self.INDF = lambda value=None: self._memory[self.FSR]
        self.TMR0 = lambda value=None: self._memory[0x01]
        self.PCL = lambda value=None: self._memory[0x02]
        self.STATUS = lambda value=None: self._memory[0x03]
        self.FSR = lambda value=None: self._memory[0x04]

    @property
    def pc(self):
        return self._PC

    @property
    def w(self):
        return self._W

    @property
    def status(self):
        return self._status

    @property
    def stack(self):
        return self._stack

    @property
    def memory(self):
        return self._memory

    @property
    def labels(self):
        return self._labels

    @property
    def program(self):
        return self._program

    @property
    def current_instruction(self):
        return self._program[self._PC]

    def reset(self):
        self._memory = {}

    def step(self):
        statement = self._program[self._PC]
        self._PC += 1
        # Write an interpreter for the PIC14 midrange here.

    def _nop(self, mnemonic):
        pass

    def _movwf(self, mnemonic):
        self._memory[mnemonic.register] = self._W

    def _clrf(self, mnemonic):
        self._memory[mnemonic.register] = 0

    def _subwf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W - self._memory[f]
        else:
            self._memory[f] = self._memory[f] - self._W

    def _decf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W - 1
        else:
            self._memory[f] = self._memory[f] - 1

    def _iorwf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W | self._memory[f]
        else:
            self._memory[f] = self._memory[f] | self._W

    def _andwf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W & self._memory[f]
        else:
            self._memory[f] = self._memory[f] & self._W

    def _xorwf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W ^ self._memory[f]
        else:
            self._memory[f] = self._memory[f] ^ self._W

    def _addwf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W + self._memory[f]
        else:
            self._memory[f] = self._memory[f] + self._W

    def _movf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._memory[f]
        else:
            self._memory[f] = self._W

    def _comf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = ~self._W
        else:
            self._memory[f] = ~self._memory[f]

    def _incf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W + 1
        else:
            self._memory[f] = self._memory[f] + 1

    def _decfsz(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W - 1
            if self._W == 0:
                self._PC += 1
        else:
            self._memory[f] = self._memory[f] - 1
            if self._memory[f] == 0:
                self._PC += 1

    def _rrf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W >> 1
        else:
            self._memory[f] = self._memory[f] >> 1

    def _rlf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W << 1
        else:
            self._memory[f] = self._memory[f] << 1

    def _swapf(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = (self._W << 4) | (self._W >> 4)
        else:
            self._memory[f] = (self._memory[f] << 4) | (self._memory[f] >> 4)

    def _incfsz(self, mnemonic):
        f = mnemonic.register
        d = mnemonic.destination
        if d == 0:
            self._W = self._W + 1
            if self._W == 0:
                self._PC += 1
        else:
            self._memory[f] = self._memory[f] + 1
            if self._memory[f] == 0:
                self._PC += 1

    def _bcf(self, mnemonic):
        f = mnemonic.register
        b = mnemonic.bit
        self._memory[f] = self._memory[f] & ~(1 << b)

    def _bsf(self, mnemonic):
        f = mnemonic.register
        b = mnemonic.bit
        self._memory[f] = self._memory[f] | (1 << b)

    def _btfsc(self, mnemonic):
        f = mnemonic.register
        b = mnemonic.bit
        if self._memory[f] & (1 << b) == 0:
            self._PC += 1

    def _btfss(self, mnemonic):
        f = mnemonic.register
        b = mnemonic.bit
        if self._memory[f] & (1 << b) != 0:
            self._PC += 1

    def _goto(self, mnemonic):
        self._PC = self._labels[mnemonic.label]

    def _call(self, mnemonic):
        self._stack.append(self._PC)
        self._PC = self._labels[mnemonic.label]

    def _retfie(self, mnemonic):
        self._PC = self._stack.pop()
        self._GIE = 1

    def _retlw(self, mnemonic):
        self._W = mnemonic.value
        self._PC = self._stack.pop()

    def _return(self, mnemonic):
        self._PC = self._stack.pop()

    def _addlw(self, mnemonic):
        self._W = self._W + mnemonic.value

    def _andlw(self, mnemonic):
        self._W = self._W & mnemonic.value

    def _iorlw(self, mnemonic):
        self._W = self._W | mnemonic.value

    def _xorlw(self, mnemonic):
        self._W = self._W ^ mnemonic.value

    def _movlw(self, mnemonic):
        self._W = mnemonic.value

    def _sublw(self, mnemonic):
        self._W = self._W - mnemonic.value
