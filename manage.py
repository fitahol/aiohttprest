#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '05/01/2017'
__author__ = 'deling.ma'
"""
import asyncio
from aiohttp import web

from aio_rest import db
from aio_rest import routes
from settings.load import load_settings

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)


app['config'] = load_settings()
app.on_startup.append(db.init_db)
app.on_shutdown.append(db.close_db)

routes.setup_routes(app)

web.run_app(app)
