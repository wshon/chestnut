# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/7 18:22
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: right.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
import aiohttp_jinja2


@aiohttp_jinja2.template('system/menu/index.html')
async def index(request):
    return None

