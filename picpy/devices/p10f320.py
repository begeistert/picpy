from .midrange import *

# ============== Device Information ==============
ARCH = const(14)
MAX_RAM = const(0x007F)
BAD_RAM = const(0x002F)

HAS_TRIS = const(True)

# ============== Working Registers ==============

W = const(0x0000)
F = const(0x0001)

# ============== Bank0 ==============

INDF = const(0x0000)
TMR0 = const(0x0001)
PCL = const(0x0002)
STATUS = const(0x0003)
FSR = const(0x0004)
PORTA = const(0x0005)
TRISA = const(0x0006)
LATA = const(0x0007)
ANSELA = const(0x0008)
WPUA = const(0x0009)
PCLATH = const(0x000a)
INTCON = const(0x000b)
PIR1 = const(0x000c)
PIE1 = const(0x000d)
OPTION_REG = const(0x000e)
PCON = const(0x000f)
OSCCON = const(0x0010)
TMR2 = const(0x0011)
PR2 = const(0x0012)
T2CON = const(0x0013)
PWM1DCL = const(0x0014)
PWM1DCH = const(0x0015)
PWM1CON = const(0x0016)
PWM1CON0 = const(0x0016)
PWM2DCL = const(0x0017)
PWM2DCH = const(0x0018)
PWM2CON = const(0x0019)
PWM2CON0 = const(0x0019)
IOCAP = const(0x001a)
IOCAN = const(0x001b)
IOCAF = const(0x001c)
FVRCON = const(0x001d)
ADRES = const(0x001e)
ADCON = const(0x001f)
PMADR = const(0x0020)
PMADRL = const(0x0020)
PMADRH = const(0x0021)
PMDAT = const(0x0022)
PMDATL = const(0x0022)
PMDATH = const(0x0023)
PMCON1 = const(0x0024)
PMCON2 = const(0x0025)
CLKRCON = const(0x0026)
NCO1ACC = const(0x0027)
NCO1ACCL = const(0x0027)
NCO1ACCH = const(0x0028)
NCO1ACCU = const(0x0029)
NCO1INC = const(0x002a)
NCO1INCL = const(0x002a)
NCO1INCH = const(0x002b)
NCO1INCU = const(0x002c)
NCO1CON = const(0x002d)
NCO1CLK = const(0x002e)
WDTCON = const(0x0030)
CLC1CON = const(0x0031)
CLC1SEL0 = const(0x0032)
CLC1SEL1 = const(0x0033)
CLC1POL = const(0x0034)
CLC1GLS0 = const(0x0035)
CLC1GLS1 = const(0x0036)
CLC1GLS2 = const(0x0037)
CLC1GLS3 = const(0x0038)
CWG1CON0 = const(0x0039)
CWG1CON1 = const(0x003a)
CWG1CON2 = const(0x003b)
CWG1DBR = const(0x003c)
CWG1DBF = const(0x003d)
VREGCON = const(0x003e)
BORCON = const(0x003f)

# ============== STATUS Bits ==============

C = const(0x0000)
DC = const(0x0001)
Z = const(0x0002)
NOT_PD = const(0x0003)
NOT_TO = const(0x0004)
RP0 = const(0x0005)
RP1 = const(0x0006)
IRP = const(0x0007)

# ============== PORTA Bits ==============

RA0 = const(0x0000)
RA1 = const(0x0001)
RA2 = const(0x0002)
RA3 = const(0x0003)

# ============== TRISA Bits ==============

TRISA0 = const(0x0000)
TRISA1 = const(0x0001)
TRISA2 = const(0x0002)

# ============== LATA Bits ==============

LATA0 = const(0x0000)
LATA1 = const(0x0001)
LATA2 = const(0x0002)

# ============== ANSELA Bits ==============

ANSA0 = const(0x0000)
ANSA1 = const(0x0001)
ANSA2 = const(0x0002)

# ============== WPUA Bits ==============

WPUA0 = const(0x0000)
WPUA1 = const(0x0001)
WPUA2 = const(0x0002)
WPUA3 = const(0x0003)

# ============== PCLATH Bits ==============

PCLH0 = const(0x0000)

# ============== INTCON Bits ==============

IOCIF = const(0x0000)
INTF = const(0x0001)
TMR0IF = const(0x0002)
IOCIE = const(0x0003)
INTE = const(0x0004)
TMR0IE = const(0x0005)
PEIE = const(0x0006)
GIE = const(0x0007)

# ============== PIR1 Bits ==============

TMR2IF = const(0x0001)
CLC1IF = const(0x0003)
NCO1IF = const(0x0004)
ADIF = const(0x0006)

# ============== PIE1 Bits ==============

TMR2IE = const(0x0001)
CLC1IE = const(0x0003)
NCO1IE = const(0x0004)
ADIE = const(0x0006)

