# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/7 17:18
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: routers.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
import pathlib

import aiohttp_cors

from .views.system import (
    index as system_index,

    admin as system_admin,
    role as system_role,
    user as system_user,
)

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    # admin
    # admin index
    app.router.add_get('/system/index.html', system_index.index)

    # admin admin
    app.router.add_get('/system/admin/index.html', system_admin.index, name='system_admin.index')
    app.router.add_get('/system/admin/new.html', system_admin.new, name='system_admin.new')
    app.router.add_view('/system/admin/{id}', system_admin.Admin, name='system_admin.admin')

    # admin user
    app.router.add_get('/system/role/index.html', system_role.index, name='system_role.index')
    app.router.add_get('/system/role/new.html', system_role.new, name='system_role.new')

    # admin user
    app.router.add_get('/system/user/index.html', system_user.index, name='system_user.index')
    app.router.add_get('/system/user/new.html', system_user.new, name='system_user.new')

    # Configure default CORS settings.
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })
    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        cors.add(route)
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/', path=PROJECT_ROOT / 'static', name='static')
    app['static_root_url'] = '/static'
