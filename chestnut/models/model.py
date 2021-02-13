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

from models.enums import RightIsMenu


class TbAdmin(Model):
    id = fields.IntField(pk=True, source_field='F_ADMIN_ID', description='SysAdminMod Id')
    name = fields.TextField(source_field='F_ADMIN_Name', description='SysAdminMod Name')
    role = fields.ForeignKeyField(model_name='models.TbAdminRole', related_name='admins', on_delete=fields.RESTRICT)

    class Meta:
        table = "T_ADMIN"
        table_description = "This table for admin"

    def __str__(self):
        return f"SysAdminMod {self.id}: {self.name}"


class TbAdminRole(Model):
    id = fields.IntField(pk=True, source_field='F_ADMIN_ROLE_ID', description='AdminRole Id')
    name = fields.TextField(source_field='F_ADMIN_ROLE_NAME', description='AdminRole Name')
    desc = fields.TextField(source_field='F_ADMIN_ROLE_DESC', description='AdminRole Desc')
    create_timespan = fields.DatetimeField(source_field='F_CREATE_TIMESTAMP', auto_now_add=True)
    update_timespan = fields.DatetimeField(source_field='F_UPDATE_TIMESTAMP', auto_now=True)

    admins: fields.ReverseRelation['TbAdmin']
    rights: fields.ManyToManyRelation['TbAdminRight']

    class Meta:
        table = "T_ADMIN_ROLE"
        table_description = "This table for admin role"

    def __str__(self):
        return f"AdminRole {self.id}: {self.name}"


class TbAdminRight(Model):
    id = fields.IntField(pk=True, source_field='F_ADMIN_RIGHT_ID', description='AdminRight Id')
    parent_id = fields.IntField(source_field='F_ADMIN_RIGHT_PARENT_ID', description='AdminRight Parent Id')
    is_menu = fields.IntEnumField(RightIsMenu, source_field='F_ADMIN_RIGHT_IS_MENU', description='AdminRight is Menu')
    group = fields.TextField(source_field='F_ADMIN_RIGHT_GROUP', description='AdminRight Group')
    model = fields.TextField(source_field='F_ADMIN_RIGHT_MODEL', description='AdminRight Model')
    action = fields.TextField(source_field='F_ADMIN_RIGHT_ACTION', description='AdminRight Action')
    icon = fields.TextField(source_field='F_ADMIN_RIGHT_ICON', description='AdminRight Icon')
    name = fields.TextField(source_field='F_ADMIN_RIGHT_NAME', description='AdminRight Name')
    desc = fields.TextField(source_field='F_ADMIN_RIGHT_DESC', description='AdminRight Desc')
    create_timespan = fields.DatetimeField(source_field='F_CREATE_TIMESTAMP', auto_now_add=True)
    update_timespan = fields.DatetimeField(source_field='F_UPDATE_TIMESTAMP', auto_now=True)

    right_id = fields.ManyToManyField(model_name='models.TbAdminRole', through='T_ADMIN_ROLE_RIGHT_RL',
                                      forward_key='F_ADMIN_ROLE_ID', related_name='rights')

    class Meta:
        table = "T_ADMIN_RIGHT"
        table_description = "This table for admin right"

    def __str__(self):
        return f"AdminRight {self.id}: {self.name}"
