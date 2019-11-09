#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/7 10:53
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1094. 拼车
    https://leetcode-cn.com/contest/weekly-contest-142/problems/car-pooling/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 动态规划，
        # [m,i,j]表示 i 地点上车了 m 个人，j 地点这 m 个人又下车了。
        # A[i] = A[i-1] + m ; A[j] = A[j-1] - m
        dp = {}
        for num_passengers, start, end in trips:
            dp[start] = dp.setdefault(start, 0) + num_passengers
            dp[end] = dp.setdefault(end, 0) - num_passengers
        i = 0
        cur = 0
        while dp:
            if i in dp:
                cur += dp.pop(i)
            if cur > capacity:
                return False
            i += 1
        return True


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
