#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/19 16:18
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       961. 重复 N 次的元素 N-Repeated Element in Size 2N Array
    https://leetcode-cn.com/contest/weekly-contest-116/problems/n-repeated-element-in-size-2n-array/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        res = set()
        for i in A:
            if i not in res:
                res.add(i)
            else:
                return i


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
