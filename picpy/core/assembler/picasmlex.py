from .lex import *

preprocessor = (
    'INCLUDE', 'DEFINE', 'UNDEF', 'IFDEF', 'IFNDEF', 'ELSE', 'ENDIF',
)

mnemonics = (
    'ADDWF', 'ANDWF', 'CLRF', 'CLRW', 'COMF', 'DECF', 'DECFSZ', 'INCF', 'INCFSZ',
    'IORWF', 'MOVF', 'MOVWF', 'RLF', 'RRF', 'SUBWF', 'SWAPF', 'XORWF', 'BCF', 'BSF',
    'BTFSC', 'BTFSS', 'BC', 'BNC', 'BZ', 'BNZ', 'BRA', 'CALL', 'CLRWDT', 'GOTO',
    'RETFIE', 'RETLW', 'RETURN', 'SLEEP', 'SUBLW', 'XORLW', 'ADDLW', 'ANDLW',
    'NOP', 'IORLW', 'MOVLW', 'TRIS', 'OPTION'
)

keywords = (
    'CBLOCK', 'ENDCB', 'CUSTOM', 'ENDCUSTOM', 'MESSAGE', 'ORG', 'LIST', 'MIFDEF', 'MENDIF',
    'FILL', 'END', 'DATA', 'PAGESEL', 'BANKSEL', 'LOCAL', 'MIFNDER', 'MAXRAM', 'BADRAM', 'NOLIST', 'MINCLUDE',
    'NAME', 'RADIX',
)

tokens = preprocessor + mnemonics + keywords + (
    'EOF', 'ERROR', 'NUMBER', 'ID', 'PLUS',
    'MINUS', 'DIVIDE', 'POWER', 'COMMA', 'MODULUS',
    'CHARACTER', 'EQUALS', 'NEQ', 'LEQ', 'GEQ',
    'LSHIFT', 'RSHIFT', 'UPPER', 'HIGH', 'MULTIPLICATIVE',
    'LOW', 'LOR', 'LAND', 'NEWLINE', 'NOT', 'EQU',
    'GT', 'LT', 'BITWISE_OR', 'BITWISE_AND',
    'BITWISE_XOR', 'BITWISE_NOT', 'LPAREN', 'RPAREN',
    'DOLLAR', 'STRING', 'TWO_DOTS'
)

t_ignore = ' \t'


def t_ID(t):
    r"""[A-Z][A-Z0-9]*"""
    if t.value in keywords or t.value in mnemonics:
        t.type = t.value
    return t


t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_POWER = r'\^'
t_DIVIDE = r'/'
t_MULTIPLICATIVE = r'\*'
t_MODULUS = r'%'

t_RSHIFT = r'>>'
t_LSHIFT = r'<<'

t_LEQ = r'<='
t_GEQ = r'>='
t_NEQ = r'!='
t_EQU = r'=='

t_GT = r'>'
t_LT = r'<'

t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOLLAR = r'\$'
t_TWO_DOTS = r':'

# Expression tokens
t_BITWISE_OR = r'\|'
t_BITWISE_AND = r'&'
t_BITWISE_XOR = r'\^'
t_BITWISE_NOT = r'~'

# Logical tokens
t_NOT = r'!'
t_LOR = r'\|\|'
t_LAND = r'&&'

# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LT = r'<'
# t_LE = r'<='
# t_GT = r'>'
# t_GE = r'>='
# t_NE = r'<>'
# t_COMMA = r'\,'
# t_SEMI = r';'
t_NUMBER = r'\d+'
# t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*?\"'
t_CHARACTER = r'\'[^\']\''
t_ignore_COMMENT = r';.*'


def t_NEWLINE(t):
    r"""\n"""
    t.lexer.lineno += 1
    return t


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)


lex(debug=0)
