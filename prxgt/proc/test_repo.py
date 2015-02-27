__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from mock import Mock

import prxgt.const as const
from prxgt.domain.attribute import Attribute
from prxgt.proc.repo import RepoProcessor
from prxgt.repo.repository import Repository
from prxgt.domain.instance import Instance
from prxgt.domain.filter.value import Value
from prxgt.domain.filter.alias import Alias
from prxgt.domain.filter.filter import Filter
from prxgt.domain.filter.function import Function
from prxgt.domain.filter.function_rule import FunctionRule

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
        inst.id = 0
        inst.add_attr(attr)
        result.instances = {0: inst}
        return result

    def test_add_entity_inst__get_inst_by_id(self):
        proc = RepoProcessor(self._mock_repo())
        attr = Attribute()
        attr.name = ATTR_NAME
        attr.type = const.ATTR_TYPE_INT
        attr.value = 10
        inst = Instance()
        inst.add_attr(attr)
        # add instance to storage and get by id
        proc.add_instance(inst)
        inst_found = proc.get_inst_by_id(0)
        # @type Attribute
        attr_found = inst_found.get_attr(ATTR_NAME)
        self.assertEqual(attr_found.value, ATTR_VAL)
        pass

    def test_get_list_by_filter(self):
        # prepare test data and mocks
        proc = RepoProcessor(self._mock_repo())
        rule = FunctionRule(Function("eq"), Alias("id"), Value(0))
        filter_eq = Filter(rule)
        rule = FunctionRule(Function("gt"), Alias("id"), Value(4))
        filter_gt = Filter(rule)
        # get instance by filter "id=0"
        filtered = proc.get_list_by_filter(filter_eq)
        self.assertEqual(1, len(filtered))
        # get instance by filter "id>4"
        filtered = proc.get_list_by_filter(filter_gt)
        self.assertEqual(0, len(filtered))
        pass


if __name__ == '__main__':
    unittest.main()