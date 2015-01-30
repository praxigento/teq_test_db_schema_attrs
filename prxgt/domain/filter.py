__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.domain.attribute import Attribute


class Filter:
    """
    Filter contains a set of the conditions.
    """

    def __init__(self, attr: Attribute, condition, value):
        self._attr = attr
        self._condition = condition
        self._value = value

    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, val: Attribute):
        self._attr = val

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, val):
        self._condition = val