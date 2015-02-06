__author__ = 'Alex Gusev <alex@flancer64.com>'
"""
Функция состоит из имени и количества параметров к обработке.
"""


class Function(object):
    def __init__(self, name, args_count):
        self._name = name
        self._args_count = args_count

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def args_count(self):
        return self._args_count

    @args_count.setter
    def args_count(self, val):
        self._args_count = val

    def __repr__(self):
        return str(self.name) + ":" + str(self.args_count)