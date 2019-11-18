#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/18 14:19
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1263. 推箱子 Minimum Moves to Move a Box to Their Target Location
    https://leetcode-cn.com/contest/weekly-contest-163/problems/minimum-moves-to-move-a-box-to-their-target-location/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    # TODO 不会做 https://leetcode-cn.com/problems/minimum-moves-to-move-a-box-to-their-target-location/solution/py3-by-mao1112-13/
    def minPushBox(self, grid: List[List[str]]) -> int:
        T, B, S = (), (), ()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "T":
                    T = (i, j)
                if grid[i][j] == "B":
                    B = (i, j)
                if grid[i][j] == "S":
                    S = (i, j)
        print(T, B, S)

        def next_step():
            pass

        pass


inin = grid = [["#", "#", "#", "#", "#", "#"],
               ["#", "T", "#", "#", "#", "#"],
               ["#", ".", ".", "B", ".", "#"],
               ["#", ".", "#", "#", ".", "#"],
               ["#", ".", ".", ".", "S", "#"],
               ["#", "#", "#", "#", "#", "#"]]
rr = Solution().minPushBox(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
