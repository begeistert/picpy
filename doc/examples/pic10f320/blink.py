from picpy.devices.p10f320 import *


@interrupt
def interrupt():
    pass


@start(start_at=0x00, interrupt_at=0x04)
def main():
    pass


build(PicPy.HEX)
