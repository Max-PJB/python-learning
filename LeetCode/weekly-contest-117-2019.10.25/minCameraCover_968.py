#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/28 19:29
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
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


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 最优的策略
        # 1.每一个叶子节点的父节点装一个 摄像头
        # 2.把能拍的节点不作为树节点。然后再找叶子节点，进行步骤 （1）
        nodes = [root]
        # 节点 -> 父节点 映射
        father = {}
        i = 0
        while i < len(nodes):
            if nodes[i].left:
                nodes.append(nodes[i].left)
                father[nodes[i].left] = nodes[i]
            if nodes[i].right:
                nodes.append(nodes[i].right)
                father[nodes[i].right] = nodes[i]
            i += 1
        # 初始化。都没被摄像头拍照
        visited = {}
        k = 0
        # 逆序，保证每一个都是删除了被拍到的节点后的树的 叶子节点
        for node in nodes[::-1]:
            # 第2个节点没有访问，说明这个没有被相机拍到，
            if node not in visited:
                # 那就在你的父节点加装一个摄像头，这样 你，你的父亲，你的父亲的父亲，你的父亲的孩子都被照到了，要标记为1
                k += 1
                if node in father:
                    visited[father[node]] = 1
                    if father[node].left:
                        visited[father[node].left] = 1
                    if father[node].right:
                        visited[father[node].right] = 1
                    if father[node] in father:
                        visited[father[father[node]]] = 1
        return k
    # 上面中间写上代码块


root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(0)
root.left.left.left.right = TreeNode(0)

rrr = Solution().minCameraCover(root)
print(rrr)
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
