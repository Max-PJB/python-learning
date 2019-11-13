#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/13 9:05
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1052. 爱生气的书店老板 Grumpy Bookstore Owner
    https://leetcode-cn.com/contest/weekly-contest-138/problems/grumpy-bookstore-owner/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # all(0) + X(1) 
        # 求 max（ X（1) )
        satisfied_1 = list(map(lambda x, y: x * y, customers, grumpy))
        satisfied_0 = list(map(lambda x, y: x * (y - 1), customers, grumpy))
        res = [sum(satisfied_1[:X])]
        i, j = 1, X
        while j < len(satisfied_1):
            res.append(res[-1] + satisfied_1[j] - satisfied_1[i-1])
            i += 1
            j += 1
        print(satisfied_0,satisfied_1,res)
        return max(res) - sum(satisfied_0)


customers = [3]
grumpy = [1]
X = 3
rr = Solution().maxSatisfied(customers,grumpy,X)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
