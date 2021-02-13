# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/13 22:29
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: admin.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
from models.model import TbAdmin


class SysAdminMod(object):
    @staticmethod
    async def get_all_admin():
        admins = await TbAdmin.all()
        for admin in admins:
            admin.role = await admin.role.first()
        return admins
