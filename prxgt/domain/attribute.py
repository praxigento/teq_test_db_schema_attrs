__author__ = 'Alex Gusev <alex@flancer64.com>'
import prxgt.const as const


class Attribute:
    """
    In-memory model for one attribute
    """

    def __init__(self, name=None, type_=None, value=None):
        self._name = name
        self._type = type_
        self._value = value
        pass

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

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def __repr__(self):
        result = "[" + self.name + "@" + self.type
        if (self.value is not None) and (self.type == const.ATTR_TYPE_TXT):
            # [name@type='value']
            result += "=" + repr(self.value[:4] + "...")
        else:
            # [name@text='valu...']
            result += "=" + repr(self.value)
        result += "]"
        return result