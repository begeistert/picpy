from .parser import Parser
# from .assembler import Assembler


class Compiler:
    def __init__(self):
        self._parser = Parser()
        # self._assembler = Assembler()

    def compile(self, source):
        # self._assembler.assemble(self._parser.parse(source))
        return self._parser.parse(source)
