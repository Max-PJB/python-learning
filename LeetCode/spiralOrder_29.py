#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/5 22:14
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


# 下面写上代码块
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return [] if not matrix else list(matrix[0]) + self.spiralOrder(list(zip(*matrix[1:]))[::-1])
        # res = []
        # def haha(mat, row=0, reverse=False):
        #     nonlocal res
        #     if mat:
        #         if row == 0 and not reverse:
        #             res += mat[0]
        #             haha(list(zip(*mat[1:])), -1, False)
        #         elif row == -1 and not reverse:
        #             res += mat[-1]
        #             haha(list(zip(*mat[:-1])), -1, True)
        #         elif row == -1 and reverse:
        #             res += mat[-1][::-1]
        #             haha(list(zip(*mat[:-1])), 0, True)
        #         elif row == 0 and reverse:
        #             res += mat[0][::-1]
        #             haha(list(zip(*mat[1:])), 0, False)

        # haha(matrix, 0, False)

        # def haha2(mat):
        #     nonlocal res
        #     if mat:
        #         res += mat[0]
        #         print(type(mat),type(mat[0]))
        #         haha2(list(zip(*list(map(lambda x: x[::-1], mat[1:])))))

        # haha2(matrix)
        # return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rr = Solution().spiralOrder(matrix)
print(rr)
# 上面中间写上代码块


end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
