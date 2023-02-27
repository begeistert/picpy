from .parser import parse
from .interpreter import Interpreter
from .assembler.picasm import Assembler


class Compiler:
    def __init__(self):
        pass
        # self._assembler = Assembler()

    def compile(self, source):
        # self._assembler.assemble(self._parser.parse(source))
        interpreter = Interpreter()
        assembler = Assembler()

        abstract_syntax_tree = parse(source)
        code, linker = interpreter.interpret(abstract_syntax_tree)
        assembler.assemble(code, linker)

        return parse(source)

