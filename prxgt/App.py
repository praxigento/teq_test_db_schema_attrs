__author__ = 'Alex Gusev <alex@flancer64.com>'
import logging
from random import randint

from prxgt.dom.Attribute import Attribute
from prxgt.ProcessorSimple import ProcessorSimple


class App:
    _config = None
    """Registry for all available attributes."""
    _attrs_availble = {}
    """Registry for all used attributes."""
    _attrs_used = {}
    """Processor to operate with _data according to some schema."""
    _proc = None


    def __init__(self, cfg):
        self._config = cfg

    def run(self):
        self._proc = ProcessorSimple()
        self._config.load()
        attrs_total = self._config.get_dom_attrs_total()
        attrs_per_inst_min = self._config.get_dom_attrs_per_instance_min()
        attrs_per_inst_max = self._config.get_dom_attrs_per_instance_max()
        # validation rules
        # - attrs min & max should comply with attrs total
        logging.info("total different attributes for entity: %i", attrs_total)
        logging.info("min different attributes per one instance: %i", attrs_per_inst_min)
        logging.info("max different attributes per one instance: %i", attrs_per_inst_max)
        # create available attributes registry
        self._init_attrs()
        # pprint(repr(self._attrs_availble))
        self._init_storage()
        return

    def _get_type_by_index(self, ndx):
        """
        Temp. method to return some type by the index.
        :param ndx:
        :return:
        """
        types = {0: 'int', 1: 'decimal', 2: 'string', 3: 'text'}
        result = types.get(ndx, 0)
        return result

    def _init_attrs(self):
        for i in range(self._config.get_dom_attrs_total()):
            type = randint(0, 3)
            key = "a" + repr(i)
            attr = Attribute()
            attr.name = key
            attr.type = self._get_type_by_index(type)
            self._attrs_availble[key] = attr

    def _init_storage(self):
        """
        Create entity instances in storage according to selected scheme and register
        used attributes.
        """
        attrs_total = self._config.get_dom_attrs_total()
        attrs_min = self._config.get_dom_attrs_per_instance_min()
        attrs_max = self._config.get_dom_attrs_per_instance_max()
        keys = list(self._attrs_availble.keys())
        inst_total = self._config.get_dom_inst_total()
        for i in range(inst_total):
            inst = {}
            # get number of the attrs for current instance
            attrs_num = randint(attrs_min, attrs_max)
            for j in range(attrs_num):
                attr_ndx = randint(0, attrs_total - 1)
                attr = keys[attr_ndx]
                self._attrs_used[attr] = self._attrs_availble[attr]
                inst[attr] = self._attrs_used[attr]
            # pprint(repr(i) + ": " + repr(inst))
            self._proc.add_entity_instance(inst)
        logging.info("total %i instances are created, %i different attributes used", inst_total, len(self._attrs_used))