#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/12 10:04
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1250. 检查「好数组」Check If It Is a Good Array
    https://leetcode-cn.com/contest/weekly-contest-161/problems/check-if-it-is-a-good-array/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # 数论：裴蜀定理:
        # 设a1,a2,a3......an为n个整数，d是它们的最大公约数，那么存在整数x1......xn使得x1*a1+x2*a2+...xn*an=d。
        # 特别来说，如果a1...an互质（不是两两互质），那么存在整数x1......xn使得x1*a1+x2*a2+...xn*an=1。

        # 如果数组中存在公因数，则不满足，我们只要求出整个数组的最大公因数就好了
        # 使用 gcd 欧几里得算法
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        tmp = nums[0]
        for i in range(1,len(nums)):
            tmp = gcd(tmp,nums[i])
        if tmp > 1:
            return False
        return True


rr = [6,10,15]
rrr = Solution().isGoodArray(rr)
print(rrr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
