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

action_list = ['select', 'create', 'update', 'delete']

action_map = {
    'index.html': 'select',
    'new.html': 'create',
    'edit.html': 'update',
}


@web.middleware
async def right_check(request, handler):
    if not request.path.startswith('/system'):
        return await handler(request)

    if (request.method, request.path) in allow_list:
        return await handler(request)

    session = await get_session(request)
    if not session.get('is_login', False):
        raise web.HTTPSeeOther(request.app['system'].router.get('login').url_for())

    if request.path.endswith('.html'):
        last, html_name = request.path[1:].rsplit('/', 1)
        action = action_map.get(html_name, '')
    else:
        if request.path.endswith('/'):
            path = request.path[1:]
        else:
            path = request.path[1:].rsplit('/', 1)
        last, action = path.rsplit('/', 1)
    last_split = last.split('/')
    group = last_split[0]
    if len(last_split) > 1:
        model = '.'.join(last_split[1:])
    else:
        model = ''
    # group, model, action = get_right(request.path)
    # if action not in action_list:
    #     action = action_map.get((action, request.method), None)
    # if action not in action_list:
    #     raise web.HTTPForbidden()
    if model:
        right = await AdminRight.get_right(session.get('admin_id', None), group, model, action)
        if right is None:
            raise web.HTTPForbidden()
    return await handler(request)
    pass
