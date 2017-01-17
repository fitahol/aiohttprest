#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '05/01/2017'
__author__ = 'deling.ma'
"""
from sqlalchemy.ext.serializer import loads, dumps


class empty(object):
    """
    This class is used to represent no data being provided for a given input
    or output value.

    It is required because `None` may be a valid input or output value.
    """
    pass


class BaseSerializer(object):
    
    def __init__(self, instance=None, data=empty, **kwargs):
        self.instance = instance
        if data is not empty:
            self.initial_data = data
        kwargs.pop('many', None)

    @property
    def data(self):
        return dumps(self.instance)


class Serializer(BaseSerializer):
    pass
