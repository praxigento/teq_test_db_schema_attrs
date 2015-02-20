__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.domain.attribute import Attribute
from prxgt.domain.meta.entity import Entity


class Instance(Entity):
    """
    Entity instance representation.
    """

    def __init__(self, id_=None, attrs=None):
        self._id = id_
        if attrs is None:
            self._attrs = {}
        else:
            self._attrs = attrs
        pass

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        self._id = val

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, val):
        self._attrs = val

    def add_attr(self, attr: Attribute):
        """
        askldj alsdkasj dlas
        """
        self._attrs[attr.name] = attr
        pass

    def get_attr(self, attr_name) -> Attribute:
        result = None
        if attr_name in self._attrs:
            result = self.attrs[attr_name]
        return result