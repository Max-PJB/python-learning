#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/1 11:09
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       5275. 找出井字棋的获胜者 Find Winner on a Tic Tac Toe Game
    https://leetcode-cn.com/contest/weekly-contest-165/problems/find-winner-on-a-tic-tac-toe-game/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return "Pending"
        A = moves[0::2]
        B = moves[1::2]
        i = 3
        print(A)
        print(B)

        def is_win(C):
            line_0 = list(filter(lambda x: x[0] == 0, C))
            line_1 = list(filter(lambda x: x[0] == 1, C))
            line_2 = list(filter(lambda x: x[0] == 2, C))
            if len(line_0) == 3 or len(line_1) == 3 or len(line_2) == 3:
                return True
            for a in line_0:
                for b in line_1:
                    for c in line_2:
                        if (c[0] - b[0] == b[0] - a[0] and c[1] - b[1] == b[1] - a[1]) or (c[1] == b[1] == a[1]):
                            return True
            return False

        while i < 6:
            if is_win(A[:i]):
                return "A"
            elif is_win(B[:i]):
                return "B"
            i += 1
        if len(moves) == 9:
            return "Draw"
        return "Pending"


inin = [[0,2],[1,0],[2,2],[1,2],[2,0],[0,0],[0,1],[2,1],[1,1]]
rr = Solution().tictactoe(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
