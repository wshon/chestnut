# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/7 18:39
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: right.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""

from models.model import TbAdminRole, TbAdmin


class AdminRight(object):
    @staticmethod
    async def get_right(admin_id, group, model, action):
        admin: TbAdmin = await TbAdmin.filter(id=admin_id).first()
        if admin is None:
            return
        role: TbAdminRole = await admin.role.first()
        if role is None:
            return
        return await role.rights.filter(group=group, model=model, action=action)
