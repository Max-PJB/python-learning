#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/3 14:40
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :      975. 奇偶跳
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        # TODO 大神方法没有看懂 https://leetcode-cn.com/problems/odd-even-jump/solution/qi-ou-tiao-by-leetcode/
        # dp[1/0][index] 表示 在 index位置进行 1 奇数次跳 0 偶数次跳 是否能达到终点
        # 若 A[i] > A[n-1] 只能偶数次到达目标，反之。相等的话直接就 ok 不奇数偶数
        n = len(A)
        dp = [[False for _ in range(n)] for _ in range(2)]
        dp[0][n - 1] = True
        dp[1][n - 1] = True

        for i in range(n - 2, -1,-1):
            # 寻找奇数跳跃的下一个点,在所有大于他的中间找一个小的
            larger = [x for x in A[i + 1:] if x >= A[i]]
            if larger:
                index = A[i+1:].index(min(larger))
                dp[1][i] = dp[0][index+i+1]
            else:
                dp[1][i] = False
            # 寻找偶数次跳跃的下一个点，
            smaller = [x for x in A[i + 1:] if x <= A[i]]
            if smaller:
                index = A[i+1:].index(max(smaller))
                dp[0][i] = dp[1][index+i+1]
            else:
                dp[0][i] = False
        return len([x for x in dp[1] if x])


aa = [10,13,12,14,15]
res = Solution().oddEvenJumps(aa)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
