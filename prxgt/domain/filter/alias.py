__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.domain.filter.expression import Expression


class Alias(Expression):
    """
    Alias is representation of the attribute or select function (SELECT MIN(entity_id) AS min_id FROM ...)
    """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    def __repr__(self):
        return repr(self.name)