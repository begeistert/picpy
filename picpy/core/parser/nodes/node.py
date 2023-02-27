
class PyNode:
    def __init__(self, line, column):
        self.line = line
        self.column = column
        self._label = None
        self._context = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    def resolve(self):
        raise NotImplementedError()
