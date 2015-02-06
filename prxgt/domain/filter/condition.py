__author__ = 'Alex Gusev <alex@flancer64.com>'
"""
Filter condition (in WHERE clause) - AND, OR, NOT
"""


class Condition(object):
    """
    Representation of the boolean condition - AND, OR, NOT, ...
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