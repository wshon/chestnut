# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/7 18:01
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: debug.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""

import _locale

from aiohttp_debugmode import Debugmode

from app import get_app

_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])
Debugmode.run_app(get_app())
