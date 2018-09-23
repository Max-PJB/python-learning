#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/21 19:35
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()
# 下面写上代码块

# m = int(input())
# n = int(input())
# 定义一个函数gcd，功能是求两个正整数的最大公约数；
# 调用函数gcd，得到输入的两个正整数的最大公约数，并输出这个最大公约数。


def gcd(x, y):
    # for i in range(x, 0, -1):   # 2 1 简单易懂
    #     print(i)
    # for i in range(x)[::-1]:  # 1 0 利用list的[start:end:step]排序功能，当然在大数组下性能堪忧，不推荐用这个
    #     print(i)
    for i in range(x if x < y else y, 0, -1):
        if x % i == 0 and y % i == 0:
            return i

print(gcd(3012121212, 1212121212))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
