__author__ = 'Alex Gusev <alex@flancer64.com>'
import logging
from prxgt.dom.Attribute import Attribute
from prxgt.ProcessorBase import ProcessorBase
from random import randint
from pprint import pprint


class App:
    config = None
    """Registry for all available attributes."""
    attrsAvailable = {}
    """Registry for all used attributes."""
    attrsUsed = {}

    def __init__(self, cfg):
        self.config = cfg

    def run(self):
        self.config.load()
        attrs_total = self.config.getDomAttrsTotal()
        attrs_per_inst_min = self.config.getDomAttrsPerInstanceMin()
        attrs_per_inst_max = self.config.getDomAttrsPerInstanceMax()
        # validation rules
        # - attrs min & max should comply with attrs total
        logging.info("total different attributes for entity: %i", attrs_total)
        logging.info("min different attributes per one instance: %i", attrs_per_inst_min)
        logging.info("max different attributes per one instance: %i", attrs_per_inst_max)
        # create available attributes registry
        self.initAttrs()
        pprint(repr(self.attrsAvailable))
        # create all instances
        attrs_min = self.config.getDomAttrsPerInstanceMin()
        attrs_max = self.config.getDomAttrsPerInstanceMax()
        keys = list(self.attrsAvailable.keys())
        for i in range(self.config.getDomInstTotal()):
            inst = {}
            # get number of the attrs for current instance
            attrs_num = randint(attrs_min, attrs_max)
            for j in range(attrs_num):
                attr_ndx = randint(0, attrs_total - 1)
                attr = keys[attr_ndx]
                self.attrsUsed[attr] = self.attrsAvailable[attr]
                inst[attr] = self.attrsUsed[attr]
            pprint(repr(i) + ": " + repr(inst))
        pprint(repr(self.attrsUsed))
        return

    def _getTypeByIndex(self, ndx):
        """
        Temp. method to return some type by the index.
        :param ndx:
        :return:
        """
        types = {0: 'int', 1: 'decimal', 2: 'string', 3: 'text'}
        result = types.get(ndx, 0)
        return result

    def initAttrs(self):
        for i in range(self.config.getDomAttrsTotal()):
            type = randint(0, 3)
            key = "a" + repr(i)
            attr = Attribute()
            attr.name = key
            attr.type = self._getTypeByIndex(type)
            self.attrsAvailable[key] = attr