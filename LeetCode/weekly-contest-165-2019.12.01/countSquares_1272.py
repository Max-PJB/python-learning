#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/1 11:53
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       统计全为 1 的正方形子矩阵 Count Square Submatrices with All Ones
    https://leetcode-cn.com/contest/weekly-contest-165/problems/count-square-submatrices-with-all-ones/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    dp[1].append((i, j))
        i = 2
        while dp[i - 1] and i <= n:
            for k, l in dp[i - 1]:
                if k > 0 and l > 0:
                    flag = 1
                    for j in range(i):
                        if not matrix[k - 1][l - 1 + j] or not matrix[k - 1 + j][l - 1]:
                            flag = 0
                            break
                    if flag:
                        dp[i].append((k - 1, l - 1))
            i += 1
        print(dp)
        res = 0
        for i in dp:
            res += len(i)
        return res


matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
rr = Solution().countSquares(matrix)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
