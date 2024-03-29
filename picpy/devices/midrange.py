from picpy.picpy import build, PicPy


ARCH_MIDRANGE = 16


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


class Pic:
    @staticmethod
    def sleep():
        pass


# ==================== Helper Functions ====================
def assembly(code: str):
    """Add assembly code to the program.

    Args:
        code: The assembly code to add.
    """
    pass


def const(value):
    """Create a constant.

    Args:
        value: The value of the constant.
    """
    pass


def start(start_at=0, interrupt_at=0x04):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


def config(*args, **kwargs):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


def interrupt(source=0):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


def frequency(freq, source='internal'):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


# Configuration decorators
def watchdog(value):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


def mclr(value):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


def brownout(value):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


def low_voltage(value):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


def power_up(value):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


def debug(value):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


def lvp(value):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator


def code_protection(value):
    def decorator(function):
        def wrapper():
            pass

        return wrapper

    return decorator

