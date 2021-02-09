# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/9 19:20
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: enums.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
from enum import IntEnum


class RightIsMenu(IntEnum):
    IS_MENU = 1
    NOT_MENU = 0

    @classmethod
    def choices(cls):
        return {
            cls.IS_MENU: 'IS_MENU',
            cls.NOT_MENU: 'NOT_MENU'
        }
