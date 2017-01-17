#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '06/01/2017'
__author__ = 'deling.ma'
"""
import aioodbc
import aiomysql.sa
import sqlalchemy as sa


async def init_db(app):
    db_conf = app['config']['db']
    engine = await aiomysql.sa.create_engine(
        db=db_conf['database'],
        user=db_conf['user'],
        password=db_conf['password'],
        host=db_conf['host'],
        port=db_conf['port'],
        loop=app.loop)
    if "sqlite" in db_conf["engine"]:
        dsn = 'Driver=SQLite;Database=%s' % db_conf['database']
        engine = await aioodbc.create_pool(dsn=dsn, loop=app.loop)
    app['db'] = engine


async def close_db(app):
    app['db'].close()
    await app['db'].wait_closed()


meta = sa.MetaData()
