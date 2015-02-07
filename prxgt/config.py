__author__ = 'Alex Gusev <alex@flancer64.com>'
import json
import logging


class Config:
    _filename = None
    _data = None

    def __init__(self, filename='config.json'):
        self._filename = filename

    def load(self):
        cfg_file = open(self._filename)
        self._data = json.load(cfg_file)
        logging.info("configuration is loaded from file '%s';", self._filename)
        cfg_file.close()

    def get_dom_attrs_total(self):
        return self._data['domain']['attrs_total']

    def get_dom_attrs_per_instance_min(self):
        return self._data['domain']['attrs_per_instance_min']

    def get_dom_attrs_per_instance_max(self):
        return self._data['domain']['attrs_per_instance_max']

    def get_dom_inst_total(self):
        return self._data['domain']['instances_total']

    def get_oper_inst_count(self):
        return self._data['operations']['get_instance']['count']

    def get_oper_filter_count(self):
        return self._data['operations']['get_by_filter']['count']

    def get_oper_filter_attrs_max(self):
        return self._data['operations']['get_by_filter']['attrs_in_filter_max']

    def get_oper_filter_attrs_min(self):
        return self._data['operations']['get_by_filter']['attrs_in_filter_min']
