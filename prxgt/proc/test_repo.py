__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from mock import Mock

import prxgt.const as const
from prxgt.domain.attribute import Attribute
from prxgt.proc.repo import RepoProcessor
from prxgt.repo.repository import Repository
from prxgt.domain.instance import Instance

ATTR_NAME = 'a0'
ATTR_VAL = 10


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def _mock_repo(self) -> Repository:
        result = Mock(Repository)
        attr = Attribute()
        attr.name = ATTR_NAME
        attr.type = const.ATTR_TYPE_INT
        attr.value = 10
        inst = Instance()
        inst.add_attr(attr)
        result.instances = {0: inst}
        return result

    def test_add_entity_inst__get_inst_by_id(self):
        proc = RepoProcessor(self._mock_repo())
        attr = Attribute()
        attr.name = ATTR_NAME
        attr.type = const.ATTR_TYPE_INT
        attr.value = 10
        inst = {attr.name: attr}
        # add instance to storage and get by id
        proc.add_instance(inst)
        inst_found = proc.get_inst_by_id(0)
        # @type Attribute
        attr_found = inst_found.get_attr(ATTR_NAME)
        self.assertEqual(attr_found.value, ATTR_VAL)
        pass


if __name__ == '__main__':
    unittest.main()