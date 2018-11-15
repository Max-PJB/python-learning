#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/11 17:38
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
-------------------------------------------------
"""
import time
import math

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def double_11_love(n):
    ll = [["$" for _ in range(97)] for _ in range(41)]
    for i in range(0, 97):
        for j in range(0, 41):
            x = (i - 48) / 38.0
            y = (j - 20) / 10.0
            if (x ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3 <= 0:
                ll[j][i] = "1"
            # if x ** 2 + (5.0 * y / 4.0 - math.sqrt(abs(x)) ** 2) <= 1:
            #     ll[i][j] = 1
    for x in ll:
        print(x)


double_11_love(1)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
