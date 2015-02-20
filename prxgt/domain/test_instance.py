__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from prxgt.const import *

from prxgt.domain.attribute import Attribute
from prxgt.domain.instance import Instance, ATTR_ID_NAME

INST_ID = 5


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_properties(self):
        id_ = 4
        attrs = {'a1': Attribute('a1', ATTR_TYPE_INT, 23), 'a2': Attribute('a2', ATTR_TYPE_DEC, 2.3),
                 'a3': Attribute('a3', ATTR_TYPE_STR, 'string')}
        # constructor w/o params
        inst = Instance()
        self.assertIsNotNone(inst)
        self.assertIsNone(inst.id)
        inst.id = id_
        self.assertEqual(id_, inst.id)
        inst.attrs = attrs
        self.assertEqual(attrs, inst.attrs)
        # constructor with params
        inst = Instance(id_, attrs)
        self.assertEqual(id_, inst.id)
        self.assertEqual(attrs, inst.attrs)
        pass

    def test_id(self):
        """
        New attribute named "id" should be created
        :return:
        """
        inst = Instance()
        inst.id = INST_ID
        self.assertIsNotNone(inst.get_attr(ATTR_ID_NAME))
        attr = inst.get_attr(ATTR_ID_NAME)
        assert isinstance(attr, Attribute)
        self.assertEqual(ATTR_ID_NAME, attr.name)
        self.assertEqual(ATTR_TYPE_INT, attr.type)
        self.assertEqual(INST_ID, attr.value)
        return

    def test_add_attr(self):
        attr_name = 'a0'
        attr_value = 21
        inst = Instance()
        inst.add_attr(Attribute(attr_name, ATTR_TYPE_INT, attr_value))
        attr = inst.get_attr(attr_name)
        self.assertEqual(attr_name, attr.name)
        pass


if __name__ == '__main__':
    unittest.main()