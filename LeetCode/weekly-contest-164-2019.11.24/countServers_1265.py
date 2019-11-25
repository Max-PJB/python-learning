#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/24 14:28
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       5272. 统计参与通信的服务器 Count Servers that Communicate
    https://leetcode-cn.com/contest/weekly-contest-164/problems/count-servers-that-communicate/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # 对每一行、列求和，分别用sumRow和sumCol两个数组来存储，对每个位置，若满足：
        #
        # 当前位置有服务器（grid[i][j] == 1）
        # 同行 / 同列上有其他服务器（sumRow[i] * sumCol[j] >= 2）
        # 则该服务器能够通信。
        import numpy as np
        if not grid:
            return 0
        counter = 0
        sumRow = list(np.sum(grid, axis=1))
        sumCol = list(np.sum(grid, axis=0))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if sumRow[i] * sumCol[j] >= 2 and grid[i][j]:
                    counter += 1
        return counter


inin = [[1, 1], [0, 0]]
rr = Solution().countServers(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
