#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/13 12:58
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
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        pre = [triangle[0][0]]
        for i in range(1, n):
            nodes = triangle[i]
            tmp = [pre[0] + nodes[0]]
            for j in range(1, len(nodes) - 1):
                tmp.append(min(pre[j], pre[j - 1]) + nodes[j])
            tmp.append(pre[- 1] + nodes[-1])
            pre = tmp
        return min(pre)


inin = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
rr = Solution().minimumTotal(inin)
print(rr)

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
