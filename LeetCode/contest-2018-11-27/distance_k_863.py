#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/27 12:23
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   二叉树中所有距离为 K 的结点

    虚拟 用户通过次数 24
    虚拟 用户尝试次数 44
    虚拟 通过次数 24
    虚拟 提交次数 44
    题目难度 Medium

给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。



示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

输出：[7,4,1]

解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1



注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。



提示：

    给定的树是非空的，且最多有 K 个结点。
    树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
    目标结点 target 是树上的结点。
    0 <= K <= 1000.
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        def dfs(path):
            # for i in path:
            #     print(i.val, end=" ")
            # print("")
            """
            :param path: List[TreeNode]
            :param targ: TreeNode
            :return: List[TreeNode]
            """
            if path[-1] == target:
                return path
            a = []
            b = []
            if path[-1].left:
                a = dfs(path+[path[-1].left])
            if path[-1].right:
                b = dfs(path+[path[-1].right])
            return a or b

        road = dfs([root])
        # print(road)
        global res
        res = []

        def child_k(node, n):
            """
            :param node:TreeNode
            :param n: int
            :return: None
            """
            global res
            if n == K:
                res.append(node.val)
            if node.left and node.left not in road:
                child_k(node.left, n+1)
            if node.right and node.right not in road:
                child_k(node.right, n+1)

        for i, nod in enumerate(road[::-1]):
            child_k(nod, i)
        return res


root = TreeNode(3)
root.right = TreeNode(1)
root.right.right = TreeNode(8)
root.right.left = TreeNode(0)
root.left = TreeNode(5)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)
root.left.left = TreeNode(6)
target = root.left
k = 2
res = Solution().distanceK(root, target, k)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
