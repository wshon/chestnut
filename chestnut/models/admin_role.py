# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/14 18:39
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: admin_role.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
from models.model import TbAdminRole


class SysAdminRoleMod(object):
    @staticmethod
    async def get_all_admin_role():
        admin_roles = await TbAdminRole.all()
        return admin_roles
