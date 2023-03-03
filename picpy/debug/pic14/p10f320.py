from .midrange import MidrangeDebugger


class P10F320(MidrangeDebugger):
    def __init__(self, program, symbols):
        super().__init__(program, symbols)
        self._memory = {i: 0 for i in range(256)}
        self.INDF = lambda value=None: self._memory[self.FSR]
        self.TMR0 = lambda value=None: self._memory[0x01]
        self.PCL = lambda value=None: self._memory[0x02]
        self.STATUS = lambda value=None: self._memory[0x03]
        self.FSR = lambda value=None: self._memory[0x04]
        self.PORTA = lambda value=None: self._memory[0x05]
        self.PORTB = lambda value=None: self._memory[0x06]
        self.EEDATA = lambda value=None: self._memory[0x08]
        self.EEADR = lambda value=None: self._memory[0x09]
        self.PCLATH = lambda value=None: self._memory[0x0A]
        self.INTCON = lambda value=None: self._memory[0x0B]
        self.PIR1 = lambda value=None: self._memory[0x0C]
        self.TMR1L = lambda value=None: self._memory[0x0E]
        self.TMR1H = lambda value=None: self._memory[0x0F]
        self.T1CON = lambda value=None: self._memory[0x10]
        self.RCSTA = lambda value=None: self._memory[0x18]
        self.TXREG = lambda value=None: self._memory[0x19]
        self.RCREG = lambda value=None: self._memory[0x1A]
        self.TXSTA = lambda value=None: self._memory[0x98]
        self.SPBRG = lambda value=None: self._memory[0x99]
        self.EECON1 = lambda value=None: self._memory[0x18C]
        self.EECON2 = lambda value=None: self._memory[0x18D]


device = P10F320([], {})


INDF = device.INDF

