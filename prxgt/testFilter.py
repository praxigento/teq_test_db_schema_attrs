__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest
from prxgt.Filter import Filter


class TestFilter(unittest.TestCase):
    def setUp(self):
        pass

    def test_all(self):
        filter0 = Filter()
        filter1 = Filter(1)
        filter2 = Filter(1, 2)
        filter3 = Filter(1, 2, 3)
        pass


if __name__ == '__main__':
    unittest.main()