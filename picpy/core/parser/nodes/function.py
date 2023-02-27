from .node import PyNode
from . import Name, Call


class Function(PyNode):

    def __init__(self, line, column, name, args, body, decorator_list=None, returns=None):
        super().__init__(line, column)
        self.name = name
        self.args = args
        self.body = body
        self.decorator_list = decorator_list
        self.decorator_list_names = []
        for decorator in self.decorator_list:
            match decorator:
                case Name():
                    self.decorator_list_names.append(decorator.name)
                case Call():
                    self.decorator_list_names.append(decorator.target)
        self.returns = returns

    def has_decorator(self, decorator):
        return decorator in self.decorator_list_names

    def get_decorator(self, decorator):
        for dec in self.decorator_list:
            match dec:
                case Name():
                    if dec.name == decorator:
                        return dec
                case Call():
                    if dec.target == decorator:
                        return dec

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
