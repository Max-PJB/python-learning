#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/30 15:57
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :      1014. 最佳观光组合
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max_remainder = 0
        j = 1
        # dp[j] 表示以第j个元素结尾的最佳组合，以0 结尾给个默认值是 0
        dp = [0]
        while j < len(A):
            # 每多前进一格，前面的值就相当于全减少1，这里我们只保存最大的一个，命名为余量。
            max_remainder = max(max_remainder - 1, A[j - 1] - 1)
            dp.append(max_remainder + A[j])
            j += 1
        return max(dp)


aa = [8, 1, 5, 2, 6]
res = Solution().maxScoreSightseeingPair(aa)
print(res)

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
