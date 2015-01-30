__author__ = 'Alex Gusev <alex@flancer64.com>'
import prxgt.domain.attribute as Attr


class Filter:
    def __init__(self, attr: Attr.Attribute=None, cond=None, value=None):
        """

        :param attr:
        :param cond:
        :param value:
        :return:
        """
        self._attr = attr
        self._condition = cond
        self._value = value

    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, val):
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