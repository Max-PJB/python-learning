#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/24 14:08
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       5271. 访问所有点的最小时间 Minimum Time Visiting All Points
    https://leetcode-cn.com/contest/weekly-contest-164/problems/minimum-time-visiting-all-points/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        visited = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]
        x, y = points[0]
        visited[x][y] = 1
        res = 0
        for i, j in points[1:]:
            print(max(abs(i - x), abs(j - y)))
            res += max(abs(i - x), abs(j - y))
            x,y = i,j
        return res


inin = [[1, 1], [3, 4], [-1, 0]]
rr = Solution().minTimeToVisitAllPoints(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
