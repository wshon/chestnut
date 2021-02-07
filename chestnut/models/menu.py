# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/7 18:39
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: menu.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
from models.model import TbAdminRole


class AdminMenu(object):
    async def get_admin_menu(self, role_id):
        role = await TbAdminRole.filter(id=role_id).first()
        menus = await role.menus.all()
        return menus
