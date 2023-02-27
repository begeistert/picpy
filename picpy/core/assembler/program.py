
class AssemblyProgram:
    """ Class to represent an assembly program. """
    def __init__(self, statement):
        self._statements = [statement]

    @property
    def body(self):
        return self._statements

    def __add__(self, statement):
        if statement not in self._statements:
            self._statements.append(statement)
        return self

    def __iadd__(self, statement):
        self._statements.append(statement)
        return self

    def __str__(self):
        return '\n'.join([str(s) for s in self._statements])

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self._statements)

    def __getitem__(self, index):
        return self._statements[index]

    def __setitem__(self, index, value):
        self._statements[index] = value

    def __delitem__(self, index):
        del self._statements[index]

    def __iter__(self):
        return iter(self._statements)

    def __reversed__(self):
        return reversed(self._statements)

    def __contains__(self, item):
        return item in self._statements

