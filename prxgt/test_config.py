__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest
import os

from prxgt.config import Config


CFG_FILE = '/_test/config.json'


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_all(self):
        path = os.path.dirname(os.path.realpath(__file__))
        file = os.path.realpath(path + CFG_FILE)
        cfg = Config(file)
        cfg.load()
        self.assertEqual(10, cfg.get_dom_attrs_per_instance_max())
        self.assertEqual(2, cfg.get_dom_attrs_per_instance_min())
        self.assertEqual(50, cfg.get_dom_attrs_total())
        self.assertEqual(100, cfg.get_dom_inst_total())
        self.assertEqual(8, cfg.get_oper_filter_attrs_max())
        self.assertEqual(400, cfg.get_oper_filter_count())
        self.assertEqual(500, cfg.get_oper_inst_count())
        pass


if __name__ == '__main__':
    unittest.main()