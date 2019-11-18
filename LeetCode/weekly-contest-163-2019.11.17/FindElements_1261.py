#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/17 13:13
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       5264. 在受污染的二叉树中查找元素
    https://leetcode-cn.com/contest/weekly-contest-163/problems/find-elements-in-a-contaminated-binary-tree/
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


class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.root.val = 0
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left:
                node.left.val = node.val * 2 + 1
                queue.append(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                queue.append(node.right)

    def find(self, target: int) -> bool:
        res = []
        while target:
            target, b = divmod(target - 1, 2)
            if b:
                res.append(1)
            else:
                res.append(0)
        node = self.root
        for i in res[::-1]:
            if i:
                node = node.right
            else:
                node = node.left
            if not node:
                return False
        return True


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
