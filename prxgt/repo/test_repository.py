__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest
import os

from mock import Mock

from prxgt.config import Config
from prxgt.repo.repository import Repository


class Test(unittest.TestCase):
    def setUp(self):
        return

    def _mock_config(self) -> Config:
        result = Mock(Config())
        result.get_dom_attrs_total = Mock(return_value=10)
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
        repo.save(fullpath)
        repo.load(fullpath)
        after = repo._instances[0]
        for attr_name in before:
            self.assertEqual(before[attr_name].value, after[attr_name].value)
        return

    def test_get_attr_names(self):
        # prepare data
        config = self._mock_config()
        # tests
        repo = Repository(config)
        repo._init_attrs()
        names = repo.get_attr_names()
        self.assertTrue(isinstance(names, list))
        self.assertEqual(10, len(names))
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


if __name__ == '__main__':
    unittest.main()