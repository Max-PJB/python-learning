#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/22 21:42
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。


说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7

返回它的最大深度 3 。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(node):
            """
            :type node: TreeNode
            :rtype: int
            """
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        return depth(root)
        # if not root:
        #     return 0
        #
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
root.left.right = TreeNode(3)
res = Solution().maxDepth(root)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
