#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/15 20:22
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1020. Number of Enclaves
    https://leetcode-cn.com/problems/number-of-enclaves/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def dfs(k, l):
            if not visited[k][l]:
                visited[k][l] = 1
                if k < n - 2 and A[k + 1][l]:
                    dfs(k + 1, l)
                if k > 1 and A[k - 1][l]:
                    dfs(k - 1, l)
                if l < m - 2 and A[k][l + 1]:
                    dfs(k, l + 1)
                if l > 1 and A[k][l - 1]:
                    dfs(k, l - 1)

        n = len(A)
        m = len(A[0])
        if n < 3 or m < 3:
            return 0
        ok = set()
        for i in range(n):
            if A[i][0]:
                ok.add((i, 0))
            if A[i][m - 1]:
                ok.add((i, m - 1))
        for j in range(m):
            if A[0][j]:
                ok.add((0, j))
            if A[n - 1][j]:
                ok.add((n - 1, j))
        visited = [[0 for _ in range(m)] for _ in range(n)]
        for i, j in ok:
            dfs(i, j)

        return sum(map(sum, A)) - sum(map(sum, visited))


inin = [[0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]]

rr = Solution().numEnclaves(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
