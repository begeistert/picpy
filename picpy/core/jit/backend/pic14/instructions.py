byte_oriented = {
    'addwf': {'op': 0x0700, },
    'andwf': {'op': 0x0500, },
    'clrf': {'op': 0x0180, },
    'clrw': {'op': 0x0100, },
    'comf': {'op': 0x0900, },
    'decf': {'op': 0x0300, },
    'decfsz': {'op': 0x0b00, },
    'incf': {'op': 0x0a00, },
    'incfsz': {'op': 0x0f00, },
    'iorwf': {'op': 0x0400, },
    'movf': {'op': 0x0800, },
    'movwf': {'op': 0x0080, },
    'nop': {'op': 0x0000, },
    'rlf': {'op': 0x0d00, },
    'rrf': {'op': 0x0c00, },
    'subwf': {'op': 0x0200, },
    'swapf': {'op': 0x0e00, },
    'xorwf': {'op': 0x0600, },
}

bit_oriented = {
    'bcf': {'op': 0x1000, },
    'bsf': {'op': 0x1400, },
    'btfsc': {'op': 0x1800, },
    'btfss': {'op': 0x1c00, },
}

literal = {
    'addlw': {'op': 0x3e00, },
    'andlw': {'op': 0x3900, },
    'iorlw': {'op': 0x3800, },
    'movlw': {'op': 0x3000, },
    'retlw': {'op': 0x3400, },
    'sublw': {'op': 0x3c00, },
    'xorlw': {'op': 0x3a00, },
}

branch = {
    'call': {'op': 0x2000, },
    'goto': {'op': 0x2800, },
}

control = {
    'clrwdt': {'op': 0x0064, },
    'retfie': {'op': 0x0009, },
    'return': {'op': 0x0008, },
    'sleep': {'op': 0x0063, },
}

