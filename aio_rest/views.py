#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '05/01/2017'
__author__ = 'deling.ma'
"""
from datetime import datetime
from aiohttp import web

from aio_rest import status
from .response import Response


class GenericView(web.View):
    def acquire_db(self):
        return self.request.app['db'].acquire()

    async def get_request_params(self):
        params = await self.request.json()
        time_ = datetime.now()
        params['utime'] = params['ctime'] = time_
        return params


class APIView(GenericView):
    model = None

    @property
    def pk(self):
        return self.request.match_info['pk']

    async def get_object(self, conn=None):
        if not conn:
            async with self.acquire_db() as conn:
                cursor = await conn.execute(
                    self.model.select(self.model.c.id == self.pk))
                data = await cursor.fetchone()
        else:
            cursor = await conn.execute(
                self.model.select(self.model.c.id == self.pk))
            data = await cursor.fetchone()
        return dict(data)
    
    async def del_object(self, conn):
        await conn.execute(
            self.model.delete(self.model.c.id == self.pk))
        return

    async def get_queryset(self, ):
        async with self.acquire_db() as conn:
            cursor = await conn.execute(self.model.select())
            records = await cursor.fetchall()
            results = [dict(n) for n in records]
        return results

    async def update(self, conn):
        params = await self.get_request_params()
        update = (self.model
                  .update()
                  .values(**params)
                  .where(self.model.c.id == self.pk))
        result = await conn.execute(update)
        return result
    
    async def get(self):
        if self.request.match_info.get("pk"):
            return Response(data=await self.get_object())
        return Response(data=await self.get_queryset(),
                        status=status.HTTP_200_OK)

    async def put(self):
        async with self.acquire_db() as conn:
            await self.update(conn)
            return Response(data=await self.get_object(conn),
                            status=status.HTTP_202_ACCEPTED)

    async def post(self):
        params = await self.get_request_params()
        async with self.acquire_db() as conn:
            cursor = await conn.execute(self.model.insert(params))
        return Response(data={"detail": "success"},
                        status=status.HTTP_201_CREATED)
    
    async def delete(self):
        async with self.acquire_db() as conn:
            await self.del_object(conn)
        return Response(data={"detail": "accept"},
                        status=status.HTTP_202_ACCEPTED)
