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
    id = fields.IntField(pk=True, source_field='F_ADMIN_ID', description='SysAdminMod id', generated=True)
    username = fields.TextField(source_field='F_ADMIN_USERNAME', description='SysAdminMod username')
    password = fields.TextField(source_field='F_ADMIN_PASSWORD', description='SysAdminMod password')
    first_name = fields.TextField(source_field='F_ADMIN_FIRST_NAME', description='SysAdminMod first name', null=True)
    last_name = fields.TextField(source_field='F_ADMIN_LAST_NAME', description='SysAdminMod last name', null=True)
    last_login = fields.DatetimeField(source_field='F_LAST_LOGIN_TIME', description='SysAdminMod last login', null=True)

    create_timestamp = fields.DatetimeField(source_field='F_CREATE_TIMESTAMP', auto_now_add=True)
    update_timestamp = fields.DatetimeField(source_field='F_UPDATE_TIMESTAMP', auto_now=True)

    role = fields.ForeignKeyField(model_name='models.TbAdminRole', related_name='admins', on_delete=fields.RESTRICT,
                                  source_field='F_ADMIN_ROLE_ID')

    class Meta:
        table = "T_ADMIN"
        table_description = "This table for admin"

    def __str__(self):
        return f"SysAdminMod {self.id}: {self.username}"


class TbAdminRole(Model):
    id = fields.IntField(pk=True, source_field='F_ADMIN_ROLE_ID', description='AdminRole id', generated=True)
    name = fields.TextField(source_field='F_ADMIN_ROLE_NAME', description='AdminRole name')
    desc = fields.TextField(source_field='F_ADMIN_ROLE_DESC', description='AdminRole desc')

    create_timestamp = fields.DatetimeField(source_field='F_CREATE_TIMESTAMP', auto_now_add=True)
    update_timestamp = fields.DatetimeField(source_field='F_UPDATE_TIMESTAMP', auto_now=True)

    admins: fields.ReverseRelation['TbAdmin']
    rights: fields.ManyToManyRelation['TbAdminRight']

    class Meta:
        table = "T_ADMIN_ROLE"
        table_description = "This table for admin role"

    def __str__(self):
        return f"AdminRole {self.id}: {self.name}"


class TbAdminRight(Model):
    id = fields.IntField(pk=True, source_field='F_ADMIN_RIGHT_ID', description='AdminRight id', generated=True)
    parent_id = fields.IntField(source_field='F_ADMIN_RIGHT_PARENT_ID', description='AdminRight parent id')
    is_menu = fields.IntEnumField(RightIsMenu, source_field='F_ADMIN_RIGHT_IS_MENU', description='AdminRight is menu')
    group = fields.TextField(source_field='F_ADMIN_RIGHT_GROUP', description='AdminRight group')
    model = fields.TextField(source_field='F_ADMIN_RIGHT_MODEL', description='AdminRight model')
    action = fields.TextField(source_field='F_ADMIN_RIGHT_ACTION', description='AdminRight action')
    icon = fields.TextField(source_field='F_ADMIN_RIGHT_ICON', description='AdminRight icon')
    name = fields.TextField(source_field='F_ADMIN_RIGHT_NAME', description='AdminRight name')
    desc = fields.TextField(source_field='F_ADMIN_RIGHT_DESC', description='AdminRight desc')

    create_timestamp = fields.DatetimeField(source_field='F_CREATE_TIMESTAMP', auto_now_add=True)
    update_timestamp = fields.DatetimeField(source_field='F_UPDATE_TIMESTAMP', auto_now=True)

    right_id = fields.ManyToManyField(model_name='models.TbAdminRole', through='T_ADMIN_ROLE_RIGHT_RL',
                                      forward_key='F_ADMIN_ROLE_ID', backward_key='F_ADMIN_RIGHT_ID',
                                      related_name='rights', on_delete=fields.RESTRICT)

    class Meta:
        table = "T_ADMIN_RIGHT"
        table_description = "This table for admin right"

    def __str__(self):
        return f"AdminRight {self.id}: {self.name}"
