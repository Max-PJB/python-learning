#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/16 10:27
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   957. N 天后的牢房

    用户通过次数 99
    用户尝试次数 187
    通过次数 102
    提交次数 516
    题目难度 Medium

8 间牢房排成一排，每间牢房不是有人住就是空着。

每天，无论牢房是被占用或空置，都会根据以下规则进行更改：

    如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。
    否则，它就会被空置。

（请注意，由于监狱中的牢房排成一行，所以行中的第一个和最后一个房间无法有两个相邻的房间。）

我们用以下方式描述监狱的当前状态：如果第 i 间牢房被占用，则 cell[i]==1，否则 cell[i]==0。

根据监狱的初始状态，在 N 天后返回监狱的状况（和上述 N 种变化）。



示例 1：

输入：cells = [0,1,0,1,1,0,0,1], N = 7
输出：[0,0,1,1,0,0,0,0]
解释：
下表概述了监狱每天的状况：
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

示例 2：

输入：cells = [1,0,0,1,0,0,1,0], N = 1000000000
输出：[0,0,1,1,1,1,1,0]



提示：

    cells.length == 8
    cells[i] 的值为 0 或 1
    1 <= N <= 10^9
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N == 0:
            return cells
        circle = {}
        circle_l = []
        cnt = 0
        xunhuan = None
        last = cells
        M = N
        while N > 0:
            ls = [0, 0]
            cnt += 1
            for i in range(1, 7):
                if last[i - 1] == last[i + 1]:
                    ls.insert(i, 1)
                else:
                    ls.insert(i, 0)
            last = ls
            keyset = tuple(ls)
            if keyset in circle:
                cir = circle[keyset]
                xunhuan = (cir, cnt - 1)
                break
            else:
                circle[keyset] = cnt
                circle_l.append(last)
            N -= 1
        if N == 0:
            return last
        else:
            return circle_l[(M - 1) % (xunhuan[1] - xunhuan[0] + 1)]


# cell_in = [0, 1, 0, 1, 1, 0, 0, 1]
# N_in = 7
cell_in = cells = [1, 0, 0, 1, 0, 0, 1, 0]
N_in = 1000000000
res = Solution().prisonAfterNDays(cell_in, N_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
