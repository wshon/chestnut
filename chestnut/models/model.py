# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/7 21:20
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: model.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
from tortoise import Model, fields


class TbAdminRole(Model):
    id = fields.IntField(pk=True, source_field='F_ADMIN_ROLE_ID', description='AdminRole Id')
    name = fields.TextField(source_field='F_ADMIN_ROLE_NAME', description='AdminRole Name')
    desc = fields.TextField(source_field='F_ADMIN_ROLE_DESC', description='AdminRole Desc')
    create_timespan = fields.DatetimeField(source_field='F_CREATE_TIMESPAN', auto_now_add=True)
    update_timespan = fields.DatetimeField(source_field='F_UPDATE_TIMESPAN', auto_now=True)

    menus: fields.ManyToManyRelation['TbAdminMenu']

    class Meta:
        table = "T_ADMIN_ROLE"
        table_description = "This table for admin role"

    def __str__(self):
        return f"AdminRole {self.id}: {self.name}"


class TbAdminMenu(Model):
    id = fields.IntField(pk=True, source_field='F_ADMIN_MENU_ID', description='AdminMenu Id')
    parent_id = fields.IntField(source_field='F_ADMIN_MENU_PARENT_ID', description='AdminMenu Parent Id')
    name = fields.TextField(source_field='F_ADMIN_MENU_NAME', description='AdminMenu Name')
    desc = fields.TextField(source_field='F_ADMIN_MENU_DESC', description='AdminMenu Desc')
    icon = fields.TextField(source_field='F_ADMIN_MENU_ICON', description='AdminMenu Icon')
    create_timespan = fields.DatetimeField(source_field='F_CREATE_TIMESPAN', auto_now_add=True)
    update_timespan = fields.DatetimeField(source_field='F_UPDATE_TIMESPAN', auto_now=True)

    menu_id = fields.ManyToManyField(
        'models.TbAdminRole', through='T_ADMIN_ROLE_MENU_RL', forward_key='F_ADMIN_ROLE_ID', related_name='menus')

    class Meta:
        table = "T_ADMIN_MENU"
        table_description = "This table for admin menu"

    def __str__(self):
        return f"AdminMenu {self.id}: {self.name}"
