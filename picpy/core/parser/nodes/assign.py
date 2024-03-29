from .node import PyNode


class Assign(PyNode):
    def __init__(self, line, column, target, value):
        super().__init__(line, column)
        self.target = target
        self.value = value

    def resolve(self):
        pass

    def __repr__(self):
        return f'Assign({self.target}, {self.value})'

    def __eq__(self, other):
        return isinstance(other, Assign) and self.target == other.target and self.value == other.value

    def __hash__(self):
        return hash((self.target, self.value))

    def accept(self, visitor):
        return visitor.visit_assign(self)


class AssignToAttribute(PyNode):
    def __init__(self, line, column, target, attribute, value):
        super().__init__(line, column)
        self.target = target
        self.attribute = attribute
        self.value = value

    def resolve(self):
        context = self._context
        natives = context.natives
        env = context.environment
        if natives.get(self.target) is not None:
            attr = getattr(natives.get(self.target), self.attribute)
            if attr is not None:
                return attr(self.value)

    def __repr__(self):
        return f'AssignToAttribute({self.target}, {self.value})'

    def __eq__(self, other):
        return isinstance(other, AssignToAttribute) and self.target == other.target and self.value == other.value

    def __hash__(self):
        return hash((self.target, self.value))

    def accept(self, visitor):
        return visitor.visit_assign_array(self)
