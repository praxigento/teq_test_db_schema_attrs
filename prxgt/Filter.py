__author__ = 'Alex Gusev <alex@flancer64.com>'
import prxgt.dom.Attribute as Attr


class Filter:
    def __init__(self, attr: Attr.Attribute=None, cond=None, value=None):
        """

        :param attr:
        :param cond:
        :param value:
        :return:
        """
        self.attr = attr
        self.condition = cond
        self.value = value

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