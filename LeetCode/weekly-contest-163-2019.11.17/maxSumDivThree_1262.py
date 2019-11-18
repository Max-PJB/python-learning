#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/18 13:26
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1262. 可被三整除的最大和
    https://leetcode-cn.com/contest/weekly-contest-163/problems/greatest-sum-divisible-by-three/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        res = 0
        remain_1 = []
        remain_2 = []
        for num in nums:
            if num % 3 == 1:
                remain_1.append(num)
            elif num % 3 == 2:
                remain_2.append(num)
            res += num
        len1 = len(remain_1)
        len2 = len(remain_2)
        k = len1 % 3 - len2 % 3
        if k < 0:
            longer = sorted(remain_2)
            shorter = sorted(remain_1)
        elif k > 0:
            longer = sorted(remain_1)
            shorter = sorted(remain_2)
        else:
            return res
        print(longer, shorter)
        if len(shorter) >= 3:
            if sum(longer[0:abs(k)]) - sum(shorter[0:3 - abs(k)]) > 0:
                return res - sum(shorter[0:3 - abs(k)])
            else:
                return res - sum(longer[0:abs(k)])
        else:
            return res - sum(longer[0:abs(k)])


nums = [4]
rr = Solution().maxSumDivThree(nums)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
