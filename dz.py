#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/14 11:56
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()

# 下面写上代码块
with open("123.Dzk", "rb") as f:
    cnt = f.readlines()
    while cnt:
        print(cnt)
        cnt = f.readline()
tian_dict = {"天": [0x0E, 0x04, 0x04, 0x1F, 0x04, 0x0A, 0x0A, 0x11]}
dz = tian_dict["天"]
res = [[] for _ in range(8)]
for i in range(8):
    for j in range(8):
        col = dz[i]
        res[i].insert(0, (col >> j) & 1)
for i in range(8):
    for j in range(8):
        if res[i][j]:
            print(res[i][j], " ", end="")
        else:
            print("  ", end="")
    print("")
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
