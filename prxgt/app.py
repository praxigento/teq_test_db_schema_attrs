__author__ = 'Alex Gusev <alex@flancer64.com>'
import logging
import random
import string
import time

import prxgt.const as cfg
from prxgt.domain.filter.alias import Alias
from prxgt.domain.filter.filter import Filter
from prxgt.domain.filter.function import Function
from prxgt.domain.filter.function_rule import FunctionRule
from prxgt.domain.filter.value import Value
from prxgt.proc.repo import RepoProcessor
from prxgt.repo.repository import Repository


class App:

    def __init__(self, cfg_):
        self._config = cfg_
        self._attrs_used = {}
        """Registry for all used attributes."""
        self._repo = None
        """
        In-memory repo to registry attributes data to construct filters,
        etc.
        """
        _proc = None
        """Processor to operate with data according to some schema."""
        return

    def run(self):
        self._init_config()
        self._repo = Repository(self._config)
        self._repo.init_all()
        self._proc = RepoProcessor(self._repo)
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
        return

    def _get_paged(self):
        logging.info("\tget paged set of the ordered instances by filter:")
        return

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
        logging.info(
            "\t\t%i iterations are done in %.3f sec;", iterations, time_total)
        return

    def _oper_get_by_filter(self):
        logging.info("\tget instances by filter:")
        iterations = self._config.get_oper_filter_count()
        # attrs_max = self._config.get_oper_filter_attrs_max()
        start_time = time.time()
        for i in range(iterations):
            rule = FunctionRule(
                Function("eq", 2), Alias("entity_id"), Value(32))
            filter_ = Filter(rule)
            self._proc.get_list_by_filter(filter_)
            pass
        time_total = time.time() - start_time
        logging.info(
            "\t\t%i iterations are done in %.3f sec;", iterations, time_total)
        pass

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
            chars = string.ascii_letters + string.digits
            result = ''.join(random.choice(chars) for _ in range(8))
        if type_name == cfg.ATTR_TYPE_TXT:
            chars = string.ascii_letters + string.digits + " "
            result = ''.join(random.choice(chars) for _ in range(512))
        return result
