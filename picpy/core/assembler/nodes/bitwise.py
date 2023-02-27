from .expression import AssemblyUnaryExpr


class BitwiseNotNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a bitwise operation."""

    def __init__(self, right):
        self.right = right

    def evaluate(self, env):
        return ~self.right.evaluate(env)


class BitwiseAndNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a bitwise operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) & self.right.evaluate(env)


class BitwiseOrNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a bitwise operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) | self.right.evaluate(env)


class BitwiseXorNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a bitwise operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) ^ self.right.evaluate(env)