# ============== OPTION_REG Bits ==============

PSA = const(0x0003)
T0SE = const(0x0004)
T0CS = const(0x0005)
INTEDG = const(0x0006)
NOT_WPUEN = const(0x0007)
PS0 = const(0x0000)
PS1 = const(0x0001)
PS2 = const(0x0002)

# ============== PCON Bits ==============

NOT_BOR = const(0x0000)
NOT_POR = const(0x0001)

# ============== OSCCON Bits ==============

HFIOFS = const(0x0000)
LFIOFR = const(0x0001)
HFIOFR = const(0x0003)
IRCF0 = const(0x0004)
IRCF1 = const(0x0005)
IRCF2 = const(0x0006)

# ============== T2CON Bits ==============

TMR2ON = const(0x0002)
T2CKPS0 = const(0x0000)
T2CKPS1 = const(0x0001)
TOUTPS0 = const(0x0003)
TOUTPS1 = const(0x0004)
TOUTPS2 = const(0x0005)
TOUTPS3 = const(0x0006)

# ============== PWM1DCL Bits ==============

PWM1DCL0 = const(0x0006)
PWM1DCL1 = const(0x0007)

# ============== PWM1DCH Bits ==============

PWM1DCH0 = const(0x0000)
PWM1DCH1 = const(0x0001)
PWM1DCH2 = const(0x0002)
PWM1DCH3 = const(0x0003)
PWM1DCH4 = const(0x0004)
PWM1DCH5 = const(0x0005)
PWM1DCH6 = const(0x0006)
PWM1DCH7 = const(0x0007)

# ============== PWM1CON Bits ==============

PWM1POL = const(0x0004)
PWM1OUT = const(0x0005)
PWM1OE = const(0x0006)
PWM1EN = const(0x0007)

# ============== PWM2DCL Bits ==============

PWM2DCL0 = const(0x0006)
PWM2DCL1 = const(0x0007)

# ============== PWM2DCH Bits ==============

PWM2DCH0 = const(0x0000)
PWM2DCH1 = const(0x0001)
PWM2DCH2 = const(0x0002)
PWM2DCH3 = const(0x0003)
PWM2DCH4 = const(0x0004)
PWM2DCH5 = const(0x0005)
PWM2DCH6 = const(0x0006)
PWM2DCH7 = const(0x0007)

# ============== PWM2CON Bits ==============

PWM2POL = const(0x0004)
PWM2OUT = const(0x0005)
PWM2OE = const(0x0006)
PWM2EN = const(0x0007)

# ============== IOCAP Bits ==============

IOCAP0 = const(0x0000)
IOCAP1 = const(0x0001)
IOCAP2 = const(0x0002)
IOCAP3 = const(0x0003)

# ============== IOCAN Bits ==============

IOCAN0 = const(0x0000)
IOCAN1 = const(0x0001)
IOCAN2 = const(0x0002)
IOCAN3 = const(0x0003)

# ============== IOCAF Bits ==============

IOCAF0 = const(0x0000)
IOCAF1 = const(0x0001)
IOCAF2 = const(0x0002)
IOCAF3 = const(0x0003)

# ============== FVRCON Bits ==============

TSRNG = const(0x0004)
TSEN = const(0x0005)
FVRRDY = const(0x0006)
FVREN = const(0x0007)
ADFVR0 = const(0x0000)
ADFVR1 = const(0x0001)

# ============== ADCON Bits ==============

ADON = const(0x0000)
GO_NOT_DONE = const(0x0001)
CHS0 = const(0x0002)
CHS1 = const(0x0003)
CHS2 = const(0x0004)
ADCS0 = const(0x0005)
ADCS1 = const(0x0006)
ADCS2 = const(0x0007)

# ============== PMADRH Bits ==============

PMADR8 = const(0x0000)

# ============== PMCON1 Bits ==============

RD = const(0x0000)
WR = const(0x0001)
WREN = const(0x0002)
WRERR = const(0x0003)
FREE = const(0x0004)
LWLO = const(0x0005)
CFGS = const(0x0006)

# ============== CLKRCON Bits ==============

CLKROE = const(0x0006)

# ============== NCO1ACCL Bits ==============

NCO1ACC0 = const(0x0000)
NCO1ACC1 = const(0x0001)
NCO1ACC2 = const(0x0002)
NCO1ACC3 = const(0x0003)
NCO1ACC4 = const(0x0004)
NCO1ACC5 = const(0x0005)
NCO1ACC6 = const(0x0006)
NCO1ACC7 = const(0x0007)

# ============== NCO1ACCH Bits ==============

