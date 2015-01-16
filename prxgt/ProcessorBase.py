__author__ = 'Alex Gusev <alex@flancer64.com>'
from abc import ABCMeta, abstractmethod


class ProcessorBase(metaclass=ABCMeta):
    @abstractmethod
    def method1(self):
        pass
