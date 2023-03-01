class DeviceDebugger:
    def __init__(self):
        self._PC = 0
        self._W = 0
        self._status = 0
        self._stack = []
        self._memory = {}
        self._labels = {}
        self._program = []
        self._symbols = {}

    def reset(self):
        raise NotImplementedError

    def step(self):
        raise NotImplementedError

