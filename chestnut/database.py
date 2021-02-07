# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/7 19:01
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: database.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
import pathlib

from tortoise.contrib.aiohttp import register_tortoise

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_orm(app):
    register_tortoise(
        app,
        db_url=f'sqlite://{PROJECT_ROOT.parent}/db.sqlite3',
        modules={"models": ["models.model"]},
        generate_schemas=True
    )
    pass
