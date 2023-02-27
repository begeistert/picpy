from .yacc import *
from .nodes import *
from .program import AssemblyProgram
import picpy.core.assembler.picasmlex as picasmlex

tokens = picasmlex.tokens

"""precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
    ('right', 'UMINUS')
)"""


# A BASIC program is a series of statements.  We represent the program as a
# dictionary of tuples indexed by line number.


def p_program(p):
    """program : program newlines statement
               | statement"""
    if len(p) == 2 and p[1]:
        stat = p[1]
        p[0] = AssemblyProgram(stat)
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = {}
        if p[2]:
            line, stat = p[2]
            p[0][line] = stat


def p_newlines(p):
    """newlines : newlines NEWLINE
                | NEWLINE"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]


"""line
    : instruction
    | label instruction
    | label ':' instruction
    | label newlines instruction
    | label ':' newlines instruction
    | macro
    | label macro
    | label ':' macro
    | label newlines macro
    | label ':' newlines macro
    | configuration 
    | preprocessor_directive;
"""


def p_statement(p):
    """statement : instruction"""
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
    elif len(p) == 5:
        p[0] = p[1] + p[2] + p[3] + p[4]
    elif len(p) == 6:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]


"""instruction
    : OP_ADDWF source ',' destination  
    | OP_ADDWF source
    | OP_ANDWF source ',' destination  
    | OP_ANDWF source
    | OP_CLRF source  
    | OP_CLRW                 
    | OP_COMF source ',' destination
    | OP_COMF source
    | OP_DECF source ',' destination
    | OP_DECF source
    | OP_DECFSZ source ',' destination
    | OP_DECFSZ source
    | OP_INCF source ',' destination
    | OP_INCF source
    | OP_INCFSZ source ',' destination
    | OP_INCFSZ source
    | OP_IORWF source ',' destination
    | OP_IORWF source
    | OP_MOVF source ',' destination
    | OP_MOVF source
    | OP_MOVWF destination
    | OP_NOP             
    | OP_RLF source ',' destination
    | OP_RLF source
    | OP_RRF source ',' destinatio
    | OP_RRF source
    | OP_SUBWF source ',' destination
    | OP_SUBWF source
    | OP_SWAPF source ',' destination
    | OP_SWAPF source
    | OP_XORWF source ',' destination
    | OP_XORWF source
    | OP_BCF source 
    | OP_BCF source ',' destination
    | OP_BSF source
    | OP_BSF source ',' destination
    | OP_BTFSC source
    | OP_BTFSC source ',' destination
    | OP_BTFSS source
    | OP_BTFSS source ',' destination
    | OP_ADDLW source
    | OP_ANDLW source
    | OP_CALL source
    | OP_CLRWDT
    | OP_GOTO source
    | OP_IORLW source
    | OP_MOVLW source
    | OP_RETFIE
    | OP_RETLW source
    | OP_RETURN
    | OP_SLEEP 
    | OP_SUBLW source
    | OP_TRIS source
    | OP_OPTION
    | OP_XORLW source  
   ;"""


def p_instruction(p):
    """instruction : CLRF ID
    """
    p[0] = MnemonicNode(p[1], register=p[2])


bparser = yacc()


def parse(data, debug=0):
    bparser.error = 0
    p = bparser.parse(data, debug=debug)
    if bparser.error:
        return None
    return p
