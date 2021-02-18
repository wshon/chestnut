# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/18 21:38
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: result.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
from aiohttp import web


class OptSuccess(object):
    code = 0
    text = '操作成功'

    def __new__(cls, *args, **kwargs):
        return web.json_response({'code': -1, 'message': cls.text})


class OptError:
    class UnknownError(OptSuccess):
        code = -1
        text = '未知错误'

    class PasswordNotSame(OptSuccess):
        code = -1001
        text = '两次密码不一致'
