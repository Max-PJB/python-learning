#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/23 22:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

# 从一个python列表里面删除‘’，‘ ’，None, 有时候 list 会产生 删除 空，空格，None
time_list = ['', '', ' ', None, 1, 2, 3]
print(time_list)
# ['', '', ' ', None, 1, 2, 3]
ret1 = [x for x in time_list if x not in ['', ' ', None]]
ret2 = [x for x in time_list if x is not None]
print(ret1)
print(ret2)
# [1, 2, 3]
