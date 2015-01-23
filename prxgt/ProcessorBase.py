__author__ = 'Alex Gusev <alex@flancer64.com>'
from abc import ABCMeta, abstractmethod


class ProcessorBase(metaclass=ABCMeta):
    @abstractmethod
    def add_entity_inst(self, inst):
        """
        Add new instance to storage.
        :param inst: new instance (contains attributes and values)
        :return:
        """

    @abstractmethod
    def get_inst_by_id(self, id):
        """
        Select and return instance with attrs by id.
        :param id:
        :return:
        """
