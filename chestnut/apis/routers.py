# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/3/12 22:14
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: routers.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
from aiohttp import web

from .v1.routers import api_v1

apis = web.Application()

apis.add_subapp('/v1', api_v1)
apis['v1'] = api_v1
