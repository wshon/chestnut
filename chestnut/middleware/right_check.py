# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/9 21:00
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: right_check.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
from aiohttp import web
from aiohttp_session import get_session

from models.right import AdminRight


@web.middleware
async def right_check(request, handler):
    url = request.url.path
    if not url.startWith('/admin'):
        return await handler(request)
    session = await get_session(request)
    right = await AdminRight.get_right()
    pass
