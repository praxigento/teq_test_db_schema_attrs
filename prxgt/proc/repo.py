__author__ = 'Alex Gusev <alex@flancer64.com>'
import random

from prxgt.proc.base import ProcessorBase
from prxgt.domain.filter.filter import Filter
from prxgt.domain.instance import Instance
from prxgt.repo.repository import Repository


class RepoProcessor(ProcessorBase):
    """
    Simple in-memory processor based on Repository object. Used in development
    purposes only to test operations.
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
        result = {}
        assert (isinstance(self._repo, Repository))
        instances = self._repo.instances
        assert (isinstance(instances, dict))
        for id_ in instances:
            one = instances[id_]
            # TODO: we need comparator to get filtration result for the concrete instance
            if comparator(filter, one):
                result[one.id] = one
            pass
        return result


def comparator(filter, instance):
    chance = random.randint(0, 10)
    result = (chance > 9)
    return result

# TODO: should we register subclasses in parent?
# ProcessorBase.register(RepoProcessor)
