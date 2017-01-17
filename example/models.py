#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '06/01/2017'
__author__ = 'deling.ma'
"""
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Table

from aio_rest.db import meta

User = Table("user_info", meta,
             Column("id", Integer, primary_key=True),
             Column("phone", String(32)),
             Column("ctime", DateTime),
             Column("utime", DateTime, nullable=True),
             Column("is_bind", Boolean, server_default="1"),
             Column("remark", String(500), server_default="")
             )
