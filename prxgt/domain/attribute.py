__author__ = 'Alex Gusev <alex@flancer64.com>'
import prxgt.const as const
from prxgt.domain.meta.attribute import Attribute as AttributeBase


class Attribute(AttributeBase):
    """
    This Attribute model contains data.
    """

    def __init__(self, name=None, type_=None, value=None):
        super(Attribute, self).__init__(name, type_)
        self._value = value
        return

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def __repr__(self):
        result = super(Attribute, self).__repr__()
        if (self.value is not None) and (self.type == const.ATTR_TYPE_TXT):
            # [name@type='value']
            result += "=" + repr(self.value[:4] + "...")
        else:
            # [name@text='valu...']
            result += "=" + repr(self.value)
        return result