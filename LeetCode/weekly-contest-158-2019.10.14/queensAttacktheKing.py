#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/14 9:27
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    5223. 可以攻击国王的皇后 显示英文描述
    https://leetcode-cn.com/contest/weekly-contest-158/problems/queens-that-can-attack-the-king/
用户通过次数708
用户尝试次数779
通过次数709
提交次数1178
题目难度Medium
在一个 8x8 的棋盘上，放置着若干「黑皇后」和一个「白国王」。

「黑皇后」在棋盘上的位置分布用整数坐标数组 queens 表示，「白国王」的坐标用数组 king 表示。

「黑皇后」的行棋规定是：横、直、斜都可以走，步数不受限制，但是，不能越子行棋。

请你返回可以直接攻击到「白国王」的所有「黑皇后」的坐标（任意顺序）。



示例 1：



输入：queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
输出：[[0,1],[1,0],[3,3]]
解释：
[0,1] 的皇后可以攻击到国王，因为他们在同一行上。
[1,0] 的皇后可以攻击到国王，因为他们在同一列上。
[3,3] 的皇后可以攻击到国王，因为他们在同一条对角线上。
[0,4] 的皇后无法攻击到国王，因为她被位于 [0,1] 的皇后挡住了。
[4,0] 的皇后无法攻击到国王，因为她被位于 [1,0] 的皇后挡住了。
[2,4] 的皇后无法攻击到国王，因为她和国王不在同一行/列/对角线上。
示例 2：



输入：queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
输出：[[2,2],[3,4],[4,4]]
示例 3：



输入：queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
输出：[[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]


提示：

1 <= queens.length <= 63
queens[0].length == 2
0 <= queens[i][j] < 8
king.length == 2
0 <= king[0], king[1] < 8
一个棋盘格上最多只能放置一枚棋子。
-------------------------------------------------
"""
import time
from typing import List
import copy

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        res = []
        for direction in directions:
            hit = copy.deepcopy(king)
            print(king)
            while hit not in queens:
                hit[0] = hit[0] + direction[0]
                hit[1] = hit[1] + direction[1]
                if hit[0] < 0 or hit[0] > 7 or hit[1] < 0 or hit[1] > 7:
                    break
            if hit in queens:
                res.append(hit)
        return res


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))

queens = [[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4],
          [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2],
          [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]]
king = [3, 4]
rr = Solution().queensAttacktheKing(queens, king)
print(rr)
