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

from .views.admin import (
    index as admin_index,

    adminer as admin_adminer,
    role as admin_role,
    user as admin_user,
)

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    # admin
    # admin index
    app.router.add_get('/admin/index.html', admin_index.index)

    # admin adminer
    app.router.add_get('/admin/adminer/index.html', admin_adminer.index, name='admin_adminer.index')
    app.router.add_get('/admin/adminer/new.html', admin_adminer.new, name='admin_adminer.new')

    # admin user
    app.router.add_get('/admin/role/index.html', admin_role.index, name='admin_role.index')
    app.router.add_get('/admin/role/new.html', admin_role.new, name='admin_role.new')

    # admin user
    app.router.add_get('/admin/user/index.html', admin_user.index, name='admin_user.index')
    app.router.add_get('/admin/user/new.html', admin_user.new, name='admin_user.new')

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
