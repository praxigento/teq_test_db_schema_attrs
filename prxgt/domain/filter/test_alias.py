__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from prxgt.domain.filter.alias import Alias


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        name = "customer_id"
        alias = Alias(name)
        self.assertEqual(repr(name), repr(alias))
        name2 = "order_id"
        alias.name = name2
        self.assertEqual(repr(name2), repr(alias))
        pass


if __name__ == '__main__':
    unittest.main()