# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2021/2/24 22:33
@Author  : Shon Wang
@Email   : muumlover@live.com
@Blog    : https://blog.wshon.com
@Project : chestnut
@FileName: right.py
@Software: PyCharm
@license : (C) Copyright 2021 by Shon Wang. All rights reserved.
@Desc    : 
    
"""


def get_right(path):
    path_split = path[1:].split('/')
    if len(path_split) == 0:
        return '', '', ''
    elif len(path_split) == 1:
        return path_split[0], '', ''
    elif len(path_split) == 2:
        return path_split[0], '', path_split[1]
    else:
        return path_split[0], '.'.join(path_split[1:-1]), path_split[-1]
