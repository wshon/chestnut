# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/3/13 16:37
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: add_admin.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
import asyncio

from tortoise import Tortoise

from database import PROJECT_ROOT
from models.admin import SysAdminMod


async def add_admin(username, password):
    await Tortoise.init(
        db_url=f'sqlite://{PROJECT_ROOT.parent}/db.sqlite3',
        modules={"models": ["models.model"]}
    )
    await SysAdminMod.create({
        'username': username,
        'password': password,
        'role_id': 1,
    })


if __name__ == '__main__':
    asyncio.run(add_admin('admin', 'admin'))
