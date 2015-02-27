from prxgt.domain.filter.filter import Filter
from prxgt.domain.filter.function_rule import FunctionRule
from prxgt.domain.instance import Instance
from prxgt.domain.filter.value import Value
from prxgt.domain.filter.alias import Alias
from prxgt.domain.filter.expression import Expression

__author__ = 'Alex Gusev <alex@flancer64.com>'

_EQ = 'eq'
_GT = 'gt'
_GTE = 'gte'
_LT = 'lt'
_LTE = 'lte'


class Filtrator(object):
    """
    Apply some filter to instance and return 'true' in case of filter
    conditions are applied to the instance or 'false' otherwise.
    """

    @staticmethod
    def is_applied(filter_: Filter, instance: Instance):
        """
        Acceptable filter is a FunctionRule with functions [eq|gt|gte|lt|lte] and 2 args.
        :param filter_:
        :param instance:
        :return:
        """
        result = False
        rule = filter_.rule
        if isinstance(rule, FunctionRule):
            """@type rule: FunctionRule"""
            func = rule.func
            fname = func.name
            # extract first and second arguments
            params = rule.params
            arg1 = Filtrator._extract_value(params[0], instance)
            arg2 = Filtrator._extract_value(params[1], instance)
            if (arg1 is not None) and (arg2 is not None):
                result = Filtrator._compare(fname, arg1, arg2)
        return result


    @staticmethod
    def _extract_value(param: Expression, instance: Instance):
        """
        Extract value from 'param' in case of 'param' is Value or extract value from
        'instance' attribute in case of 'param' is Alias.
        :param param:
        :param instance:
        :return:
        """

        result = None
        if isinstance(param, Value):
            result = param.value
        if isinstance(param, Alias):
            attr_name = param.name
            attr = instance.get_attr(attr_name)
            if attr is not None:
                result = attr.value
        return result


    @staticmethod
    def _compare(name, arg1, arg2):
        """
        Perform comparison.

        :param name: [eq|gt|gte|lt|lte]
        :param arg1:
        :param arg2:
        :return:
        """
        result = False
        if name == _EQ:
            result = (arg1 == arg2)
        elif name == _GT:
            result = (arg1 > arg2)
        elif name == _GTE:
            result = (arg1 >= arg2)
        elif name == _LT:
            result = (arg1 < arg2)
        elif name == _LTE:
            result = (arg1 <= arg2)
        return result