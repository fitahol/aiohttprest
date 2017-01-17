#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '06/01/2017'
__author__ = 'deling.ma'
"""

from aio_rest.routes import RouteCollector, Route
from example.views import publish, IndexView

routes = RouteCollector(prefix='/app', routes=[
    Route('/', IndexView),
    Route('/publish', publish, method='GET'),
])
