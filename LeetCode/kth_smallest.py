#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/15 18:53
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    二叉搜索树中第K小的元素

给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1

示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3

进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
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


def deep_search(node, n, k):
    """
    :type node: TreeNode
    :type k: int
    :rtype: (int,int)
    """
    if node.left:
        x, n = deep_search(node.left, n, k)
        if n == k:
            return x, n
    x, n = node.val, n + 1
    if n == k:
        return x, n
    if node.right:
        x, n = deep_search(node.right, n, k)
        if n == k:
            return x, n
    return x, n


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        x, n = deep_search(root, 0, k)
        return x


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.right = TreeNode(3)
res = Solution().kthSmallest(root, 3)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
