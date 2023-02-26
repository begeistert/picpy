from .parser.nodes import DeclareObject


def link(references):
    pass


class Linker:
    def __init__(self):
        self._environment = {}
        self._objects = {}

    @property
    def environment(self):
        return self._environment

    def link(self, declarations):
        for declaration in declarations:
            if isinstance(declaration, DeclareObject) and declaration.reference is 'const':
                self._environment[declaration.name] = declaration.args[0].value
            else:
                self._objects[declaration.name] = declaration
