__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from prxgt.const import *
from prxgt.domain.attribute import Attribute
from prxgt.domain.filter import Filter


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_properties(self):
        attr0 = Attribute('a0', ATTR_TYPE_INT)
        attr1 = Attribute('a1', ATTR_TYPE_DEC)
        # constructor with params
        filter_ = Filter(attr0, COND_EQ, 21)
        self.assertEqual(attr0, filter_.attr)
        self.assertEqual(COND_EQ, filter_.condition)
        self.assertEqual(21, filter_.value)
        # accessors
        filter_.attr = attr1
        filter_.condition = COND_GT
        filter_.value = 2.34
        self.assertEqual(attr1, filter_.attr)
        self.assertEqual(COND_GT, filter_.condition)
        self.assertEqual(2.34, filter_.value)
        pass


if __name__ == '__main__':
    unittest.main()