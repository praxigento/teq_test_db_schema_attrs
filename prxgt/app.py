__author__ = 'Alex Gusev <alex@flancer64.com>'
import logging
import string
import random
import time

import prxgt.const as cfg
from prxgt.domain.attribute import Attribute
from prxgt.domain.filter import FilterOld
from prxgt.proc.simple import SimpleProcessor


class App:
    _config = None
    """Registry for all available attributes."""
    _attrs_available = {}
    """Registry for all used attributes."""
    _attrs_used = {}
    """Processor to operate with data according to some schema."""
    _proc = None

    def __init__(self, cfg_):
        self._config = cfg_
        return

    def run(self):
        self._proc = SimpleProcessor()
        self._init_config()
        self._init_attrs()
        self._init_storage()
        self._operations()
        self._save_results()
        return

    def _save_results(self):
        logging.info("save results to file;")
        return

    def _init_config(self):
        self._config.load()
        # TODO: validation rules
        # - attrs min & max should comply with attrs total
        return

    def _operations(self):
        logging.info("call data access operations:")
        self._oper_get_instance()
        self._oper_get_by_filter()
        self._get_ordered()
        self._get_paged()
        return

    def _get_ordered(self):
        logging.info("\tget set of the ordered instances:")
        pass

    def _get_paged(self):
        logging.info("\tget paged set of the ordered instances by filter:")
        pass

    def _oper_get_instance(self):
        """
        Test getting the instance with all attributes from storage.
        :return:
        """
        logging.info("\tget instance with attributes by id:")
        total_instances = self._config.get_dom_inst_total()
        iterations = self._config.get_oper_inst_count()
        start_time = time.time()
        for i in range(iterations):
            # generate random ID from available IDs range
            instance_id = random.randint(0, total_instances - 1)
            instance = self._proc.get_inst_by_id(instance_id)
            # should we validate instance data?
            pass
        time_total = time.time() - start_time
        logging.info("\t\t%i iterations are done in %.3f sec;", iterations, time_total)
        return

    def _oper_get_by_filter(self):
        logging.info("\tget instances by filter:")
        iterations = self._config.get_oper_filter_count()
        attrs_max = self._config.get_oper_filter_attrs_max()
        start_time = time.time()
        for i in range(iterations):
            filter_ = FilterOld()
            self._proc.get_list_by_filter(filter_)
            pass
        time_total = time.time() - start_time
        logging.info("\t\t%i iterations are done in %.3f sec;", iterations, time_total)
        pass

    def _get_random_type(self):
        """
        Return some random type.
        :return:
        """
        types = {0: cfg.ATTR_TYPE_INT, 1: cfg.ATTR_TYPE_DEC, 2: cfg.ATTR_TYPE_STR, 3: cfg.ATTR_TYPE_TXT}
        ndx = random.randint(0, 3)
        result = types.get(ndx)
        return result

    def _get_value_by_type(self, type_name):
        """
        Return some value for the given type.
        """
        result = None
        if type_name == cfg.ATTR_TYPE_INT:
            result = random.randint(0, 10)
        if type_name == cfg.ATTR_TYPE_DEC:
            result = random.randint(0, 10000) / 100
        if type_name == cfg.ATTR_TYPE_STR:
            chars = string.ascii_letters + string.digits + " "
            result = ''.join(random.choice(chars) for _ in range(8))
        if type_name == cfg.ATTR_TYPE_TXT:
            chars = string.ascii_letters + string.digits + " "
            result = ''.join(random.choice(chars) for _ in range(512))
        return result

    def _init_attrs(self):
        logging.info("create registry for available attributes;")
        for i in range(self._config.get_dom_attrs_total()):
            key = "a" + repr(i)
            attr = Attribute()
            attr.name = key
            attr.type = self._get_random_type()
            self._attrs_available[key] = attr
        return

    def _init_storage(self):
        """
        Create entity instances in storage according to selected scheme and register
        used attributes.
        """
        logging.info("create instances using simple data processor:")
        attrs_total = self._config.get_dom_attrs_total()
        attrs_min = self._config.get_dom_attrs_per_instance_min()
        attrs_max = self._config.get_dom_attrs_per_instance_max()
        attr_names_avlb = list(self._attrs_available.keys())
        inst_total = self._config.get_dom_inst_total()

        logging.info("\ttotal different attributes for entity: %i;", attrs_total)
        logging.info("\tmin different attributes per one instance: %i;", attrs_min)
        logging.info("\tmax different attributes per one instance: %i;", attrs_max)
        logging.info("\ttotal instances in storage: %i;", inst_total)

        for i in range(inst_total):
            inst = {}
            # get number of the attrs for current instance
            attrs_num = random.randint(attrs_min, attrs_max)
            for j in range(attrs_num):
                # get random attribute and generate value for the instance
                attr_ndx = random.randint(0, attrs_total - 1)
                attr_name = attr_names_avlb[attr_ndx]
                # @type prxgt.domain.Attribute.Attribute
                attr_selected = self._attrs_available[attr_name]
                self._attrs_used[attr_name] = attr_selected
                attr = Attribute()
                attr.name = attr_selected.name
                attr.type = attr_selected.type
                attr.value = self._get_value_by_type(attr_selected.type)
                inst[attr.name] = attr
            self._proc.add_entity_inst(inst)
        logging.info("\ttotal %i instances are created, %i different attributes are used;", inst_total,
                     len(self._attrs_used))
        # pprint(self._proc.storage)
        return
