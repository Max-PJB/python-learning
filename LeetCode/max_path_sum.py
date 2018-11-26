#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/22 22:25
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    二叉树中的最大路径和

给定一个非空二叉树，返回其最大路径和。给你一个二叉树，求出一条和最大的路径,经过的节点的值相加最大的一条路径

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6

示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42


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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_sum(node):
            """
            :type node: TreeNode
            :rtype: int, int
            """
            if not node:
                return None, None
            left_over, left = max_sum(node.left)
            right_over, right = max_sum(node.right)
            a = max(filter(lambda x: isinstance(x, int), (
                left, right, left_over, right_over,
                sum(filter(lambda x: isinstance(x, int), (node.val, left, right))))))
            b = node.val + max(filter(lambda x: isinstance(x, int), (0, left, right)))
            return a, b

        return max(max_sum(root))
        # return max_sum(root)
        # 上面中间写上代码块


root = TreeNode(-2)
# root.left = TreeNode(6)
root.right = TreeNode(6)
root.right.right = TreeNode(0)
root.right.left = TreeNode(-6)
res = Solution().maxPathSum(root)
print(res)
end = time.time()
print('Running time: %s Seconds' % (end - start))
