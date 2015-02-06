__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from prxgt.domain.filter.condition import Condition


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        name = "AND"
        cond = Condition(name)
        self.assertEqual(name, cond.name)
        cond.name = "OR"
        self.assertEqual("OR", cond.name)
        pass

    def test_repr(self):
        name = "AND"
        cond = Condition(name)
        self.assertEqual(repr(name), repr(cond))
        pass


if __name__ == '__main__':
    unittest.main()