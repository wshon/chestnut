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
from typing import Dict, Optional, Union

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp_jinja2.helpers import _Context
from aiohttp_session import setup as setup_session, cookie_storage
from cryptography.fernet import Fernet

from chestnut.routers import setup_routes
from database import setup_orm
from middleware.right_check import right_check


@jinja2.contextfunction
def url_for(
        context: _Context,
        __route_name: str,
        app_: str = None,
        query_: Optional[Dict[str, str]] = None,
        **parts: Union[str, int]
):
    """Filter for generating urls.

    Usage: {{ url('the-view-name') }} might become "/path/to/view" or
    {{ url('item-details', id=123, query={'active': 'true'}) }}
    might become "/items/1?active=true".
    """
    if app_:
        app = context["app"][app_]
    else:
        app = context["app"]

    parts_clean: Dict[str, str] = {}
    for key in parts:
        val = parts[key]
        if isinstance(val, str):
            # if type is inherited from str expilict cast to str makes sense
            # if type is exactly str the operation is very fast
            val = str(val)
        elif type(val) is int:
            # int inherited classes like bool are forbidden
            val = str(val)
        else:
            raise TypeError(
                "argument value should be str or int, "
                "got {} -> [{}] {!r}".format(key, type(val), val)
            )
        parts_clean[key] = val

    url = app.router[__route_name].url_for(**parts_clean)
    if query_:
        url = url.with_query(query_)
    return url


def get_app():
    app = web.Application()

    # secret_key must be 32 url-safe base64-encoded bytes
    fernet_key = Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup_session(app, cookie_storage.EncryptedCookieStorage(secret_key))
    setup_routes(app)
    setup_orm(app)

    env = aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('chestnut', 'templates'))
    env.filters['sysconfig'] = lambda _: ''
    env.globals['url'] = url_for

    app.middlewares.append(right_check)

    return app


if __name__ == '__main__':
    web.run_app(get_app())
