from .expression import AssemblyUnaryExpr


class ModulusNode(AssemblyUnaryExpr):
    """Represents the modulus expression in the assembly code."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return env[self.left] % env[self.right]

    def __repr__(self):
        return "ModulusNode(%s)" % self.right


class DivideNode(AssemblyUnaryExpr):
    """Represents the divide expression in the assembly code."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return env[self.left] / env[self.right]

    def __repr__(self):
        return "DivideNode(%s)" % self.right


class MultiplyNode(AssemblyUnaryExpr):
    """Represents the multiply expression in the assembly code."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return env[self.left] * env[self.right]

    def __repr__(self):
        return "MultiplyNode(%s)" % self.right


class SubtractNode(AssemblyUnaryExpr):
    """Represents the subtract expression in the assembly code."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return env[self.left] - env[self.right]

    def __repr__(self):
        return "SubtractNode(%s)" % self.right


class AddNode(AssemblyUnaryExpr):
    """Represents the add expression in the assembly code."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return env[self.left] + env[self.right]

    def __repr__(self):
        return "AddNode(%s)" % self.right

