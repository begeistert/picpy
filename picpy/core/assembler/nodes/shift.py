from .expression import AssemblyUnaryExpr


class LeftShiftNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a shift operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) << self.right.evaluate(env)


class RightShiftNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a shift operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) >> self.right.evaluate(env)



