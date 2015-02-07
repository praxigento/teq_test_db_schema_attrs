__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest
from prxgt.const import *
from prxgt.domain.meta.attribute import Attribute


class Test(unittest.TestCase):
    def test_properties(self):
        name = 'Name'
        type_ = 'Type'
        # constructor with params
        attr = Attribute(name, type_)
        self.assertEqual(name, attr.name)
        self.assertEqual(type_, attr.type)
        # constructor w/o params
        attr = Attribute()
        attr.name = name
        attr.type = type_
        self.assertEqual(name, attr.name)
        self.assertEqual(type_, attr.type)
        return

    def test_repr(self):
        attr = Attribute('name', 'type')
        self.assertEqual("[name@type]", repr(attr))
        return


if __name__ == '__main__':
    unittest.main()