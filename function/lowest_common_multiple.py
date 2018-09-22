#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/21 19:43
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""
__author__ = 'Max_Pengjb'

# 编写程序，功能是求两个正整数的最小公倍数；
# 要求实现方法：先定义一个private函数_gcd()求两个正整数的最大公约数，再定义public函数lcm()调用_gcd()函数求两个正整数的最小公倍数。
# 调用函数lcm()，并将输入的两个正整数的最小公倍数输出
# 输入两个正整数a,b
a = int(input())
b = int(input())

# 请在此添加代码，求两个正整数的最小公倍数
# ********** Begin *********#


def _gcd(x, y):
    for i in range(x if x < y else y, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def lcm(x, y):
    return int(x * y / _gcd(x, y))

# ********** End **********#

# 调用函数，并输出a,b的最小公倍数
print(lcm(a, b))
