__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

import prxgt.const as const
from prxgt.domain.meta.attribute import Attribute
from prxgt.domain.meta.entity import Entity


TYPE_DEC = const.ATTR_TYPE_DEC
TYPE_INT = const.ATTR_TYPE_INT
TYPE_STR = const.ATTR_TYPE_STR
TYPE_TXT = const.ATTR_TYPE_TXT


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_properties(self):
        attrs = {'a1': Attribute('a1', TYPE_INT), 'a2': Attribute('a2', TYPE_DEC),
                 'a3': Attribute('a3', TYPE_STR), 'a4': Attribute('a4', TYPE_STR)}
        # constructor w/o params
        inst = Entity()
        self.assertIsNotNone(inst)
        inst.attrs = attrs
        self.assertEqual(attrs, inst.attrs)
        # constructor with params
        inst = Entity(attrs)
        self.assertEqual(attrs, inst.attrs)
        pass

    def test_add_attr(self):
        attr_name = 'a0'
        inst = Entity()
        inst.add_attr(Attribute(attr_name, TYPE_INT))
        attr = inst.get_attr(attr_name)
        self.assertEqual(attr_name, attr.name)
        pass


if __name__ == '__main__':
    unittest.main()