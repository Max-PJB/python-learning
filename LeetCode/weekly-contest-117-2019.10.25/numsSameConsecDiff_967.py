#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/27 13:49
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   967. 连续差相同的数字
-------------------------------------------------
"""
__author__ = 'Max_Pengjb'

from typing import List
import time

start_time = time.time()


# 下面写上代码块
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        # 其实就是相当于层次遍历,但是我们这里用 dp 方法
        # dp[n][i] = dp[n-1][i-k]+dp[n-1][i+k] 第n个位置为i的话，他拥有的可能数是 第 n-1个位置 为 i-k 和 i+k 的可能的和
        # i-k 或者 i+k 如果不合理那他对应的 dp[n-1][i-k]=0 或者 dp[n-1][i+k] = 0 完成递归
        if N == 1:
            return 10
        dp_pre = [1 for _ in range(10)]
        print(dp_pre)
        for n in range(1, N):
            dp = [0 for _ in range(10)]
            for i in range(10):
                if i + K < 10:
                    dp[i] += dp_pre[i + K]
                if i - K >= 0:
                    dp[i] += dp_pre[i - K]
            dp_pre = dp
        return sum(dp_pre[1:])

    def numsSameConsecDiff2(self, N, K):
        # 要求出所有的数，就需要一个数组来记录结果了
        if N == 1:
            return [i for i in range(10)]
        res = [i for i in range(1, 10)]
        k = 1
        while k < N:
            tmp = []
            for i in res:
                mod = i % 10
                if mod + K < 10:
                    tmp.append(i * 10 + mod + K)
                if mod - K >= 0:
                    tmp.append(i * 10 + mod - K)
            res = set(tmp)
            k += 1
        return res


res = Solution().numsSameConsecDiff2(2, 0)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
