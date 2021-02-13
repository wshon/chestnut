# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/10 10:25
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: admin.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    :

"""
import aiohttp_jinja2
from aiohttp import web
from aiohttp_cors import CorsViewMixin

from models.admin import SysAdminMod


@aiohttp_jinja2.template('system/admin/index.html')
async def index(request):
    data = dict()
    data['admins'] = await SysAdminMod.get_all_admin()
    return data


@aiohttp_jinja2.template('system/admin/new.html')
async def new(request):
    return None


class Admin(web.View, CorsViewMixin):

    async def get(self):
        return await get_resp(self.request)

    async def post(self):
        return await post_resp(self.request)
