#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/24 10:02
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import os

p = '/haha/hehe/xixi/wo.did.xixi.txt'
print(os.path.splitext(p))
print(os.path.split(p))
print(os.path.basename(p))
print(os.path.dirname(p))
print(os.path.join('a','b','c'))
print(len(os.listdir('./photo')))
