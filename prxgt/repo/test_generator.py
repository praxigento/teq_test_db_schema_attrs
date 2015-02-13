__author__ = 'Alex Gusev <alex@flancer64.com>'
import unittest
import prxgt.const  as const
from prxgt.repo.generator import Generator


class Test(unittest.TestCase):
    def test_init(self):
        # tests
        gene = Generator()
        self.assertIsNotNone(gene)
        return

    def test_get_value(self):
        # tests simple generators.
        gene = Generator()
        self.assertIsNotNone(gene)
        value = gene.get_value(const.ATTR_TYPE_DEC)
        self.assertTrue(isinstance(value, float))
        value = gene.get_value(const.ATTR_TYPE_INT)
        self.assertTrue(isinstance(value, int))
        value = gene.get_value(const.ATTR_TYPE_STR)
        self.assertTrue(isinstance(value, str))
        self.assertTrue(len(value) == 8)
        value = gene.get_value(const.ATTR_TYPE_TXT)
        self.assertTrue(isinstance(value, str))
        self.assertTrue(len(value) == 512)
        return

    def test_set_for_type(self):
        # tests custom generator for some type.
        gene = Generator()
        self.assertIsNotNone(gene)
        value = gene.get_value(const.ATTR_TYPE_STR)
        self.assertTrue(isinstance(value, str))
        self.assertTrue(len(value) == 8)
        gene.set_for_type(const.ATTR_TYPE_STR, custom_generator)
        value = gene.get_value(const.ATTR_TYPE_STR)
        self.assertTrue(isinstance(value, int))
        self.assertTrue(value == 5)


def custom_generator(self):
    result = 5
    return result


if __name__ == '__main__':
    unittest.main()