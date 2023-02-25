import ast


class Parser:
    def __init__(self):
        self._parsed = []

    def parse(self, source):
        self._parsed = []
        self.visit(ast.parse(source))
        return self._parsed
