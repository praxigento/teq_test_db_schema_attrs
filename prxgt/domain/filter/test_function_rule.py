__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from prxgt.domain.filter.expression import Expression
from prxgt.domain.filter.function import Function
from prxgt.domain.filter.function_rule import FunctionRule


class Test(unittest.TestCase):
    def test_init(self):
        func_ = Function("eq", 2)
        exp1 = Expression()
        exp2 = Expression()
        frule = FunctionRule(func_, exp1, exp2)
        self.assertEqual(func_, frule.func)
        pass

    def test_properties(self):
        frule = FunctionRule(None, None)
        func_ = Function("eq", 2)
        exp1 = Expression()
        exp2 = Expression()
        tup = (exp1, exp2)
        frule.func = func_
        frule.params = tup
        self.assertEqual(func_, frule.func)
        self.assertEqual(tup, frule.params)
        pass

    def test_params(self):
        """
        Test method to investigate function parameters variations.
        :return:
        """
        fname = Function("eq", 2)
        exp1 = Expression()
        exp2 = Expression()
        tup = (exp1, exp2, fname)
        FunctionRule(fname, tup)
        FunctionRule(fname, exp1, exp2, fname)
        pass


if __name__ == '__main__':
    unittest.main()