#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/10 18:45
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  840. 矩阵中的幻方

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Easy

3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。

给定一个由整数组成的 N × N 矩阵，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。



示例 1:

输入: [[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]]
输出: 1
解释:
下面的子矩阵是一个 3 x 3 的幻方：
438
951
276

而这一个不是：
384
519
762

总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。

提示:

    1 <= grid.length = grid[0].length <= 10
    0 <= grid[i][j] <= 15
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return 0

        def is_magic(x, y):
            Ma = 15
            ll = []
            for i in range(3):
                for j in range(3):
                    if grid[x+i][y+j] < 1 or grid[x+i][y+j] > 9:
                        ll.append(grid[x+i][y+j])
                        return False
            if len(ll) != len(set(ll)):
                return False
            if Ma != grid[x][y] + grid[x + 1][y + 1] + grid[x + 2][y + 2] or Ma != grid[x + 2][y] + grid[x + 1][y + 1] + grid[x][y + 2]:
                return False
            for i in range(3):
                if Ma != grid[x + i][y] + grid[x + i][y + 1] + grid[x + i][y + 2] or Ma != grid[x][y + i] + grid[x + 1][y + i] + grid[x + 2][y + i]:
                    return False
            return True

        cnt = 0
        for i in range(n - 2):
            for j in range(m - 2):
                if is_magic(i, j):
                    cnt += 1
        return cnt


# grid_in = [[4, 3, 8, 4],[9, 5, 1, 9],[2, 7, 6, 2]]
grid_in = [[1,8,6],[10,5,0],[4,2,9]]
res = Solution().numMagicSquaresInside(grid_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
