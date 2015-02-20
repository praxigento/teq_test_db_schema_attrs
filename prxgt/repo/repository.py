__author__ = 'Alex Gusev <alex@flancer64.com>'
import logging
import random
import json

import prxgt.const as const
from prxgt.config import Config
from prxgt.domain.attribute import Attribute
from prxgt.repo.generator import Generator
from prxgt.domain.instance import Instance


TYPE_DEC = const.ATTR_TYPE_DEC
TYPE_INT = const.ATTR_TYPE_INT
TYPE_STR = const.ATTR_TYPE_STR
TYPE_TXT = const.ATTR_TYPE_TXT

JSON_META = 'meta'
JSON_DATA = 'data'
JSON_TYPE = 'type'


class Repository(object):
    """
    Repository contains meta data for domain (attribute names, types and values) and data itself. Repository data is
    used to create test queries. Repository can be saved to file or loaded from file.
    """

    def __init__(self, config: Config):
        """

        :param config:
        :return:
        """

        self._config = config
        """ Save application configuration """

        self._generator = Generator()

        self._attrs_available = {}
        """ Registry for all available attributes (name and type). """

        self._attrs_used = {}
        """ Registry for all attributes used in instances (name and type). """

        self._instances = {}
        """ Registry for the generated or loaded instances """

        self._types = {0: TYPE_DEC, 1: TYPE_INT, 2: TYPE_STR, 3: TYPE_TXT}
        """ Available types """

    def init_all(self):
        self._init_attrs()
        self._init_instances()

    def add_instance(self, inst: Instance):
        for attr_name in inst.attrs:
            attr = inst.get_attr(attr_name)
            if attr_name not in self._attrs_available:
                self._attrs_available[attr_name] = attr
            if attr_name not in self._attrs_used:
                self._attrs_used[attr_name] = attr
        self._instances[inst.id] = inst

    def _init_attrs(self):
        """
        Initialize attributes names and types.
        :return:
        """
        logging.info("init available attributes registry;")
        total = self._config.get_dom_attrs_total()
        for i in range(total):
            name = "a" + repr(i)
            type_ = self._get_random_type()
            attr = Attribute()
            attr.name = name
            attr.type = type_
            self._attrs_available[name] = attr
        return

    def _init_instances(self):
        total = self._config.get_dom_inst_total()
        attrs_min = self._config.get_dom_attrs_per_instance_min()
        attrs_max = self._config.get_dom_attrs_per_instance_max()
        attrs_total = self._config.get_dom_attrs_total()
        attr_names = list(self._attrs_available.keys())
        for i in range(total):
            inst = Instance()
            # get number of the attributes for current instance
            attrs_num = random.randint(attrs_min, attrs_max)
            for j in range(attrs_num):
                # get random attribute and generate value for the instance
                attr_ndx = random.randint(0, attrs_total - 1)
                attr_name = attr_names[attr_ndx]
                attr_selected = self.get_attr_by_name(
                    attr_name)  # @type Attribute
                assert isinstance(attr_selected, Attribute)
                self._attrs_used[attr_name] = attr_selected
                attr = Attribute()
                attr.name = attr_selected.name
                attr.type = attr_selected.type
                attr.value = self._generator.get_value(attr_selected.type)
                inst.add_attr(attr)
            inst.id = i
            self._instances[i] = inst
        logging.info("\ttotal %i instances are created, %i different attributes are used;", total,
                     len(self._attrs_used))
        return

    def save(self, filename: str):
        obj = {JSON_META: {}, JSON_DATA: {}}
        # parse meta data (attributes)
        for key in self._attrs_available:
            attr = self._attrs_available[key]
            assert isinstance(attr, Attribute)
            obj[JSON_META][attr.name] = {JSON_TYPE: attr.type}
        # get all instances by id and save it into dictionary to convert to JSON
        for key in self._instances:
            one = self._instances[key]
            assert isinstance(one, Instance)
            inst = {}
            for attr_name in one.attrs:
                inst_attr = one.get_attr(attr_name)
                assert isinstance(inst_attr, Attribute)
                inst[attr_name] = inst_attr.value
            obj[JSON_DATA][key] = inst
        # save data to JSON file
        with open(filename, 'w') as output:
            json.dump(obj, output)
        return

    def load(self, filename: str):
        file = open(filename)
        loaded = json.load(file)
        meta = loaded[JSON_META]
        data = loaded[JSON_DATA]
        # reset repository registries
        self._attrs_available = {}
        self._attrs_used = {}
        self._instances = {}
        # load meta
        for attr_name in meta:
            attr = Attribute()
            attr.name = attr_name
            attr.type = meta[attr_name][JSON_TYPE]
            self._attrs_available[attr_name] = attr
            self._attrs_used[attr_name] = attr
        # load instances data
        for id_ in data:
            inst_loaded = data[id_]
            inst = Instance()
            for attr_name in inst_loaded:
                attr_meta = self._attrs_available[attr_name]
                assert isinstance(attr_meta, Attribute)
                attr = Attribute()
                attr.name = attr_name
                attr.type = attr_meta.type
                attr.value = inst_loaded[attr_name]
                inst.add_attr(attr)
            inst.id = id_
            self._instances[int(id_)] = inst
        return

    @property
    def instances(self):
        """
        Return all instances from repo (dictionary: id => instance)
        :return:
        """
        return self._instances

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
