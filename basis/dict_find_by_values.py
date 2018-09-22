#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/22 15:09
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import collections
__author__ = 'Max_Pengjb'


jimscore = int(input())
jerryscore = int(input())
#请在此添加代码，判断若jim的得分jimscore更高，则赢家为jim。若jerry的得分jerryscore更高，则赢家为jerry并输出赢家的名字。
#********** Begin *********#
dict1 = {}
dict1['jim'] = jimscore
dict1['jerry'] = jerryscore
x = 3
print(isinstance(dict1.values(), collections.Iterable))
print(isinstance(dict1.values(), collections.Iterator))
print(isinstance(iter(dict1.values()), collections.Iterator))
print(list(dict1.keys())[list(dict1.values()).index(x)])

# x:jimscore if jimscore > jerryscore else jerryscore