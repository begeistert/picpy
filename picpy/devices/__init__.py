from .p10f320 import *


# ==================== Helper Classes ====================
class Pin:
    """A pin on the PIC.

    Attributes:
        port: The port the pin is on.
        bit: The bit the pin is on.
    """
    OUT = 0
    IN = 1

    def __init__(self, port, bit, mode=IN):
        self.port = port
        self.bit = bit
        self.mode = mode

    @property
    def value(self, value=None):
        pass

    @value.setter
    def value(self, value):
        pass

    def on(self):
        pass

    def off(self):
        pass

    def __repr__(self):
        return f"Pin({self.port}, {self.bit}, {self.mode})"

    def __str__(self):
        return f"{self.port}.{self.bit} = {'OUT' if self.mode == Pin.OUT else 'IN'}"


# ==================== Helper Functions ====================
def assembly(code: str):
    """Add assembly code to the program.

    Args:
        code: The assembly code to add.
    """
    pass
