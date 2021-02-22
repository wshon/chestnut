# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/7 17:56
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: index.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
import aiohttp_jinja2

from models.menu import SysMenuMod


@aiohttp_jinja2.template('system/index/index.html')
async def index(request):
    data = dict()
    data['menus'] = await SysMenuMod.get_system_menu(1)
    return data


@aiohttp_jinja2.template('system/index/login.html')
async def login(request):
    return None


@aiohttp_jinja2.template('system/index/logout.html')
async def logout(request):
    return None
