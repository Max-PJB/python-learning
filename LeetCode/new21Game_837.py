#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/3 13:44
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


# https://leetcode-cn.com/problems/new-21-game/solution/xin-21dian-by-leetcode-solution/
# 看看人家状态定义的多棒啊
# 下面写上代码块
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # 我这个方法很蠢，下面链接是别人的方法，状态定义好啊
        # https://leetcode-cn.com/problems/new-21-game/solution/huan-you-bi-zhe-geng-jian-dan-de-ti-jie-ma-tian-ge/
        p = [1 / W if 0 < i <= W else 0.0 for i in range(max(W, N) + 1)]
        # dp[i][j] 表示第 i 次结果是 j 的概率 i=1,2,3……N， N>=j>=i
        dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        dp[1][1:N + 1] = p[1:N + 1]
        for i in range(2, N + 1):
            for j in range(i, N + 1):
                for k in range(1, j):
                    if j - k < K and k < K:
                        dp[i][j] += dp[i - 1][j - k] * dp[1][k]
        import numpy as np
        for d in dp:
            print(d)
        print(np.sum(np.array(dp)))


N = 6
K = 1
W = 10
rr = Solution().new21Game(N, K, W)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
