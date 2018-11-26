#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/23 12:02
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    二叉树的最近公共祖先

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

说明:

    所有节点的值都是唯一的。
    p、q 为不同节点且均存在于给定的二叉树中。
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def search_road(stack, x):
            """
            :type stack: list[TreeNode]
            :type x: TreeNode
            :rtype: list,boole
            """
            t = stack[-1]
            if t.val == x:
                return stack, True
            if t.left:
                stack.append(t.left)
                stack_left, res_left = search_road(stack, x)
                if res_left:
                    return stack_left, res_left
            if t.right:
                stack.append(t.right)
                stack_right, res_right = search_road(stack, x)
                if res_right:
                    return stack_right, res_right
            stack.pop()
            return stack, False

        pk = list(map(lambda x: x.val, search_road([root], p.val)[0]))
        qk = list(map(lambda x: x.val, search_road([root], q.val)[0]))
        if len(pk) < len(qk):
            pk, qk = qk, pk
        for i in range(len(pk)):
            if pk[i] not in qk:
                return pk[i - 1]


root = TreeNode(3)
root.right = TreeNode(1)
root.right.right = TreeNode(8)
root.right.left = TreeNode(0)
root.left = TreeNode(5)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)
root.left.left = TreeNode(6)
p = TreeNode(5)
q = TreeNode(4)
res = Solution().lowestCommonAncestor(root, p, q)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
