# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/13 22:29
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: admin.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""
import hashlib
import os
from datetime import datetime

from models.model import TbAdmin


class SysAdminMod(object):
    @staticmethod
    async def fetch_all():
        admins = await TbAdmin.all()
        for admin in admins:
            admin.role = await admin.role.first()
        return admins

    @staticmethod
    async def create(data):
        pass_salt = os.urandom(8)
        pass_byte = hashlib.scrypt(data['password'].encode(), salt=pass_salt, n=2048, r=8, p=1, dklen=24)
        pass_db = pass_byte + pass_salt
        data['password'] = pass_db.hex()
        admin_new = TbAdmin()
        await admin_new.update_from_dict(data)
        await admin_new.save()

    @staticmethod
    async def login(username, passward):
        admin = await TbAdmin.filter(username=username).first()
        pass_db = bytes.fromhex(admin.password)
        pass_salt = pass_db[:8]
        pass_byte = hashlib.scrypt(passward.encode(), salt=pass_salt, n=2048, r=8, p=1, dklen=24)
        if pass_byte != pass_db[8:]:
            return False
        admin.last_login = datetime.now()
        await admin.save()
        return admin.id
