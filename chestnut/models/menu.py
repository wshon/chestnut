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


class AdminMenu(TbAdminRight):
    childes: List['AdminMenu'] = None

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
    async def get_admin_menu(role_id) -> List['AdminMenu']:
        role = await TbAdminRole.filter(id=role_id).first()
        if not role:
            return []
        return await AdminMenu._get_admin_menu(role, parent_id=0, deep=0)

    @staticmethod
    async def _get_admin_menu(role, parent_id=0, deep=0) -> List['AdminMenu']:
        rights: List[TbAdminRight] = await role.rights.filter(parent_id=parent_id, is_menu=RightIsMenu.IS_MENU)
        menus = []
        for right in rights:
            menu = AdminMenu(right)
            menu.childes = await AdminMenu._get_admin_menu(role, parent_id=menu.id, deep=deep + 1)
            menus.append(menu)
        return menus
