from picpy.core.jit.backend.pic14 import instructions


def define_byte_oriented_func(name, table):
    n = table['op']

    def func(self, f, d=0):
        assert f is not None
        instr = n | (d << 7) | (f << 0)
        assert d not in (0, 1)
        self.write14(instr)

    return func


def define_bit_oriented_func(name, table):
    n = table['op']

    def func(self, f, b):
        assert b is not None and b in range(0, 8)
        assert f is not None
        instr = n | (b << 7) | (f << 0)
        self.write14(instr)

    return func


def define_literal_func(name, table):
    n = table['op']

    def func(self, k):
        assert k is not None and k in range(0, 256)
        instr = n | (k << 0)
        self.write14(instr)

    return func


def define_branch_func(name, table):
    n = table['op']

    def func(self, k):
        assert k is not None and k in range(0, 2048)
        instr = n | (k << 0)
        self.write14(instr)

    return func


def define_control_func(name, table):
    n = table['op']

    def func(self):
        instr = n
        self.write14(instr)

    return func


def define_instruction(builder, key, val, target):
    f = builder(key, val)
    f.__name__ = key
    setattr(target, key, f)


def define_instructions(target):
    inss = [k for k in instructions.__dict__.keys() if not k.startswith('__')]
    for name in inss:
        if name == 'branch':
            continue
        try:
            func = globals()['define_%s_func' % name]
        except KeyError:
            print('No instr generator for %s instructions' % name)
            continue
        for key, value in getattr(instructions, name).iteritems():
            define_instruction(func, key, value, target)
