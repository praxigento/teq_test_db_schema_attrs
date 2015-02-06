__author__ = 'Alex Gusev <alex@flancer64.com>'
from abc import ABCMeta, abstractmethod

from prxgt.domain.filter.filter import Filter


class ProcessorBase(metaclass=ABCMeta):
    @abstractmethod
    def add_entity_inst(self, inst):
        """
        Add new instance to storage.
        :param inst: new instance (contains attributes and values)
        :return:
        """

    @abstractmethod
    def get_inst_by_id(self, instance_id):
        """
        Return instance with attrs by instance_id.
        :param instance_id:
        :return:
        """

    @abstractmethod
    def get_list_by_filter(self, filter_: Filter):
        """
        Return list of instances filtered by filter_data.
        :param filter_:
        :return:
        """

    @abstractmethod
    def get_list_ordered(self, filter_data, order_data):
        """
        Return ordered list of instances filtered by filter_data.
        :param filter_data:
        :return:
        """

    @abstractmethod
    def get_list_paged(self, filter_data, order_data, pages_data):
        """
        Return paged and ordered list of instances filtered by filter_data.
        :param filter_data:
        :return:
        """