NCO1ACC8 = const(0x0000)
NCO1ACC9 = const(0x0001)
NCO1ACC10 = const(0x0002)
NCO1ACC11 = const(0x0003)
NCO1ACC12 = const(0x0004)
NCO1ACC13 = const(0x0005)
NCO1ACC14 = const(0x0006)
NCO1ACC15 = const(0x0007)

# ============== NCO1ACCU Bits ==============

NCO1ACC16 = const(0x0000)
NCO1ACC17 = const(0x0001)
NCO1ACC18 = const(0x0002)
NCO1ACC19 = const(0x0003)

# ============== NCO1INCL Bits ==============

NCO1INC0 = const(0x0000)
NCO1INC1 = const(0x0001)
NCO1INC2 = const(0x0002)
NCO1INC3 = const(0x0003)
NCO1INC4 = const(0x0004)
NCO1INC5 = const(0x0005)
NCO1INC6 = const(0x0006)
NCO1INC7 = const(0x0007)

# ============== NCO1INCH Bits ==============

NCO1INC8 = const(0x0000)
NCO1INC9 = const(0x0001)
NCO1INC10 = const(0x0002)
NCO1INC11 = const(0x0003)
NCO1INC12 = const(0x0004)
NCO1INC13 = const(0x0005)
NCO1INC14 = const(0x0006)
NCO1INC15 = const(0x0007)

# ============== NCO1CON Bits ==============

N1PFM = const(0x0000)
N1POL = const(0x0004)
N1OUT = const(0x0005)
N1OE = const(0x0006)
N1EN = const(0x0007)

# ============== NCO1CLK Bits ==============

N1CKS0 = const(0x0000)
N1CKS1 = const(0x0001)
N1PWS0 = const(0x0005)
N1PWS1 = const(0x0006)
N1PWS2 = const(0x0007)

# ============== WDTCON Bits ==============

SWDTEN = const(0x0000)
WDTPS0 = const(0x0001)
WDTPS1 = const(0x0002)
WDTPS2 = const(0x0003)
WDTPS3 = const(0x0004)
WDTPS4 = const(0x0005)

# ============== CLC1CON Bits ==============

LC1MODE0 = const(0x0000)
LC1MODE1 = const(0x0001)
LC1MODE2 = const(0x0002)
LC1INTN = const(0x0003)
LC1INTP = const(0x0004)
LC1OUT = const(0x0005)
LC1OE = const(0x0006)
LC1EN = const(0x0007)
LCMODE0 = const(0x0000)
LCMODE1 = const(0x0001)
LCMODE2 = const(0x0002)
LCINTN = const(0x0003)
LCINTP = const(0x0004)
LCOUT = const(0x0005)
LCOE = const(0x0006)
LCEN = const(0x0007)

# ============== CLC1SEL0 Bits ==============

LC1D1S0 = const(0x0000)
LC1D1S1 = const(0x0001)
LC1D1S2 = const(0x0002)
LC1D2S0 = const(0x0004)
LC1D2S1 = const(0x0005)
LC1D2S2 = const(0x0006)
D1S0 = const(0x0000)
D1S1 = const(0x0001)
D1S2 = const(0x0002)
D2S0 = const(0x0004)
D2S1 = const(0x0005)
D2S2 = const(0x0006)

# ============== CLC1SEL1 Bits ==============

LC1D3S0 = const(0x0000)
LC1D3S1 = const(0x0001)
LC1D3S2 = const(0x0002)
LC1D4S0 = const(0x0004)
LC1D4S1 = const(0x0005)
LC1D4S2 = const(0x0006)
D3S0 = const(0x0000)
D3S1 = const(0x0001)
D3S2 = const(0x0002)
D4S0 = const(0x0004)
D4S1 = const(0x0005)
D4S2 = const(0x0006)

# ============== CLC1POL Bits ==============

LC1G1POL = const(0x0000)
LC1G2POL = const(0x0001)
LC1G3POL = const(0x0002)
LC1G4POL = const(0x0003)
LC1POL = const(0x0007)
G1POL = const(0x0000)
G2POL = const(0x0001)
G3POL = const(0x0002)
G4POL = const(0x0003)
POL = const(0x0007)

# ============== CLC1GLS0 Bits ==============

LC1G1D1N = const(0x0000)
LC1G1D1T = const(0x0001)
LC1G1D2N = const(0x0002)
LC1G1D2T = const(0x0003)
LC1G1D3N = const(0x0004)
LC1G1D3T = const(0x0005)
LC1G1D4N = const(0x0006)
LC1G1D4T = const(0x0007)
D1N = const(0x0000)
D1T = const(0x0001)
D2N = const(0x0002)
D2T = const(0x0003)
D3N = const(0x0004)
D3T = const(0x0005)
D4N = const(0x0006)
D4T = const(0x0007)

# ============== CLC1GLS1 Bits ==============

