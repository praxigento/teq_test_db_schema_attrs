__author__ = 'Alex Gusev <alex@flancer64.com>'
from prxgt.proc.base import ProcessorBase
from prxgt.domain.filter.filter import Filter
from prxgt.domain.instance import Instance
from prxgt.repo.repository import Repository


class RepoProcessor(ProcessorBase):
    """
    Simple in-memory storage processor.
    """

    def __init__(self, repo: Repository):
        self._repo = repo
        """Repository to store data and meta data"""

    def get_list_paged(self, filter_data, order_data, pages_data):
        super().get_list_paged(filter_data, order_data, pages_data)

    def get_list_ordered(self, filter_data, order_data):
        super().get_list_ordered(filter_data, order_data)

    def add_instance(self, inst: Instance):
        self._repo.add_instance(inst)
        return

    def get_inst_by_id(self, instance_id) -> Instance:
        result = self._repo.instances[instance_id]
        return result

    def get_list_by_filter(self, filter_: Filter):
        pass


ProcessorBase.register(RepoProcessor)