__author__ = 'Alex Gusev <alex@flancer64.com>'
import logging
import random

import prxgt.const as const
from prxgt.config import Config
from prxgt.domain.attribute import Attribute


class Repository(object):
    """
    Repository contains meta data for domain (attribute names, types and values) and data itself. Repository data is
    used to create test queries. Repository can be saved to file or loaded from file.
    """

    def __init__(self, config: Config):
        """Registry for all available attributes (name and type)."""
        self._attrs_available = {}
        self._types = {0: const.ATTR_TYPE_INT, 1: const.ATTR_TYPE_DEC, 2: const.ATTR_TYPE_STR, 3: const.ATTR_TYPE_TXT}
        self._init_attrs(config.get_dom_attrs_total())

    def _init_attrs(self, attrs_total):
        """
        Initialize attributes names and types.
        :return:
        """
        logging.info("init available attributes registry;")
        for i in range(attrs_total):
            name = "a" + repr(i)
            type_ = self._get_random_type()
            attr = Attribute()
            attr.name = name
            attr.type = type_
            self._attrs_available[name] = attr
        return

    def _get_random_type(self):
        """
        Return random attribute type.
        :return:
        """
        ndx = random.randint(0, 3)
        result = self._types.get(ndx)
        return result

    def get_attr_by_name(self, name) -> Attribute:
        result = self._attrs_available[name]
        return result

    def get_attr_names(self):
        result = list(self._attrs_available.keys())
        return result