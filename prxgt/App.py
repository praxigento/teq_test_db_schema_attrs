__author__ = 'Alex Gusev <alex@flancer64.com>'
import logging
import string
import random
from pprint import pprint

from prxgt.dom.Attribute import Attribute
from prxgt.ProcessorSimple import ProcessorSimple


class App:
    ATTR_TYPE_INT = "int"
    ATTR_TYPE_DEC = "decimal"
    ATTR_TYPE_STR = "string"
    ATTR_TYPE_TXT = "text"
    _config = None
    """Registry for all available attributes."""
    _attrs_available = {}
    """Registry for all used attributes."""
    _attrs_used = {}
    """Processor to operate with data according to some schema."""
    _proc = None

    def __init__(self, cfg):
        self._config = cfg

    def run(self):
        """

        :return:
        """
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
        # pprint(repr(self._attrs_available))
        self._init_storage()
        return

    def _get_random_type(self):
        """
        Return some random type.
        :return:
        """
        types = {0: self.ATTR_TYPE_INT, 1: self.ATTR_TYPE_DEC, 2: self.ATTR_TYPE_STR, 3: self.ATTR_TYPE_TXT}
        ndx = random.randint(0, 3)
        result = types.get(ndx)
        return result

    def _get_value_by_type(self, type_name):
        """
        Return some value for the given type.
        """
        result = None
        if type_name == self.ATTR_TYPE_INT:
            result = random.randint(0, 10);
        if type_name == self.ATTR_TYPE_DEC:
            result = random.randint(0, 10000) / 100;
        if type_name == self.ATTR_TYPE_STR:
            chars = string.ascii_letters + string.digits + " "
            result = ''.join(random.choice(chars) for _ in range(8))
        if type_name == self.ATTR_TYPE_TXT:
            chars = string.ascii_letters + string.digits + " "
            result = ''.join(random.choice(chars) for _ in range(512))
        return result

    def _init_attrs(self):
        for i in range(self._config.get_dom_attrs_total()):
            key = "a" + repr(i)
            attr = Attribute()
            attr.name = key
            attr.type = self._get_random_type()
            self._attrs_available[key] = attr

    def _init_storage(self):
        """
        Create entity instances in storage according to selected scheme and register
        used attributes.
        """
        attrs_total = self._config.get_dom_attrs_total()
        attrs_min = self._config.get_dom_attrs_per_instance_min()
        attrs_max = self._config.get_dom_attrs_per_instance_max()
        attr_names_avlb = list(self._attrs_available.keys())
        inst_total = self._config.get_dom_inst_total()
        for i in range(inst_total):
            inst = {}
            # get number of the attrs for current instance
            attrs_num = random.randint(attrs_min, attrs_max)
            for j in range(attrs_num):
                # get random attribute and generate value for the instance
                attr_ndx = random.randint(0, attrs_total - 1)
                attr_name = attr_names_avlb[attr_ndx]
                # @type prxgt.dom.Attribute
                attr_selected = self._attrs_available[attr_name]
                self._attrs_used[attr_name] = attr_selected
                attr = Attribute()
                attr.name = attr_selected.name
                attr.type = attr_selected.type
                attr.value = self._get_value_by_type(attr_selected.type)
                inst[attr.name] = attr
            pprint(repr(i) + ": " + repr(inst))
            self._proc.add_entity_instance(inst)
        logging.info("total %i instances are created, %i different attributes used", inst_total, len(self._attrs_used))