class MemoryMap:
    def __init__(self, size, bad_ram=None, bad_rom=None):
        self._size = size
        self._memory = {}
        self._bad_ram = bad_ram
        self._bad_rom = bad_rom

    def allocate(self, address, value):
        if address < self._size:
            if self._bad_ram is not None and address in self._bad_ram:
                raise Exception(f'Address {address} is bad RAM')
            self._memory[address] = value
        else:
            raise Exception(f'Address {address} is out of range')
