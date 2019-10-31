#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/31 13:47
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       919. 完全二叉树插入器
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


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.q = [root]
        i = 0
        while i < len(self.q):
            if self.q[i].left:
                self.q.append(self.q[i].left)
            if self.q[i].right:
                self.q.append(self.q[i].right)
            # (i - 1) // 2 是父节点的下标
            if (i - 1) // 2 >= 0:
                # 自己的下标是奇数就是左节点，偶数就是右节点
                if i % 2 == 0:  # 偶数，右子节点
                    self.q[(i - 1) // 2].right = self.q[i]
                else:
                    self.q[(i - 1) // 2].left = self.q[i]
            i += 1

        print(list(map(lambda x: x.val, self.q)))

    def insert(self, v: int) -> int:
        self.q.append(TreeNode(v))
        length = len(self.q)
        # 总长度n是偶数，那么插入的值的下标 n-1 就是奇数，奇数的话，就是父节点的左子节点
        if length % 2 == 0:
            self.q[length // 2 - 1].left = self.q[length - 1]
        else:
            self.q[length // 2 - 1].right = self.q[length - 1]
        return self.q[length // 2 - 1].val

    def get_root(self) -> TreeNode:
        print(list(map(lambda x: x.val, self.q)))

        return self.q[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

obj = CBTInserter(root)
param_1 = obj.insert(7)
print(param_1)
param_2 = obj.insert(8)
print(param_2)
res = obj.get_root()
print(res.left.val)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
