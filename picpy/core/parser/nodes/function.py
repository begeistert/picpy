from .node import PyNode


class Function(PyNode):

    def __init__(self, line, column, name, args, body, decorator_list=None, returns=None):
        super().__init__(line, column)
        self.name = name
        self.args = args
        self.body = body
        self.decorator_list = decorator_list
        self.returns = returns

    def has_decorator(self, decorator):
        return decorator in self.decorator_list

    def resolve(self):
        pass

    def __repr__(self):
        return f'Function({self.name}, {self.args}, {self.body})'

    def __eq__(self, other):
        return isinstance(other,
                          Function) and self.name == other.name and self.args == other.args and self.body == other.body

    def __hash__(self):
        return hash((self.name, self.args, self.body))

    def accept(self, visitor):
        return visitor.visit_function(self)
