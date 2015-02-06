__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.domain.filter.expression import Expression


class Value(Expression):
    def __init__(self, val):
        self._value = val

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def __repr__(self):
        return repr(self.value)