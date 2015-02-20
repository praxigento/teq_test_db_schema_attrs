__author__ = 'Alex Gusev <alex@flancer64.com>'

import random
import string

import prxgt.const as const


TYPE_DEC = const.ATTR_TYPE_DEC
TYPE_INT = const.ATTR_TYPE_INT
TYPE_STR = const.ATTR_TYPE_STR
TYPE_TXT = const.ATTR_TYPE_TXT


class Generator(object):
    """
    Values generator for various types data.
    Простой генератор, который возвращает значение для данных какого-либо типа.
    Функция генерации значения может переопределяться через метод set_for_type(type, function).
    Переопределение функции сделано криво - это и не Java (с отдельным типом параметра -
    setForType(TypeGenerator newOne)), и не JavaScript (пока что я не знаю как сделать, чтобы внешняя функция стала
    "родным" методом для объекта).
    """

    def __init__(self):
        self._type_gen = {
            TYPE_DEC: _simple_dec,
            TYPE_INT: _simple_int,
            TYPE_STR: _simple_str,
            TYPE_TXT: _simple_txt
        }
        pass

    def set_for_type(self, type_, function_):
        self._type_gen[type_] = function_

    def get_value(self, type_):
        result = self._type_gen[type_](self)
        return result


"""
Simple generators bound to the types by default.
"""


def _simple_dec(self):
    result = random.randint(0, 10000) / 100
    return result


def _simple_int(self):
    result = random.randint(0, 10)
    return result


def _simple_str(self):
    chars = string.ascii_letters + string.digits
    result = ''.join(random.choice(chars) for _ in range(8))
    return result


def _simple_txt(self):
    chars = string.ascii_letters + string.digits + " "
    result = ''.join(random.choice(chars) for _ in range(512))
    return result