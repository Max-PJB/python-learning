#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/19 16:26
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       962. 最大宽度坡 Maximum Width Ramp
    https://leetcode-cn.com/contest/weekly-contest-116/problems/maximum-width-ramp/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # 单调数组
        monotonous = [0]
        res = 0
        for i, a in enumerate(A):
            if a < A[monotonous[-1]]:
                monotonous.append(i)
            else:
                k = len(monotonous) - 1
                while k >= 0 and a >= A[monotonous[k]]:
                    res = max(res, i - monotonous[k])
                    k -= 1
        return res


inin = [2,4,1,3]
rr = Solution().maxWidthRamp(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
