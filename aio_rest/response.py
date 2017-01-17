#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '05/01/2017'
__author__ = 'deling.ma'
"""
import json

from aiohttp.web import Response as BaseResponse


class Response(BaseResponse):
    
    def __init__(self, data, charset='utf-8', content_type='text/html',
                 status=200):
        if isinstance(data, dict) or isinstance(data, list):
            content_type = 'application/json'
            data = json.dumps(data, indent=4, sort_keys=True,
                              default=lambda x: str(x))
        if isinstance(data, int) or isinstance(data, float):
            data = str(data)
        super(Response, self).__init__(text=data, charset=charset,
                                       content_type=content_type,
                                       status=status)

