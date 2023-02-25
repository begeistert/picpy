from . import assembly
from picpy.picpy import build, PicPy


def interrupt(source=0):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

