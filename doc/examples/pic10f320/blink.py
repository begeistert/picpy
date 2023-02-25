from time import sleep
from picpy.devices.p10f320 import *


@interrupt
def interrupt():
    pass


@start
@config(0x3F3A)
def main():
    #  TRISA[RA0] = 0  # Set RA0 to output
    led = Pin(PORTA, RA0, Pin.OUT)  # Create a pin object for RA0
    while True:
        led.value = 1
        sleep(0.5)
        led.off()
        sleep(0.5)
        Pic.sleep()


build(PicPy.HEX)
