from picpy.core.jit.backend.model import AbstractCPU


class CPUInfo(object):
    enhanced = False
    arch_version = 14


class AbstractPIC14CPU(AbstractCPU):
    def __init__(self):
        self.cpu_info = CPUInfo()


class CPU_PIC14(AbstractPIC14CPU):
    """PIC14"""
    backend_name = 'pic14'
