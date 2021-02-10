# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/10 10:25
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: adminer.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    :

"""
import aiohttp_jinja2


@aiohttp_jinja2.template('admin/adminer/index.html')
async def index(request):
    return None


@aiohttp_jinja2.template('admin/adminer/new.html')
async def new(request):
    return None
