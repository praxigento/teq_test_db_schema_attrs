__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest

from prxgt.repo.repository import Repository


class Test(unittest.TestCase):
    def setUp(self):
        return

    def test_init(self):
        repo = Repository(10)
        self.assertIsNotNone(repo)
        return

    def test_get_attr_names(self):
        repo = Repository(10)
        names = repo.get_attr_names()
        self.assertTrue(isinstance(names, list))
        self.assertEqual(10, len(names))
        return

    def test_get_attr_names(self):
        repo = Repository(1)
        attr = repo.get_attr_by_name("a0")
        self.assertEqual("a0", attr.name)
        return


if __name__ == '__main__':
    unittest.main()