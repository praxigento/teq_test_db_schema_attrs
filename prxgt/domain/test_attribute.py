__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest
from prxgt.const import *
from prxgt.domain.attribute import Attribute


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_properties(self):
        name = 'Name'
        type_ = 'Type'
        value = 123
        # constructor with params
        attr = Attribute(name, type_, value)
        self.assertEqual(name, attr.name)
        self.assertEqual(type_, attr.type)
        self.assertEqual(value, attr.value)
        # constructor w/o params
        attr = Attribute()
        attr.name = name
        attr.type = type_
        attr.value = value
        self.assertEqual(name, attr.name)
        self.assertEqual(type_, attr.type)
        self.assertEqual(value, attr.value)
        pass

    def test_repr(self):
        attr = Attribute('name', 'type', 'value')
        self.assertEqual("[name@type='value']", repr(attr))
        attr = Attribute('name', ATTR_TYPE_TXT, 'value')
        self.assertEqual("[name@text='valu...']", repr(attr))
        pass


if __name__ == '__main__':
    unittest.main()