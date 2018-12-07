#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/6 19:07
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :      最大公约数
    最大公倍数 = a * b / 最大公约数
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
def gcd(a, b):
    print("sd")
    """
    :param a: int
    :param b: int
    a >= b
    :return: int
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
