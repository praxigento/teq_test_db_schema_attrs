__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest
import os

from mock import Mock

from prxgt.config import Config
from prxgt.repo.repository import Repository
from prxgt.domain.instance import Instance
from prxgt.domain.attribute import Attribute


ATTR_NAME = "a0"
INST_ID = 0
ATTR_TYPE = "som type"
ATTR_VALUE = "some value"

_TEST_CONFIG_ATTRS_TOTAL = 10


class Test(unittest.TestCase):
    def setUp(self):
        return

    def _mock_config(self) -> Config:
        result = Mock(Config())
        result.get_dom_attrs_total = Mock(return_value=_TEST_CONFIG_ATTRS_TOTAL)
        result.get_dom_attrs_per_instance_min = Mock(return_value=3)
        result.get_dom_attrs_per_instance_max = Mock(return_value=5)
        result.get_dom_inst_total = Mock(return_value=50)
        return result

    def test_init(self):
        # prepare data
        config = self._mock_config()
        # tests
        repo = Repository(config)
        self.assertIsNotNone(repo)
        return

    def test_init_all(self):
        # prepare data
        config = self._mock_config()
        # tests
        repo = Repository(config)
        repo.init_all()
        self.assertTrue(isinstance(repo._instances, dict))
        self.assertEqual(50, len(repo._instances))
        return

    def test_save_load(self):
        filename = '../_test/tmp/repository.json'
        dirname = os.path.dirname(os.path.abspath(__file__))
        fullpath = dirname + '/' + filename
        # prepare data
        config = self._mock_config()
        # tests
        repo = Repository(config)
        repo.init_all()
        before = repo._instances[0]
        assert isinstance(before, Instance)
        repo.save(fullpath)
        repo.load(fullpath)
        after = repo._instances[0]
        assert isinstance(after, Instance)
        for attr_name in before.attrs:
            self.assertEqual(before.get_attr(attr_name).value, after.get_attr(attr_name).value)
        return

    def test_get_attr_names(self):
        # prepare data
        config = self._mock_config()
        # tests
        repo = Repository(config)
        repo._init_attrs()
        names = repo.get_attr_names()
        self.assertTrue(isinstance(names, list))
        self.assertEqual(_TEST_CONFIG_ATTRS_TOTAL + 1, len(names))  # + "id" attribute
        return

    def test_get_attr_by_name(self):
        # prepare data
        config = self._mock_config()
        # tests
        repo = Repository(config)
        repo._init_attrs()
        attr = repo.get_attr_by_name("a0")
        self.assertEqual("a0", attr.name)
        return

    def test_add_instance(self):
        # prepare data
        config = self._mock_config()
        attr = Attribute()
        attr.name = ATTR_NAME
        attr.type = ATTR_TYPE
        attr.value = ATTR_VALUE
        inst = Instance()
        inst.add_attr(attr)
        # tests
        repo = Repository(config)
        repo.add_instance(inst)
        all_ = repo.instances
        self.assertTrue(isinstance(all_, dict))
        test_inst = all_[INST_ID]
        assert isinstance(test_inst, Instance)
        self.assertEqual(INST_ID, test_inst.id)
        test_attr = test_inst.get_attr(ATTR_NAME)
        assert isinstance(test_attr, Attribute)
        self.assertEqual(ATTR_NAME, test_attr.name)
        self.assertEqual(ATTR_TYPE, test_attr.type)
        self.assertEqual(ATTR_VALUE, test_attr.value)
        return


if __name__ == '__main__':
    unittest.main()