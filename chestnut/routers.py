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

from .apis.routers import apis
from .views.routers import system

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.add_subapp('/apis', apis)
    app['apis'] = apis
    app.add_subapp('/system', system)
    app['system'] = system

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
