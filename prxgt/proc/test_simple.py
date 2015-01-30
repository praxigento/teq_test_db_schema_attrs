from prxgt.proc import simple

__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest
import prxgt.const as const
from prxgt.domain.attribute import Attribute
from prxgt.proc.simple import ProcessorSimple


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_entity_inst__get_inst_by_id(self):
        ATTR_NAME = 'a0'
        ATTR_VAL = 10
        proc = ProcessorSimple()
        attr = Attribute()
        attr.name = ATTR_NAME
        attr.type = const.ATTR_TYPE_INT
        attr.value = 10
        inst = {attr.name: attr}
        # add instance to storage and get by id
        proc.add_entity_inst(inst)
        inst_found = proc.get_inst_by_id(0)
        # @type Attribute
        attr_found = inst_found[ATTR_NAME]
        self.assertEqual(attr_found.value, ATTR_VAL)
        pass


if __name__ == '__main__':
    unittest.main()