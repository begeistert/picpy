from .parser.nodes import DeclareObject


def link(references):
    pass


class Linker:
    def __init__(self):
        self._environment = {}
        self._natives = {}
        self._objects = {}
        self._labels = {}

    @property
    def environment(self):
        return self._environment

    @property
    def natives(self):
        return self._natives

    @property
    def objects(self):
        return self._objects

    def link(self, declarations):
        for declaration in declarations:
            if isinstance(declaration, DeclareObject) and declaration.reference is 'const':
                self._environment[declaration.name] = declaration.args[0].value
            else:
                match declaration.reference:
                    case 'Pin':
                        if self._environment['ARCH'] == 14:
                            from .evaluators.midrange import Pin

                            self._natives[declaration.name] = Pin(*declaration.args,
                                                                  has_tris=self._environment['HAS_TRIS'])
                    case _:
                        # Custom object
                        pass
