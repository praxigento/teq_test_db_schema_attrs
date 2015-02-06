__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from prxgt.domain.filter.value import Value


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        val1 = 32
        value_ = Value(val1)
        self.assertEqual(repr(val1), repr(value_))
        val2 = "string value"
        value_.value = val2
        self.assertEqual(repr(val2), repr(value_))
        pass


if __name__ == '__main__':
    unittest.main()