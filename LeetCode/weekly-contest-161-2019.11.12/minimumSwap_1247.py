#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/12 8:59
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1247. 交换字符使得字符串相同
    https://leetcode-cn.com/contest/weekly-contest-161/problems/minimum-swaps-to-make-strings-equal/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # x y     不同的情况只有这两种，   x x    y y   一次   y x    x y 两次 所以只需要找到  x->y   y->x多少个就行了
        # y x                           y y    x x         x y    y x
        xy = 0
        yx = 0
        for i, j in zip(s1, s2):
            if i == "x" and j == "y":
                xy += 1
            if i == "y" and j == "x":
                yx += 1
        xy_time,xy_remain = divmod(xy,2)
        yx_time,yx_remain = divmod(yx,2)
        res = xy_time + yx_time
        if yx_remain == xy_remain:
            res += yx_remain * 2
            return res
        else:
            return -1


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
