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
    elif len(p) == 4:
        p[0] = p[1] + p[3]


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

"""instruction
    : OP_ADDWF source ',' destination  """


def p_addwf_instruction(p):
    """instruction : ADDWF source COMMA source
                   | ADDWF source"""
    if len(p) == 5:
        p[0] = MnemonicNode(p[1], register=p[2], destination=p[4])
    else:
        p[0] = MnemonicNode(p[1], register=p[2])


def p_clrf_instruction(p):
    """instruction : CLRF source"""
    p[0] = MnemonicNode(p[1], register=p[2])


# Data types
def p_id(p):
    """id : ID"""
    p[0] = p[1]


def p_string(p):
    """string : STRING"""
    p[0] = p[1]


def p_number(p):
    """number : NUMBER"""
    p[0] = p[1]


def p_character(p):
    """character : CHARACTER"""
    p[0] = p[1]


def p_source(p):
    """source : expression"""
    p[0] = p[1]


# Expressions
def p_expression(p):
    """expression : bitwise_not_expression"""
    p[0] = p[1]


def p_bitwise_not_expression(p):
    """bitwise_not_expression : BITWISE_NOT logical_not_expression
                              | logical_not_expression"""
    if len(p) == 3:
        p[0] = BitwiseNotNode(p[2])
    else:
        p[0] = p[1]


def p_logical_not_expression(p):
    """logical_not_expression : NOT negate_expression
                              | negate_expression"""
    if len(p) == 3:
        p[0] = LogicalNotNode(p[2])
    else:
        p[0] = p[1]


def p_negate_expression(p):
    """negate_expression : MINUS low_expression
                         | low_expression"""
    if len(p) == 3:
        p[0] = BitwiseNotNode(p[2])
    else:
        p[0] = p[1]


def p_low_expression(p):
    """low_expression : LOW high_expression
                      | high_expression"""
    if len(p) == 3:
        p[0] = LowExprNode(p[2])
    else:
        p[0] = p[1]


def p_high_expression(p):
    """high_expression : HIGH upper_expression
                       | upper_expression"""
    if len(p) == 3:
        p[0] = HighExprNode(p[2])
    else:
        p[0] = p[1]


def p_upper_expression(p):
    """upper_expression : UPPER basic_expression
                        | basic_expression"""
    if len(p) == 3:
        p[0] = UpperExprNode(p[2])
    else:
        p[0] = p[1]


def p_basic_expression(p):
    """basic_expression : modulus_expression"""
    p[0] = p[1]


def p_modulus_expression(p):
    """modulus_expression : modulus_expression MODULUS divisive_expression
                          | divisive_expression"""
    if len(p) == 4:
        p[0] = ModulusNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_divisive_expression(p):
    """divisive_expression : divisive_expression DIVIDE multiplicative_expression
                           | multiplicative_expression"""
    if len(p) == 4:
        p[0] = DivideNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_multiplicative_expression(p):
    """multiplicative_expression : multiplicative_expression MULTIPLICATIVE subtractive_expression
                                 | subtractive_expression"""
    if len(p) == 4:
        p[0] = MultiplyNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_subtractive_expression(p):
    """subtractive_expression : subtractive_expression MINUS additive_expression
                              | additive_expression"""
    if len(p) == 4:
        p[0] = SubtractNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_additive_expression(p):
    """additive_expression : additive_expression PLUS shift_expression
                           | shift_expression"""
    if len(p) == 4:
        p[0] = AddNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_shift_expression(p):
    """shift_expression : right_shift_expression"""
    p[0] = p[1]


def p_right_shift_expression(p):
    """right_shift_expression : right_shift_expression RSHIFT left_shift_expression
                              | left_shift_expression"""
    if len(p) == 4:
        p[0] = RightShiftNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_left_shift_expression(p):
    """left_shift_expression : left_shift_expression LSHIFT equal_expression
                             | equal_expression"""
    if len(p) == 4:
        p[0] = LeftShiftNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_equal_expression(p):
    """equal_expression : lower_than_equals_expression"""
    p[0] = p[1]


def p_lower_than_equals_expression(p):
    """lower_than_equals_expression : lower_than_equals_expression LEQ greater_than_equals_expression
                                    | greater_than_equals_expression"""
    if len(p) == 4:
        p[0] = LowerThanEqualsNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_greater_than_equals_expression(p):
    """greater_than_equals_expression : greater_than_equals_expression GEQ not_equals_expression
                                      | not_equals_expression"""
    if len(p) == 4:
        p[0] = GreaterThanEqualsNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_not_equals_expression(p):
    """not_equals_expression : not_equals_expression NEQ equals_expression
                             | equals_expression"""
    if len(p) == 4:
        p[0] = NotEqualsNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_equals_expression(p):
    """equals_expression : equals_expression EQU than_expression
                         | than_expression"""
    if len(p) == 4:
        p[0] = EqualsNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_than_expression(p):
    """than_expression : greater_than_expression"""
    p[0] = p[1]


def p_greater_than_expression(p):
    """greater_than_expression : greater_than_expression GT lower_than_expression
                               | lower_than_expression"""
    if len(p) == 4:
        p[0] = GreaterThanNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_lower_than_expression(p):
    """lower_than_expression : lower_than_expression LT bitwise_expression
                             | bitwise_expression"""
    if len(p) == 4:
        p[0] = LowerThanNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_bitwise_expression(p):
    """bitwise_expression : bitwise_xor_expression"""
    p[0] = p[1]


def p_bitwise_xor_expression(p):
    """bitwise_xor_expression : bitwise_xor_expression BITWISE_XOR bitwise_or_expression
                              | bitwise_or_expression"""
    if len(p) == 4:
        p[0] = BitwiseXorNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_bitwise_or_expression(p):
    """bitwise_or_expression : bitwise_or_expression BITWISE_OR bitwise_and_expression
                             | bitwise_and_expression"""
    if len(p) == 4:
        p[0] = BitwiseOrNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_bitwise_and_expression(p):
    """bitwise_and_expression : bitwise_and_expression BITWISE_AND logical_expression
                              | logical_expression"""
    if len(p) == 4:
        p[0] = BitwiseAndNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_logical_expression(p):
    """logical_expression : logical_and_expression"""
    p[0] = p[1]


def p_logical_and_expression(p):
    """logical_and_expression : logical_and_expression LAND logical_or_expression
                              | logical_or_expression"""
    if len(p) == 4:
        p[0] = LogicalAndNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_logical_or_expression(p):
    """logical_or_expression : logical_or_expression LOR unary_expression
                             | unary_expression"""
    if len(p) == 4:
        p[0] = LogicalOrNode(p[1], p[3])
    else:
        p[0] = p[1]


def p_unary_expression(p):
    """unary_expression : primary_expression"""
    p[0] = p[1]


def p_primary_expression_nested(p):
    """primary_expression : LPAREN expression RPAREN"""
    p[0] = p[2]


def p_primary_expression_number(p):
    """primary_expression : number"""
    p[0] = Value(integer=int(p[1]))


def p_primary_expression_id(p):
    """primary_expression : id"""
    p[0] = Value(identifier=p[1])


def p_primary_expression_string(p):
    """primary_expression : string"""
    p[0] = Value(string=p[1])


def p_primary_expression_character(p):
    """primary_expression : character"""
    p[0] = Value(character=p[1])


def p_primary_expression_dollar(p):
    """primary_expression : DOLLAR"""
    p[0] = Value(current_memory_address=True)


bparser = yacc()


def parse(data, debug=0):
    bparser.error = 0
    p = bparser.parse(data, debug=debug)
    if bparser.error:
        return None
    return p
