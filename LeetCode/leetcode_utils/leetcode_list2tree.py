#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengjb
    @   date    :       2019/12/5 22:13
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       leetcode 上面涉及的关于树的操作的题的时候，一般输入的树形状是一个 List[int],如 [1,7,0,7,-8,None,None]
    我现在要写一个工具，输入一个list[int]，返回一个 root ，给我生成测试用例
    他的结构是，类广度优先序列，非None节点的左右子节点都是加入到list，而None节点，就不加入到list了

-------------------------------------------------
"""

__author__ = 'Max_Pengjb'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs(r: TreeNode):
    from queue import Queue
    que = Queue()
    que.put(r)
    res = []
    while not que.empty():
        r = que.get()
        res.append(r.val)
        if r.left:
            que.put(r.left)
        if r.right:
            que.put(r.right)
    return res


def dlr(r: TreeNode):
    if r:
        print(r.val)
    if r.left:
        dlr(r.left)
    if r.right:
        dlr(r.right)


def list_to_tree(S: list) -> TreeNode:
    """
    :param L:
    :return:
    """
    L = [TreeNode(val) if val is not None else None for val in S]
    # print(L)
    tmp_list = [L[0]]
    cursor = 1
    N = len(L)
    while tmp_list:
        n = len(tmp_list)
        next_cursor = cursor + n * 2
        for i, node in enumerate(tmp_list):
            # print(list(map(lambda x: x.val, tmp_list)), "->", S[cursor:next_cursor])
            # print(i, node.val)
            if cursor + 2 * i < N:
                node.left = L[cursor + 2 * i]
            if cursor + 2 * i + 1 < N:
                node.right = L[cursor + 2 * i + 1]
        tmp_list = list(filter(lambda x: x, L[cursor:next_cursor]))
        cursor = next_cursor
    return L[0]


def tree_to_list(root: TreeNode) -> list:
    """
    :param root:TreeNode
    :return:List
    """
    from queue import Queue
    res = []
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        if node:
            res.append(node.val)
            queue.put(node.left)
            queue.put(node.right)
        else:
            res.append(None)
    while res[-1] is None:
        res.pop()
    return res


lis = [-27745, 27518, 54612, None, 79175, -55310, -38265, None, None, 73079, -42208, 37513, 18112, -73627, None, 91755,
       None, None, -60797, -78407, 29146, 11707, None, None, -42650, -12111, None, -36290, 82890, 60637, 51963, None,
       None, None, None, 83323, None, 78120, None, -61634, -12828, 36784, 53898, -50094, -83697, None, -89871, -28950,
       None, None, None, None, None, None, None, None, -69294, -69762, 65189, 83559, 68085, 41715, None, None, None,
       None,
       None, -88143, -27856, None, 9949, None, None, 2575, None, None, None, None, None, None, None, None, -6319,
       -78964,
       None, -43587, -14981, None, None, 84885, 84898, None, None, -2467, -95751]
# lis = [-27745, 27518, 54612, None, 79175, -55310, -38265]
# t = list_to_tree(lis)
# n = tree_to_list(t)
# print(n)
# print(len(n),len(lis))
# k = bfs(t)
# print(len(k), k)
# kk = list(filter(lambda x: x, lis))
# print(len(kk), kk)
# print(t.val)
# print(t.left.val)
# print(t.right.val)
