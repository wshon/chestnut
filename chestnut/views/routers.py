# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/3/12 22:14
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: routers.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
from aiohttp import web

from .system import (
    index as system_index,
    auth as system_auth,

    admin as system_admin,
    role as system_role,
    user as system_user,
)

system = web.Application()

# admin
# admin index
system.router.add_get('/index.html', system_index.index, name='index')
system.router.add_get('/login.html', system_index.login, name='login')
system.router.add_get('/login.html', system_index.login, name='login_fail')

system.router.add_post('/login.html', system_auth.login, name='login_post')
system.router.add_get('/logout.html', system_auth.logout)

# admin admin
system.router.add_get('/admin/index.html', system_admin.index, name='admin.index')
system.router.add_get('/admin/new.html', system_admin.new, name='admin.new')
system.router.add_view('/admin/', system_admin.Admin, name='admin.admins')
system.router.add_view('/admin/{id}', system_admin.Admin, name='admin.admin')

# admin user
system.router.add_get('/role/index.html', system_role.index, name='role.index')
system.router.add_get('/role/new.html', system_role.new, name='role.new')

# admin user
system.router.add_get('/user/index.html', system_user.index, name='user.index')
system.router.add_get('/user/new.html', system_user.new, name='user.new')