LC1G2D1N = const(0x0000)
LC1G2D1T = const(0x0001)
LC1G2D2N = const(0x0002)
LC1G2D2T = const(0x0003)
LC1G2D3N = const(0x0004)
LC1G2D3T = const(0x0005)
LC1G2D4N = const(0x0006)
LC1G2D4T = const(0x0007)

# ============== CLC1GLS2 Bits ==============

LC1G3D1N = const(0x0000)
LC1G3D1T = const(0x0001)
LC1G3D2N = const(0x0002)
LC1G3D2T = const(0x0003)
LC1G3D3N = const(0x0004)
LC1G3D3T = const(0x0005)
LC1G3D4N = const(0x0006)
LC1G3D4T = const(0x0007)

# ============== CLC1GLS3 Bits ==============

LC1G4D1N = const(0x0000)
LC1G4D1T = const(0x0001)
LC1G4D2N = const(0x0002)
LC1G4D2T = const(0x0003)
LC1G4D3N = const(0x0004)
LC1G4D3T = const(0x0005)
LC1G4D4N = const(0x0006)
LC1G4D4T = const(0x0007)
G4D1N = const(0x0000)
G4D1T = const(0x0001)
G4D2N = const(0x0002)
G4D2T = const(0x0003)
G4D3N = const(0x0004)
G4D3T = const(0x0005)
G4D4N = const(0x0006)
G4D4T = const(0x0007)

# ============== CWG1CON0 Bits ==============

G1CS0 = const(0x0000)
G1POLA = const(0x0003)
G1POLB = const(0x0004)
G1OEA = const(0x0005)
G1OEB = const(0x0006)
G1EN = const(0x0007)

# ============== CWG1CON1 Bits ==============

G1IS0 = const(0x0000)
G1IS1 = const(0x0001)
G1ASDLA0 = const(0x0004)
G1ASDLA1 = const(0x0005)
G1ASDLB0 = const(0x0006)
G1ASDLB1 = const(0x0007)

# ============== CWG1CON2 Bits ==============

G1ASDSFLT = const(0x0000)
G1ASDSCLC1 = const(0x0001)
G1ARSEN = const(0x0006)
G1ASE = const(0x0007)

# ============== CWG1DBR Bits ==============

CWG1DBR0 = const(0x0000)
CWG1DBR1 = const(0x0001)
CWG1DBR2 = const(0x0002)
CWG1DBR3 = const(0x0003)
CWG1DBR4 = const(0x0004)
CWG1DBR5 = const(0x0005)

# ============== CWG1DBF Bits ==============

CWG1DBF0 = const(0x0000)
CWG1DBF1 = const(0x0001)
CWG1DBF2 = const(0x0002)
CWG1DBF3 = const(0x0003)
CWG1DBF4 = const(0x0004)
CWG1DBF5 = const(0x0005)

# ============== VREGCON Bits ==============

VREGPM0 = const(0x0000)
VREGPM1 = const(0x0001)

# ============== BORCON Bits ==============

BORRDY = const(0x0000)
BORFS = const(0x0006)
SBOREN = const(0x0007)
_CONFIG = const(0x2007)

# ============== CONFIG Options ==============

_FOSC_INTOSC = const(0x3ffe)
_FOSC_EC = const(0x3fff)
_BOREN_OFF = const(0x3ff9)
_BOREN_SBODEN = const(0x3ffb)
_BOREN_NSLEEP = const(0x3ffd)
_BOREN_ON = const(0x3fff)
_WDTE_OFF = const(0x3fe7)
_WDTE_SWDTEN = const(0x3fef)
_WDTE_NSLEEP = const(0x3ff7)
_WDTE_ON = const(0x3fff)
_PWRTE_ON = const(0x3fdf)
_PWRTE_OFF = const(0x3fff)
_MCLRE_OFF = const(0x3fbf)
_MCLRE_ON = const(0x3fff)
_CP_ON = const(0x3f7f)
_CP_OFF = const(0x3fff)
_LVP_OFF = const(0x3eff)
_LVP_ON = const(0x3fff)
_LPBOR_OFF = const(0x3dff)
_LPBOR_ON = const(0x3fff)
_BORV_HI = const(0x3bff)
_BORV_27 = const(0x3bff)
_BORV_LO = const(0x3fff)
_BORV_24 = const(0x3fff)
_WRT_ALL = const(0x27ff)
_WRT_HALF = const(0x2fff)
_WRT_BOOT = const(0x37ff)
_WRT_OFF = const(0x3fff)

# ============== DEVID Equates ==============

_DEVID1 = const(0x2006)

# ============== IDLOC Equates ==============

_IDLOC0 = const(0x2000)
_IDLOC1 = const(0x2001)
_IDLOC2 = const(0x2002)
_IDLOC3 = const(0x2003)
