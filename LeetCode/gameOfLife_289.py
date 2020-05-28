#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/5/26 18:54
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


# https://leetcode-cn.com/problems/game-of-life/solution/xiong-mao-shua-ti-python3-bao-xue-bao-hui-cvzhong-/
# 下面写上代码块
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import numpy as np
        boad_ = np.array(board)
        n = len(board)
        m = len(board[0])
        expired_board = np.zeros((n + 2, m + 2))
        expired_board[1:n + 1, 1:m + 1] = boad_
        # print(expired_board)
        # aa = np.copy(expired_board)
        kernel = np.ones((3, 3))
        kernel[1][1] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                lives = np.sum(kernel * expired_board[i - 1:i + 2, j - 1:j + 2])
                cur = expired_board[i][j]
                if cur:
                    if lives < 2 or lives > 3:
                        board[i - 1][j - 1] = 0
                else:
                    if lives == 3:
                        board[i - 1][j - 1] = 1
        # print(expired_board==aa)
        return board


a = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]
rr = Solution().gameOfLife(a)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
