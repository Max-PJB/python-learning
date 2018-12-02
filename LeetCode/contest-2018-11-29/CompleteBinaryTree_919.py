#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/30 15:55
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 919. 完全二叉树插入器

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Medium

完全二叉树是每一层（除最后一层外）都是完全填充（即，结点数达到最大）的，并且所有的结点都尽可能地集中在左侧。

设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：

    CBTInserter(TreeNode root) 使用头结点为 root 的给定树初始化该数据结构；
    CBTInserter.insert(int v) 将 TreeNode 插入到存在值为 node.val = v  的树中以使其保持完全二叉树的状态，并返回插入的 TreeNode 的父结点的值；
    CBTInserter.get_root() 将返回树的头结点。



示例 1：

输入：inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
输出：[null,1,[1,2]]

示例 2：

输入：inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
输出：[null,3,4,[1,2,3,4,5,6,7,8]]



提示：

    最初给定的树是完全二叉树，且包含 1 到 1000 个结点。
    每个测试用例最多调用 CBTInserter.insert  操作 10000 次。
    给定结点或插入结点的每个值都在 0 到 5000 之间。
-------------------------------------------------
"""
import time
import queue

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = [root]
        for node in self.nodes:
            if node.left:
                self.nodes.append(node.left)
            if node.right:
                self.nodes.append(node.right)
        self.length = len(self.nodes)
        # print(list(map(lambda x: x.val, self.nodes)))

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        self.length += 1
        self.nodes.append(v)
        parent = self.nodes[self.length//2 - 1]
        if self.length % 2 == 0:
            parent.right = v
        else:
            parent.left = v
        return parent

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes[0]


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
cbt = CBTInserter(root)
# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
