#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/1/6 11:39
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
import collections

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
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        r = []
        global k
        k = 0

        def bfs(node):
            """
            :param node:TreeNode
            :return:
            """
            # if not root:
            #     return True
            global k
            if k == len(voyage):
                return True
            if node is None:
                return True
            if node.val != voyage[k]:
                return False
            k += 1
            if not node.left:
                return bfs(node.right)
            if not node.right:
                return bfs(node.left)
            if node.left.val == voyage[k]:
                return bfs(node.left) and bfs(node.right)
            else:
                r.append(node.val)
                return bfs(node.right) and bfs(node.left)

        if bfs(root):
            return r
        else:
            return [-1]


root = TreeNode(1)
# root.right = TreeNode(6)
# root.right.left = TreeNode(7)
# root.right.left.left = TreeNode(8)
# root.right.left.right = TreeNode(9)
# root.right.left.right.left = TreeNode(10)
# root.right.left.right.right = TreeNode(11)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.right = TreeNode(4)
# root.left.right.right = TreeNode(5)
# root.left.left = TreeNode(3)
res = Solution().flipMatchVoyage(root, [1, 3, 2])
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
