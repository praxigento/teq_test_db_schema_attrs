__author__ = 'Alex Gusev <alex@flancer64.com>'
from abc import ABCMeta, abstractmethod


class ProcessorBase(metaclass=ABCMeta):
    @abstractmethod
    def add_entity_instance(self, inst):
        """
        Add new instance to storage.
        :param inst: attributes for new instance
        :return:
        """
