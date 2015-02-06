__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from prxgt.domain.filter.alias import Alias
from prxgt.domain.filter.condition import Condition
from prxgt.domain.filter.condition_rule import ConditionRule
from prxgt.domain.filter.filter import Filter
from prxgt.domain.filter.function import Function
from prxgt.domain.filter.function_rule import FunctionRule
from prxgt.domain.filter.value import Value


class Test(unittest.TestCase):
    def test_init(self):
        and_ = "AND"
        cond = Condition(and_)
        frule = FunctionRule(Function("gt", 2), Alias("customer_id"), Value(5))
        filter1 = Filter(frule)
        filter2 = Filter(frule)
        crule = ConditionRule(cond, filter1, filter2)
        self.assertEqual(cond, crule.condition)
        pass

    def test_properties(self):
        and_ = "AND"
        or_ = "OR"
        cond1 = Condition(and_)
        frule = FunctionRule(Function("gt", 2), Alias("customer_id"), Value(5))
        filter1 = Filter(frule)
        filter2 = Filter(frule)
        crule = ConditionRule(cond1, filter1, filter2)
        self.assertEqual(cond1, crule.condition)
        cond2 = Condition(or_)
        crule.condition = cond2
        self.assertEqual(cond2, crule.condition)
        filters = (filter2, filter1)
        crule.filters = filters
        self.assertEqual(filters, crule.filters)
        pass


    def test_repr(self):
        and_ = "AND"
        cond = Condition(and_)
        frule1 = FunctionRule(Function("gt", 2), Alias("customer_id"), Value(5))
        frule2 = FunctionRule(Function("lt", 2), Alias("customer_id"), Value(25))
        filter1 = Filter(frule1)
        filter2 = Filter(frule2)
        crule = ConditionRule(cond, filter1, filter2)
        self.assertEqual("'AND'(gt:2('customer_id', 5), lt:2('customer_id', 25))", repr(crule))
        pass


if __name__ == '__main__':
    unittest.main()