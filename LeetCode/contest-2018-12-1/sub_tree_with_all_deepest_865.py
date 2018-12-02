#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/1 14:12
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   865. 具有所有最深结点的最小子树

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Medium

给定一个根为 root 的二叉树，每个结点的深度是它到根的最短距离。

如果一个结点在整个树的任意结点之间具有最大的深度，则该结点是最深的。

一个结点的子树是该结点加上它的所有后代的集合。

返回能满足“以该结点为根的子树中包含所有最深的结点”这一条件的具有最大深度的结点。



示例：

输入：[3,5,1,6,2,0,8,null,null,7,4]
输出：[2,7,4]
解释：

我们返回值为 2 的结点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的结点。
输入 "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" 是对给定的树的序列化表述。
输出 "[2, 7, 4]" 是对根结点的值为 2 的子树的序列化表述。
输入和输出都具有 TreeNode 类型。



提示：

    树中结点的数量介于 1 和 500 之间。
    每个结点的值都是独一无二的。
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
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 经过我的分析，这是一个求左右子树深度的问题，
        # 1.左右子树深度相等，那这个点就是所求的点了
        # 2.左右子树深度不等，那就访问深度大的点，循环
        node_left_right_deep = {}

        def deep_tag(node):
            """
            :param node:TreeNode
            :return: Noe
            """
            node_left = 0
            node_right = 0
            if node.left:
                node_left = deep_tag(node.left)
            if node.right:
                node_right = deep_tag(node.right)
            node_left_right_deep[node] = {"left":node_left, "right":node_right}
            return max(node_left, node_right) + 1

        deep_tag(root)
        # print(node_left_right_deep.items())
        # print(list(map(lambda x: (x[0].val, x[1]["left"], x[1]["right"]), node_left_right_deep.items())))
        while node_left_right_deep[root]["left"] != node_left_right_deep[root]["right"]:
            if node_left_right_deep[root]["left"] > node_left_right_deep[root]["right"]:
                root = root.left
            else:
                root = root.right
        return root


root = TreeNode(3)
root.right = TreeNode(1)
root.right.right = TreeNode(8)
root.right.left = TreeNode(0)
root.left = TreeNode(5)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)
root.left.left = TreeNode(6)
res = Solution().subtreeWithAllDeepest(root)
print(res.val)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
