#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/15 20:04
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   1219. 黄金矿工 显示英文描述
用户通过次数259
用户尝试次数309
通过次数265
提交次数487
题目难度Medium
你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。

为了使收益最大化，矿工需要按以下规则来开采黄金：

每当矿工进入一个单元，就会收集该单元格中的所有黄金。
矿工每次可以从当前位置向上下左右四个方向走。
每个单元格只能被开采（进入）一次。
不得开采（进入）黄金数目为 0 的单元格。
矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。


示例 1：

输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。
示例 2：

输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
输出：28
解释：
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。


提示：

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
最多 25 个单元格中有黄金。
-------------------------------------------------
"""
import time
from typing import List
import copy

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        gold_ores = []
        golds = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    gold_ores.append((i, j))
        # print(gold_ores)

        def dig_gold(pre_grid,cur_total):
            # print(cur_total,left_ores)
            for direction in directions:
                next_step = (pre_grid[0] + direction[0], pre_grid[1] + direction[1])
                if next_step in gold_ores:
                    gold_ores.remove(next_step)
                    dig_gold(next_step, cur_total + grid[next_step[0]][next_step[1]])
                    gold_ores.append(next_step)
                else:
                    golds.append(cur_total)

        fofo = copy.deepcopy(gold_ores)
        for start_step in fofo:
            gold_ores.remove(start_step)
            dig_gold(start_step, grid[start_step[0]][start_step[1]])
            gold_ores.append(start_step)
            # print(gold_ores)
        # print(golds)
        return max(golds)


grid = [[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,0,0,0,0,0],[3,0,0,20,20,20]]
res = Solution().getMaximumGold(grid)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
