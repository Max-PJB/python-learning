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
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块


def myfunc(a, *args, **kwds):
    print('a:', a)
    for i in args:
        print(i)
    for i, j in kwds.items():
        print(i, j)


args = (1, 2)
kwds = {"c": 5, "d": 6}
# for i,j in kwds.items():
#     print(i,j)
myfunc(0, *args, **kwds)
myfunc(1,2,3,c=1,b=2)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
