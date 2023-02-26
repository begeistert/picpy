from .parser import parse
from .linker import link
from .interpreter import Interpreter
#from .assembler import


class Compiler:
    def __init__(self):
        pass
        # self._assembler = Assembler()

    def compile(self, source):
        # self._assembler.assemble(self._parser.parse(source))
        interpreter = Interpreter()

        abstract_syntax_tree = parse(source)
        plain_syntax_tree = interpreter.interpret(abstract_syntax_tree)
        environment = link(plain_syntax_tree)

        return parse(source)

