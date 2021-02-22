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

from models.admin import SysAdminMod


async def login(request):
    post_data = dict()
    if request.content_type == 'application/json':
        post_data = json.loads(str(await request.content.read(), encoding="utf-8"))
    elif request.content_type == 'application/x-www-form-urlencoded' or request.content_type == 'multipart/form-data':
        post_data = await request.post()
    res = await SysAdminMod.login_admin(post_data['username'], post_data['password'])
    return None
