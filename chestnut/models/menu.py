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
from typing import List

from models.model import TbAdminRole, TbAdminMenu


class AdminMenu(object):
    async def get_admin_menu(self, role_id) -> List[TbAdminMenu]:
        role = await TbAdminRole.filter(id=role_id).first()
        if not role:
            return []
        menus: List[TbAdminMenu] = await self._get_admin_menu(role, parent_id=0, deep=0)
        return menus

    async def _get_admin_menu(self, role, parent_id=0, deep=0) -> List[TbAdminMenu]:
        menus: List[TbAdminMenu] = await role.menus.filter(parent_id=parent_id)
        for menu in menus:
            menu.childes = await self._get_admin_menu(role, parent_id=menu.id, deep=deep + 1)
        return menus
