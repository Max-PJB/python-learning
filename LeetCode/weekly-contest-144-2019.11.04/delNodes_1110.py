#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/4 14:15
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1110. 删点成林
    https://leetcode-cn.com/contest/weekly-contest-144/problems/delete-nodes-and-return-forest/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        global res
        res = []

        def have_father(father, l_or_r, node):
            if node:
                if node.val in to_delete:
                    if l_or_r == "left":
                        father.left = None
                    if l_or_r == "right":
                        father.right = None
                    no_father(node.left)
                    no_father(node.right)
                else:
                    have_father(node, "left", node.left)
                    have_father(node, "right", node.right)

        def no_father(node):
            if node:
                if node.val in to_delete:
                    no_father(node.left)
                    no_father(node.right)
                else:
                    res.append(node)
                    have_father(node, "left", node.left)
                    have_father(node, "right", node.right)

        no_father(root)
        return res


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
