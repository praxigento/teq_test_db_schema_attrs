__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from prxgt.domain.filter.alias import Alias
from prxgt.domain.filter.filter import Filter
from prxgt.domain.filter.function import Function
from prxgt.domain.filter.function_rule import FunctionRule
from prxgt.domain.filter.value import Value
from prxgt.domain.instance import Instance
from prxgt.proc.filtrator import Filtrator
from prxgt.domain.attribute import Attribute
from prxgt.const import *


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        # tests
        filtrator = Filtrator()
        self.assertIsNotNone(filtrator)
        return

    def test_is_applied_simple(self):
        t_value = 32
        t_compare = 'eq'
        t_alias = 'customer_id'
        # create instance
        inst = Instance()
        inst.add_attr(Attribute(t_alias, ATTR_TYPE_STR, t_value))
        # create filter
        func = Function(t_compare)
        alias = Alias(t_alias)
        value_ = Value(t_value)
        rule = FunctionRule(func, alias, value_)
        filter_ = Filter(rule)
        # tests
        filtrator = Filtrator()
        self.assertIsNotNone(filtrator)
        is_applied = filtrator.is_applied(filter_, inst)
        self.assertTrue(is_applied)
        return

    def test__compare_int(self):
        # tests
        # eq
        self.assertFalse(Filtrator._compare('eq', 1, 2))
        self.assertTrue(Filtrator._compare('eq', 1, 1))
        self.assertFalse(Filtrator._compare('eq', 2, 1))
        # gt
        self.assertFalse(Filtrator._compare('gt', 1, 2))
        self.assertFalse(Filtrator._compare('gt', 1, 1))
        self.assertTrue(Filtrator._compare('gt', 2, 1))
        # gte
        self.assertFalse(Filtrator._compare('gte', 1, 2))
        self.assertTrue(Filtrator._compare('gte', 1, 1))
        self.assertTrue(Filtrator._compare('gte', 2, 1))
        # lt
        self.assertTrue(Filtrator._compare('lt', 1, 2))
        self.assertFalse(Filtrator._compare('lt', 1, 1))
        self.assertFalse(Filtrator._compare('lt', 2, 1))
        # lte
        self.assertTrue(Filtrator._compare('lte', 1, 2))
        self.assertTrue(Filtrator._compare('lte', 1, 1))
        self.assertFalse(Filtrator._compare('lte', 2, 1))
        pass

    def test__compare_str(self):
        # tests
        filtrator = Filtrator()
        self.assertIsNotNone(filtrator)
        # eq
        self.assertFalse(Filtrator._compare('eq', 'a', 'b'))
        self.assertTrue(Filtrator._compare('eq', 'a', 'a'))
        self.assertFalse(Filtrator._compare('eq', 'b', 'a'))
        # gt
        self.assertFalse(Filtrator._compare('gt', 'a', 'b'))
        self.assertFalse(Filtrator._compare('gt', 'a', 'a'))
        self.assertTrue(Filtrator._compare('gt', 'b', 'a'))
        # gte
        self.assertFalse(Filtrator._compare('gte', 'a', 'b'))
        self.assertTrue(Filtrator._compare('gte', 'a', 'a'))
        self.assertTrue(Filtrator._compare('gte', 'b', 'a'))
        # lt
        self.assertTrue(Filtrator._compare('lt', 'a', 'b'))
        self.assertFalse(Filtrator._compare('lt', 'a', 'a'))
        self.assertFalse(Filtrator._compare('lt', 'b', 'a'))
        # lte
        self.assertTrue(Filtrator._compare('lte', 'a', 'b'))
        self.assertTrue(Filtrator._compare('lte', 'a', 'a'))
        self.assertFalse(Filtrator._compare('lte', 'b', 'a'))
        pass

    def test__extract_value(self):
        # prepare test data
        t_value = 'any value here'
        t_value_alias = 'any alias value here'
        t_name_alias = 'alias name'
        value = Value(t_value)
        alias = Alias(t_name_alias)
        instance = Instance()
        instance.id = 5
        attr = Attribute(t_name_alias, ATTR_TYPE_STR, t_value_alias)
        instance.add_attr(attr)
        # test value
        res = Filtrator._extract_value(value, instance)
        self.assertEqual(t_value, res)
        # test existed alias
        res = Filtrator._extract_value(alias, instance)
        self.assertEqual(t_value_alias, res)
        # test not existed alias
        alias = Alias(t_name_alias + 'missed')
        res = Filtrator._extract_value(alias, instance)
        self.assertIsNone(res)
        pass


if __name__ == '__main__':
    unittest.main()
