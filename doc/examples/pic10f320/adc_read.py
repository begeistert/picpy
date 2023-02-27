from picpy.devices.p10f320 import *


@interrupt
def interrupt():
    pass


@start
@config(0x3F3A)
def main():
    pass


build(PicPy.HEX)
