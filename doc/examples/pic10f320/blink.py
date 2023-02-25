from time import sleep
from picpy.devices.p10f320 import *


@interrupt
def interrupt():
    pass


@start
def main():
    led = Pin(PORTA, RA0, Pin.OUT)
    while True:
        led.value = 1
        sleep(0.5)
        led.off()
        sleep(0.5)


build(PicPy.HEX)
