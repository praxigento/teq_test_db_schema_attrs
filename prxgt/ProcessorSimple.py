__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.ProcessorBase import ProcessorBase


class ProcessorSimple(ProcessorBase):
    """
    Simple in-memory storage processor.
    """
    """In-memory storage for all instances."""
    storage = None

    def add_entity_instance(self, inst):
        super().add_entity_instance(inst)


ProcessorBase.register(ProcessorSimple)