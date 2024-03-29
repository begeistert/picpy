from time import sleep
from picpy.devices.p10f320 import *


@interrupt
def interrupt():
    pass


@start
@mclr(False)
@watchdog(False)
@code_protection(False)
@frequency(4_000_000, source='internal')
def main():
    #  TRISA[RA0] = 0  # Set RA0 to output
    assembly("""
    clrf ANSELA
    addwf TRISA, f
    addwf PORTB
    """)
    led = Pin(PORTA, RA0, Pin.OUT)  # Create a pin object for RA0
    while True:
        led.value = 1
        sleep(0.5)
        led.off()
        sleep(0.5)


build(PicPy.HEX)
