__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest
from prxgt.const import *
from prxgt.domain.attribute import Attribute
from prxgt.domain.entity import Entity


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_properties(self):
        id_ = 4
        inst = Entity()
        self.assertIsNotNone(inst)
        self.assertIsNone(inst.id)
        inst.id = id_
        self.assertEqual(id_, inst.id)
        attrs = {'a1': Attribute('a1', ATTR_TYPE_INT, 23), 'a2': Attribute('a2', ATTR_TYPE_DEC, 2.3),
                 'a3': Attribute('a3', ATTR_TYPE_STR, 'string')}
        inst.attrs = attrs
        self.assertEqual(attrs, inst.attrs)
        pass

    def test_add_attr(self):
        attr_name = 'a0'
        attr_value = 21
        inst = Entity()
        inst.add_attr(Attribute(attr_name, ATTR_TYPE_INT, attr_value))
        attr = inst.get_attr(attr_name)
        self.assertEqual(attr_name, attr.name)
        pass


if __name__ == '__main__':
    unittest.main()