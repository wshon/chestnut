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
import json

import aiohttp_jinja2
from aiohttp import web
from aiohttp_cors import CorsViewMixin

from models.admin import SysAdminMod
from models.admin_role import SysAdminRoleMod
from utils.result import OptError, OptSuccess


@aiohttp_jinja2.template('system/admin/index.html')
async def index(request):
    data = dict()
    data['admins'] = await SysAdminMod.get_all_admin()
    return data


@aiohttp_jinja2.template('system/admin/new.html')
async def new(request):
    data = dict()
    data['roles'] = await SysAdminRoleMod.get_all_admin_role()
    return data


class Admin(web.View, CorsViewMixin):

    async def get(self):
        return await self.select_all_admins()

    async def post(self):
        return await self.create_admin()

    async def select_all_admins(self):
        pass

    async def create_admin(self):
        post_data = dict()
        if self.request.content_type == 'application/json':
            post_data = json.loads(str(await self.request.content.read(), encoding="utf-8"))
        elif self.request.content_type == 'application/x-www-form-urlencoded' or self.request.content_type == 'multipart/form-data':
            post_data = await self.request.post()
        if post_data.get('pass') != post_data.get('repass'):
            return OptError.PasswordNotSame()

        await SysAdminMod.add_admin(post_data)
        return OptSuccess()

    async def select_admin(self, admin_id):
        pass

    async def update_admin(self, admin_id):
        pass

    async def delete_admin(self, admin_id):
        pass
