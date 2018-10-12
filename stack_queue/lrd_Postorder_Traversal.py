#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/23 22:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lrd(root):
    ls = []
    ans = []
    pre = None
    while root or len(ls) > 0:
        if root:
            ls.append(root)
            root = root.left
        else:
            root = ls[-1]
            if root.right and root.right != pre:
                root = root.right
            else:
                ls.pop()
                ans.append(root.val)
                pre = root
                root = None
    return ans


