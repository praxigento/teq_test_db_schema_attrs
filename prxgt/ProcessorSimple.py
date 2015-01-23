__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.ProcessorBase import ProcessorBase


class ProcessorSimple(ProcessorBase):
    """
    Simple in-memory storage processor.
    """
    """In-memory storage for all instances."""
    _storage = []

    def add_entity_inst(self, inst):
        self._storage.append(inst)
        return

    def get_inst_by_id(self, instance_id):
        result = self._storage[instance_id]
        return result


ProcessorBase.register(ProcessorSimple)