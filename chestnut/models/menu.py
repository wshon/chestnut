# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/10 10:43
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: menu.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    :

"""
from typing import List, Any

from models.enums import RightIsMenu
from models.model import TbAdminRole, TbAdminRight


class SysMenuMod(TbAdminRight):
    childes: List['SysMenuMod'] = None

    def __init__(self, right, **kwargs: Any):
        super().__init__(**kwargs)
        self.__dict__.update(right.__dict__)

    @property
    def link(self) -> str:
        link = ''
        for x in [self.group, self.model, self.action]:
            if x:
                link += '/' + x
        return link + '.html'

    @staticmethod
    async def get_system_menu(role_id) -> List['SysMenuMod']:
        role = await TbAdminRole.filter(id=role_id).first()
        if not role:
            return []
        return await SysMenuMod._get_system_menu(role, parent_id=0, deep=0)

    @staticmethod
    async def _get_system_menu(role, parent_id=0, deep=0) -> List['SysMenuMod']:
        rights: List[TbAdminRight] = await role.rights.filter(parent_id=parent_id, is_menu=RightIsMenu.IS_MENU)
        menus = []
        for right in rights:
            menu = SysMenuMod(right)
            menu.childes = await SysMenuMod._get_system_menu(role, parent_id=menu.id, deep=deep + 1)
            menus.append(menu)
        return menus
