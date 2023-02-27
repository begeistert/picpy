class Mnemonic:

    def __init__(self, register=0, bit=0, destination=0, constant=0):
        self.mnemonic = 0
        self.register = register
        self.bit = bit
        self.destination = destination
        self.constant = constant
        self._label = None

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value

    def emit(self):
        raise NotImplementedError()

    def __repr__(self):
        return f"Mnemonic({self.__class__.__name__}, {self.register}, {self.bit}, {self.destination})"

    def __str__(self):
        return f"{self.__class__.__name__} {self.register}"
