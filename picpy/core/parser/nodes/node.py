
class PyNode:
    def __init__(self, line, column):
        self.line = line
        self.column = column
        self._label = None

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    def resolve(self, context):
        raise NotImplementedError()
