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
import threading
import time
__author__ = 'Max_Pengjb'

# 实测：在python2.7、mac os下，运行以下代码可能会产生脏数据。但是在python3中就不一定会出现下面的问题。


def run(n):
    global num
    num += 1


num = 0
t_obj = []
for i in range(20000):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()
    t_obj.append(t)
for t in t_obj:
    t.join()
print("num:", num)
"""
产生脏数据后的运行结果：
num: 19999
"""
