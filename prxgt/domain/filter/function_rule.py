__author__ = 'Alex Gusev <alex@flancer64.com>'

from prxgt.domain.filter.filter_rule import FilterRule
from prxgt.domain.filter.function import Function
from prxgt.domain.filter.expression import Expression


class FunctionRule(Expression, FilterRule):
    """
    FunctionRule представляет собой функцию с некоторым набором параметров, возвращающую True или False и может быть
    использована в качестве FilterRule или части другой FunctionRule
    """

    def __init__(self, func: Function, *parameters: Expression):
        self._func = func
        self._params = []
        # TODO we should check parts of the rule - 1 for NOT and > 1 for AND & OR
        for one in parameters:
            self._params.append(one)
        pass

    @property
    def func(self) -> Function:
        return self._func

    @func.setter
    def func(self, val: Function):
        self._func = val

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, val):
        self._params = val

    def __repr__(self):
        p = ""
        for one in self.params:
            p += repr(one) + ", "
        return repr(self.func) + "(" + p[:-2] + ")"