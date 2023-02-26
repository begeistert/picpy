class Mnemonic:
    ADDLW = 0
    ADDWF = 1
    ANDLW = 2
    ANDWF = 3
    BCF = 4
    BSF = 5
    BTFSC = 6
    BTFSS = 7
    CALL = 8
    CLRF = 9
    CLRW = 10
    CLRWDT = 11
    COMF = 12
    DECF = 13
    DECFSZ = 14
    GOTO = 15
    INCF = 16
    INCFSZ = 17
    IORWF = 18
    MOVLB = 19
    MOVLW = 20
    MOVF = 21
    MOVWF = 22
    NOP = 23
    OPTION = 24
    RETFIE = 25
    RETLW = 26
    RETURN = 27
    RLF = 28
    RRF = 29
    SLEEP = 30
    SUBLW = 31
    SUBWF = 32
    SWAPF = 33
    XORLW = 34
    XORWF = 35

    def __init__(self, register=0, bit=0, destination=0, constant=0):
        self.mnemonic = 0
        self.register = register
        self.bit = bit
        self.destination = destination
        self.constant = constant

    def emit(self):
        raise NotImplementedError()

    def __repr__(self):
        return f"Mnemonic({self.mnemonic}, {self.register}, {self.bit}, {self.destination})"

    def __str__(self):
        return f"{self.mnemonic} {self.register}"
