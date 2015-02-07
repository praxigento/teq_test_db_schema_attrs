__author__ = 'Alex Gusev <alex@flancer64.com>'
import prxgt.const as const


class Attribute:
    """
    Attribute definition (name and type).
    """

    def __init__(self, name=None, type_=None):
        self._name = name
        self._type = type_
        return

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, val):
        self._type = val

    def __repr__(self):
        result = "[" + self.name + "@" + self.type + "]"
        return result