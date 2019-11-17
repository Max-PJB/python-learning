#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/17 11:35
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       5263. 二维网格迁移
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        a, b = divmod(k, m)
        c = a % n
        if c:
            grid = grid[-c:] + grid[:-c]
        print("ccccccccc", grid)
        # print(grid)
        if b:
            for j in range(b):
                tmp = grid[n - 1][-j - 1]
                for i in range(n):
                    grid[i][-j - 1], tmp = tmp, grid[i][-j - 1]
            grid = list(zip(*grid))
            left = grid[:-b]
            right = grid[-b:]
            res = right + left
            return list(map(list, zip(*res)))
        return grid


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
rr = Solution().shiftGrid(grid, k)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
