__author__ = 'Alex Gusev <alex@flancer64.com>'
import json
import logging


class Config:
    filename = None
    data = None

    def __init__(self, filename='config.json'):
        self.filename = filename

    def load(self):
        cfg_file = open(self.filename)
        self.data = json.load(cfg_file)
        logging.info("configuration is loaded from file '%s'.", self.filename)
        cfg_file.close()

    def getDomAttrsTotal(self):
        return self.data['domain']['attrs_total']

    def getDomAttrsPerInstanceMin(self):
        return self.data['domain']['attrs_per_instance_min']

    def getDomAttrsPerInstanceMax(self):
        return self.data['domain']['attrs_per_instance_max']