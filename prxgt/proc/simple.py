__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.proc.base import ProcessorBase
from prxgt.domain.filter.filter import Filter


class SimpleProcessor(ProcessorBase):
    """
    Simple in-memory storage processor.
    """

    """In-memory storage for all instances."""
    _storage = []

    def get_list_paged(self, filter_data, order_data, pages_data):
        super().get_list_paged(filter_data, order_data, pages_data)

    def get_list_ordered(self, filter_data, order_data):
        super().get_list_ordered(filter_data, order_data)

    def add_entity_inst(self, inst):
        self._storage.append(inst)
        return

    def get_inst_by_id(self, instance_id):
        result = self._storage[instance_id]
        return result

    def get_list_by_filter(self, filter_: Filter):
        pass


ProcessorBase.register(SimpleProcessor)