__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest
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

    def test_get_attr_names(self):
        # prepare data
        config = self._mock_config()
        # tests
        repo = Repository(config)
        names = repo.get_attr_names()
        self.assertTrue(isinstance(names, list))
        self.assertEqual(10, len(names))
        return

    def test_get_attr_names(self):
        # prepare data
        config = self._mock_config()
        # tests
        repo = Repository(config)
        attr = repo.get_attr_by_name("a0")
        self.assertEqual("a0", attr.name)
        return


if __name__ == '__main__':
    unittest.main()