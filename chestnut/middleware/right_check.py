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

allow_list = [
    ('GET', '/system/login.html'),
    ('POST', '/system/login.html'),
]


@web.middleware
async def right_check(request, handler):
    if not request.path.startswith('/system'):
        return await handler(request)
    if (request.method, request.path) in allow_list:
        return await handler(request)
    session = await get_session(request)
    if not session.get('is_login', False):
        raise web.HTTPSeeOther(request.app.router.get('system.login').url_for())
    right = await AdminRight.get_right(session.get('admin_id', None), None, None, None)
    if right is None:
        return
    pass
