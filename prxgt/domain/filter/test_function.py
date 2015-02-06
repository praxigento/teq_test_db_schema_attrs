__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from prxgt.const import *
from prxgt.domain.filter.expression import Expression
from prxgt.domain.filter.filter import Filter
from prxgt.domain.filter.function import Function
from prxgt.domain.filter.function_rule import FunctionRule


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        name_ = "eq"
        args = 2
        func_ = Function(name_, args)
        self.assertEqual("eq:2", repr(func_))
        pass

    def test_properties(self):
        func_ = Function("max", 5)
        name_ = "eq"
        args = 2
        func_.name = name_
        func_.args_count = args
        self.assertEqual(name_, func_.name)
        self.assertEqual(args, func_.args_count)
        pass


if __name__ == '__main__':
    unittest.main()