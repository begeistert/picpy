from .expression import AssemblyUnaryExpr


class LogicalNotNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a logical operation."""

    def __init__(self, right):
        self.right = right

    def evaluate(self, env):
        return not self.right.evaluate(env)


class LogicalAndNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a logical operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) and self.right.evaluate(env)


class LogicalOrNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a logical operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) or self.right.evaluate(env)


class LowerThanEqualsNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a logical operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) <= self.right.evaluate(env)


class GreaterThanEqualsNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a logical operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) >= self.right.evaluate(env)


class LowerThanNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a logical operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) < self.right.evaluate(env)


class GreaterThanNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a logical operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) > self.right.evaluate(env)


class EqualsNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a logical operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) == self.right.evaluate(env)


class NotEqualsNode(AssemblyUnaryExpr):
    """Base class for all assembly nodes that represent a logical operation."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, env):
        return self.left.evaluate(env) != self.right.evaluate(env)
