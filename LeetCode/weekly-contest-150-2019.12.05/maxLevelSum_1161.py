#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/5 21:44
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1161. 最大层内元素和. Maximum Level Sum of a Binary Tree
    https://leetcode-cn.com/contest/weekly-contest-150/problems/maximum-level-sum-of-a-binary-tree/
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        from queue import Queue
        q = Queue()
        cnt = 1
        res = 1
        cur_lv = 1
        sum_max = root.val
        q.put(root)
        while not q.empty():
            tmp_sum = 0
            tmp_cnt = 0
            for _ in range(cnt):
                node = q.get()
                if node.left:
                    tmp_sum += node.left.val
                    tmp_cnt += 1
                    q.put(node.left)
                if node.right:
                    tmp_sum += node.right.val
                    tmp_cnt += 1
                    q.put(node.right)
            if tmp_sum > sum_max:
                sum_max = tmp_sum
                res = cur_lv + 1
            cur_lv += 1
            cnt = tmp_cnt
        return res


lis = [-27745, 27518, 54612, None, 79175, -55310, -38265, None, None, 73079, -42208, 37513, 18112, -73627, None, 91755,
     None, None, -60797, -78407, 29146, 11707, None, None, -42650, -12111, None, -36290, 82890, 60637, 51963, None,
     None, None, None, 83323, None, 78120, None, -61634, -12828, 36784, 53898, -50094, -83697, None, -89871, -28950,
     None, None, None, None, None, None, None, None, -69294, -69762, 65189, 83559, 68085, 41715, None, None, None, None,
     None, -88143, -27856, None, 9949, None, None, 2575, None, None, None, None, None, None, None, None, -6319, -78964,
     None, -43587, -14981, None, None, 84885, 84898, None, None, -2467, -95751]
rt = list_to_tree(lis)
rr = Solution().maxLevelSum(rt)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
