# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/22 22:44
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: auth.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""

from aiohttp import web
from aiohttp_session import get_session
from webargs import fields
from webargs.aiohttpparser import use_args

from models.admin import SysAdminMod
from utils.result import OptSuccess


@use_args({"username": fields.Str(required=True), "password": fields.Str(required=True)}, location="json_or_form")
async def login(request, args):
    admin_id = await SysAdminMod.login(args['username'], args['password'])
    if not admin_id:
        raise web.HTTPSeeOther(request.app.router.get('login_fail').url_for())
    session = await get_session(request)
    session['admin_id'] = admin_id
    session['is_login'] = True
    return OptSuccess()


async def logout(request):
    session = await get_session(request)
    if session['is_login']:
        session['is_login'] = False
    raise web.HTTPSeeOther(request.app['system'].router.get('login').url_for())
