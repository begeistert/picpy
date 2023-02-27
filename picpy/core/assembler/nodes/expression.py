from .base import AssemblyNode


class AssemblyUnaryExpr(AssemblyNode):
    """Base class for all assembly unary expressions."""

    def evaluate(self, env):
        """Evaluates the expression."""
        raise NotImplementedError


class Value(AssemblyUnaryExpr):
    """Represents a value in the assembly code."""

    def __init__(self, integer=None, string=None, identifier=None, character=None, current_memory_address=None):
        self.value = integer
        self.type = 0

        if string is not None:
            self.value = string
            self.type = 2

        if identifier is not None:
            self.value = identifier
            self.type = 1

        if character is not None:
            self.value = character
            self.type = 3

        if current_memory_address is not None:
            self.value = None
            self.type = 4

    def evaluate(self, env):
        match self.type:
            case 0:
                return self.value
            case 1:
                return env.get(self.value).value
            case 2:
                return self.value
            case 3:
                return ord(self.value)
            case 4:
                return env["__CURRENT_MEMORY_ADDRESS__"]

    def __eq__(self, other):
        return self.value == other

    def __and__(self, other):
        if self.type != 0:
            raise TypeError("Cannot perform bitwise operations on non-integer values, please evaluate before.")
        return self.value & other

    def __repr__(self):
        return self.value


class LowExprNode(AssemblyUnaryExpr):
    """Represents the low expression in the assembly code."""

    def __init__(self, right):
        self.right = right

    def evaluate(self, env):
        return self.right.evaluate(env) & 0xFF

    def __repr__(self):
        return "LowExprNode(%s)" % self.right


class HighExprNode(AssemblyUnaryExpr):
    """Represents the high expression in the assembly code."""

    def __init__(self, right):
        self.right = right

    def evaluate(self, env):
        return (self.right.evaluate(env) >> 8) & 0xFF

    def __repr__(self):
        return "HighExprNode(%s)" % self.right


class UpperExprNode(AssemblyUnaryExpr):
    """Represents the upper expression in the assembly code."""

    def __init__(self, right):
        self.right = right

    def evaluate(self, env):
        return (self.right.evaluate(env) >> 16) & 0xFF

    def __repr__(self):
        return "UpperExprNode(%s)" % self.right