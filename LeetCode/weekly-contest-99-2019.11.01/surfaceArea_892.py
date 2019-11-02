#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/1 14:24
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       892. 三维形体的表面积
    https://leetcode-cn.com/contest/weekly-contest-99/problems/surface-area-of-3d-shapes/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res = 0
        N = len(grid)
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                v = grid[x][y]
                if v > 0:
                    res += 4 * v + 2
                if x + 1 < N:
                    res -= min(v, grid[x + 1][y])
                if x - 1 >= 0:
                    res -= min(v, grid[x - 1][y])
                if y + 1 < N:
                    res -= min(v, grid[x][y + 1])
                if y - 1 >= 0:
                    res -= min(v, grid[x][y - 1])
                # print(res)
        return res


aa = [[2,2,2],[2,1,2],[2,2,2]]
res = Solution().surfaceArea(aa)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
