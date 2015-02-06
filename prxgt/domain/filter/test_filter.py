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
    def setUp(self):
        pass

    def test_properties(self):
        filter_ = Filter(None)
        func = Function("eq", 2)
        alias = Alias("customer_id")
        value_ = Value(32)
        rule = FunctionRule(func, alias, value_)
        filter_.rule = rule
        self.assertEqual(rule, filter_.rule)
        pass

    def test_repr(self):
        func = Function("eq", 2)
        alias = Alias("customer_id")
        value_ = Value(32)
        rule = FunctionRule(func, alias, value_)
        filter_ = Filter(rule)
        self.assertEqual("eq:2('customer_id', 32)", repr(filter_))
        pass

    def test_filter_as_function_rule(self):
        """
        "alias = value"
        :return:
        """
        func = Function("eq", 2)
        alias = Alias("customer_id")
        value_ = Value(32)
        rule = FunctionRule(func, alias, value_)
        filter_ = Filter(rule)
        self.assertEqual(rule, filter_.rule)
        pass

    def test_filter_as_condition_rule(self):
        """
        "(total_count > 5) AND (total_count < 25)"
        :return:
        """
        cond_name = "AND"
        alias = Alias("total_count")
        frule1 = FunctionRule(Function("gt", 2), alias, Value(5))
        frule2 = FunctionRule(Function("lt", 2), alias, Value(25))
        filter1 = Filter(frule1)
        filter2 = Filter(frule2)
        crule = ConditionRule(Condition(cond_name), filter1, filter2)
        self.assertEqual(cond_name, crule.condition.name)
        pass


if __name__ == '__main__':
    unittest.main()