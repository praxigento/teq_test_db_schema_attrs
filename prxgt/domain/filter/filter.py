__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.domain.filter.filter_rule import FilterRule


class Filter:
    """
    Top level representation of the filter structure. Filter can contain simple FunctionRule ("customer_id = 23")
    or can contain a complex ConditionRule.
    """

    def __init__(self, rule: FilterRule):
        self._rule = rule
        pass

    @property
    def rule(self) -> FilterRule:
        return self._rule

    @rule.setter
    def rule(self, val: FilterRule):
        self._rule = val

    def __repr__(self):
        return repr(self._rule)