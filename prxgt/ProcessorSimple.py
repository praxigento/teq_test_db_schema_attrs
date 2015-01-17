__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.ProcessorBase import ProcessorBase


class ProcessorSimple(ProcessorBase):
    """
    Simple in-memory storage processor.
    """

    def add_entity_instance(self, attrs):
        super().add_entity_instance(attrs)


ProcessorBase.register(ProcessorSimple)