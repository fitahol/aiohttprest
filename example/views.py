#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '06/01/2017'
__author__ = 'deling.ma'
"""
from aio_rest.response import Response
from aio_rest.views import APIView
from example.models import User


class IndexView(APIView):
    model = User


async def publish(request):
    return Response(data='OK')

