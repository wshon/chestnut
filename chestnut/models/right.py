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
from typing import List

from models.enums import RightIsMenu
from models.model import TbAdminRole, TbAdminRight


class AdminRight(object):
    async def get_admin_menu(self, role_id) -> List[TbAdminRight]:
        role = await TbAdminRole.filter(id=role_id).first()
        if not role:
            return []
        rights: List[TbAdminRight] = await self._get_admin_menu(role, parent_id=0, deep=0)
        return rights

    async def _get_admin_menu(self, role, parent_id=0, deep=0) -> List[TbAdminRight]:
        rights: List[TbAdminRight] = await role.rights.filter(parent_id=parent_id, is_menu=RightIsMenu.IS_MENU)
        for right in rights:
            right.childes = await self._get_admin_menu(role, parent_id=right.id, deep=deep + 1)
        return rights

    async def get_right(self):
        return await TbAdminRole.filter().first()
