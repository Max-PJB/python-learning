#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/2 11:40
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   951. 翻转等价二叉树

    用户通过次数 81
    用户尝试次数 93
    通过次数 81
    提交次数 179
    题目难度 Medium

我们可以为二叉树 T 定义一个翻转操作，如下所示：选择任意节点，然后交换它的左子树和右子树。

只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X 翻转等价于二叉树 Y。

编写一个判断两个二叉树是否是翻转等价的函数。这些树由根节点 root1 和 root2 给出。



示例：

输入：root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
输出：true
解释：We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram



提示：

    每棵树最多有 100 个节点。
    每棵树中的每个值都是唯一的、在 [0, 99] 范围内的整数。
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


class Solution(object):
    def flipEquiv2(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # que1 = queue.Queue()
        # que2 = queue.Queue()
        que1 = []
        que2 = []
        if root1.val != root2.val:
            return False
        que1.append(root1)
        que2.append(root2)
        while que1 and que2:
            node1 = que1.pop(0)
            node2 = que2.pop(0)
            left1 = None if not node1.left else node1.left.val
            right1 = None if not node1.right else node1.right.val
            left2 = None if not node2.left else node2.left.val
            right2 = None if not node2.right else node2.right.val
            if left1 == left2 and right1 == right2:
                if node1.left:
                    que1.append(node1.left)
                    que2.append(node2.left)
                if node1.right:
                    que1.append(node1.right)
                    que2.append(node2.right)
            elif left1 == right2 and right1 == left2:
                if node1.left:
                    que1.append(node1.left)
                    que2.append(node2.right)
                if node1.right:
                    que1.append(node1.right)
                    que2.append(node2.left)
            else:
                return False
        return True

    # 别人的方法
    def flipEquiv(self, root1, root2):
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))


# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
