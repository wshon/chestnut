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
import json

from aiohttp import web
from aiohttp_session import get_session

from models.admin import SysAdminMod
from utils.exception import *
from utils.result import OptError


async def login(request):
    post_data = dict()
    if request.content_type == 'application/json':
        post_data = json.loads(str(await request.content.read(), encoding="utf-8"))
    elif request.content_type == 'application/x-www-form-urlencoded' or request.content_type == 'multipart/form-data':
        post_data = await request.post()
    try:
        admin_id = await SysAdminMod.login(post_data['username'], post_data['password'])
    except ChestnutError:
        return OptError.LoginFailed()
    session = await get_session(request)
    session['admin_id'] = admin_id
    session['is_login'] = True
    raise web.HTTPSeeOther(request.app.router.get('system.index').url_for())


async def logout(request):
    session = await get_session(request)
    if session['is_login']:
        session['is_login'] = False
    raise web.HTTPSeeOther(request.app.router.get('system.login').url_for())
