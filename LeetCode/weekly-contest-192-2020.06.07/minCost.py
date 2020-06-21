#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/7 11:49
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


# 下面写上代码块
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp[i][t][n] 前i个房子， 组成 t个街区 第i个房子涂成颜色 n 最小话费
        dp = [[[10 ** 9 for _ in range(n + 1)] for _ in range(target + 1)] for _ in range(m + 1)]
        for y in range(1, n + 1):
            if houses[0] == y:
                dp[1][1][y] = 0
            else:
                dp[1][1][y] = cost[0][y - 1]
        for i in range(2, m + 1):
            for t in range(1, min(i + 1, target + 1)):
                for y in range(1, n + 1):
                    dp[i][t][y] = dp[i - 1][t][y]
                    for yy in range(1, n + 1):
                        if yy != y:
                            dp[i][t][y] = min(dp[i][t][y], dp[i - 1][t - 1][yy])
                    if houses[i - 1] != y:
                        dp[i][t][y] += cost[i - 1][y - 1]
        # for i in dp:
        #     print(i)
        return min(dp[m][target])


houses = [0,2,1,2,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = 5
n = 2
target = 3
rr = Solution().minCost(houses, cost, m, n, target)
print(rr)

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
