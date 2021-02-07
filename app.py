# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/7 16:38
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: app.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
import base64

import aiohttp_jinja2
import fernet
import jinja2
from aiohttp import web
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from chestnut.routers import setup_routes
from database import setup_orm


def get_app():
    app = web.Application()
    # secret_key must be 32 url-safe base64-encoded bytes
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))

    setup_routes(app)
    setup_orm(app)

    env = aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('chestnut', 'templates'))
    env.filters['sysconfig'] = lambda _: ''
    return app


if __name__ == '__main__':
    web.run_app(get_app())
