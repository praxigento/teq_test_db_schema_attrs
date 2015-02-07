__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.domain.filter.filter import Filter
from prxgt.domain.filter.filter_rule import FilterRule
from prxgt.domain.filter.condition import Condition


class ConditionRule(FilterRule):
    """
    ConditionRule представляет собой логическое условие (AND, OR, NOT), применяемое к одному или более фильтров,
    и может быть использовано в качестве части другого ConditionRule.
    """

    def __init__(self, cond: Condition, *parts: Filter):
        self._condition = cond
        self._filters = []
        # TODO we should check parts of the rule - 1 for NOT and > 1 for AND & OR
        for one in parts:
            self._filters.append(one)
        pass

    @property
    def condition(self) -> Condition:
        return self._condition

    @condition.setter
    def condition(self, val: Condition):
        self._condition = val

    @property
    def filters(self):
        return self._filters

    @filters.setter
    def filters(self, val):
        self._filters = val

    def __repr__(self):
        p = ""
        for one in self.filters:
            p += repr(one) + ", "
        return repr(self.condition) + "(" + p[:-2] + ")"