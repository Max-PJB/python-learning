#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/19 10:27
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
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        z_l = []
        for i, g in enumerate(grid):
            k = 0
            for j in range(n - 1, -1, -1):
                if g[j] == 0:
                    k += 1
                else:
                    break
            z_l.append(k)
        res = 0
        for need in range(n - 1, -1, -1):
            flag = False
            for i, k in enumerate(z_l):
                if need <= k:
                    res += i
                    z_l.pop(i)
                    flag = True
                    break
            if not flag:
                return -1
        return res


grid = [[1,0,0],[1,1,0],[1,1,1]]
rr = Solution().minSwaps(grid)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
