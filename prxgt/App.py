__author__ = 'Alex Gusev <alex@flancer64.com>'
import logging
from prxgt.dom.Attribute import Attribute
from prxgt.ProcessorBase import ProcessorBase
from random import randint
from pprint import pprint


class App:
    config = None
    """Registry for all available attributes."""
    attrsRegistry = {}

    def __init__(self, cfg):
        self.config = cfg

    def run(self):
        self.config.load()
        attrs_total = self.config.getDomAttrsTotal()
        attrs_per_inst_min = self.config.getDomAttrsPerInstanceMin()
        attrs_per_inst_max = self.config.getDomAttrsPerInstanceMax()
        logging.info("total different attributes for entity: %i", attrs_total)
        logging.info("min different attributes per one instance: %i", attrs_per_inst_min)
        logging.info("max different attributes per one instance: %i", attrs_per_inst_max)

        # create attributes registry
        for i in range(0, attrs_total):
            type = randint(0, 3)
            key = "a" + repr(i)
            attr = Attribute()
            attr.name = key
            attr.type = self._getTypeByIndex(type)
            self.attrsRegistry[key] = attr

        pprint(repr(self.attrsRegistry))
        return

    def _getTypeByIndex(self, ndx):
        types = {0: 'int', 1: 'decimal', 2: 'string', 3: 'text'}
        result = types.get(ndx, 0)
        return result
