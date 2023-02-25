import inspect
import sys
from .core.compiler import Compiler


class PicPy:
    ASM = 0x01
    HEX = 0x02


def build(file_type: int):
    """Build the program.
    """
    code = ''
    for frame in inspect.stack():
        if 'build' in frame.code_context[0]:
            code = open(frame.filename).read()
            break
    if code == '':
        print("Couldn't find the code to build.")
        sys.exit(1)
    else:
        compiler = Compiler()
        code = compiler.compile(code)

    print(code)
