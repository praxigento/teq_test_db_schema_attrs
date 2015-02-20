__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.domain.meta.attribute import Attribute


class Entity:
    """
    Entity definition. Each entity contains a set of meta attributes (name and type).
    """

    def __init__(self, attrs=None):
        if attrs is None:
            self._attrs = {}
        else:
            self._attrs = attrs
        pass

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, val):
        self._attrs = val

    def add_attr(self, attr: Attribute):
        self._attrs[attr.name] = attr
        pass

    def get_attr(self, attr_name) -> Attribute:
        result = None
        if attr_name in self._attrs:
            result = self.attrs[attr_name]
        return result