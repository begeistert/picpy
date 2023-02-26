from .lex import *

preprocessor = (
    'INCLUDE', 'DEFINE', 'UNDEF', 'IFDEF', 'IFNDEF', 'ELSE', 'ENDIF', 'ERROR',
)

mnemonics = (
    'ADDWF', 'ANDWF', 'CLRF', 'CLRW', 'COMF', 'DECF', 'DECFSZ', 'INCF', 'INCFSZ',
    'IORWF', 'MOVF', 'MOVWF', 'RLF', 'RRF', 'SUBWF', 'SWAPF', 'XORWF', 'BCF', 'BSF',
    'BTFSC', 'BTFSS', 'BC', 'BNC', 'BZ', 'BNZ', 'BRA', 'CALL', 'CLRWDT', 'GOTO',
    'RETFIE', 'RETLW', 'RETURN', 'SLEEP', 'SUBLW', 'XORLW', 'ADDLW', 'ANDLW',
)

keywords = (
    'EQU', 'CBLOCK', 'ENDCB', 'CUSTOM', 'ENDCUSTOM', 'DATA', 'MESSAGE', 'ORG', 'LIST', 'MIFDEF', 'MENDIF',
    'FILL', 'END', 'DATA', 'PAGESEL', 'BANKSEL', 'LOCAL', 'MIFNDER', 'MAXRAM', 'BADRAM', 'NOLIST', 'INCLUDE',
    'NAME', 'RADIX',
)

tokens = preprocessor + mnemonics + keywords + (
    'EOF', 'ERROR', 'NUMBER', 'ID',
    'CHARACTER', 'NEQ', 'LEQ', 'GEQ',
    'LSH', 'LSH', 'RSH', 'UPPER', 'HIGH',
    'LOW', 'LOR', 'LAND', 'NEWLINE'
)

t_ignore = ' \t'


def t_REM(t):
    r'REM .*'
    return t


def t_ID(t):
    r'[A-Z][A-Z0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t


t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\^'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'<>'
t_COMMA = r'\,'
t_SEMI = r';'
t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*?\"'


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)


lex(debug=0)
