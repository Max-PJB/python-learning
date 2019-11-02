#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/2 14:16
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :     894. 所有可能的满二叉树
    https://leetcode-cn.com/contest/weekly-contest-99/problems/all-possible-full-binary-trees/
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


"""
公式：
n(i) 表示 有 n 个子节点的节点数量，即出度为i的节点
n0 = n2 + n3 * 2 + n4 * 3 + ………… + ni*（i-1) + 1
所以，当 是二叉树时，n0 = n2 + 1；若要使满二叉树，则 n1 = 0； 故而 N = n0 + n2 = 2n2 + 1，N必须是奇数 odd，uneven number

这里别人用的是分治法， D[n] = 左边D[2i+1] * 右边 D[n-2i-1-1]；左边有 x 种情况，右边有 y 种情况，他们的组合
class Solution:
    N_dict = {1:[TreeNode(0)]}
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N in self.N_dict:
            return self.N_dict[N]      

        res = []
        for i in range(1,N-1,2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-1-i)
            for i_l in left:
                for i_r in right:
                    root = TreeNode(0)
                    root.left = i_l
                    root.right = i_r
                    res.append(root)
        self.N_dict[N] = res
        return self.N_dict[N]
"""


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        if N == 3:
            root = TreeNode(0)
            root.left = TreeNode(0)
            root.right = TreeNode(0)
            return [root]
        # 其实就相当于，每两个节点一加，一次满二叉树的寻找共需要进行 (N-3)//2 次节点添加的选择
        # 可以记录中间状态，因为中间可能会重合，如果重合了，那就不做了。
        # 以 [0,1,2] 表示 0 1 2 位置上有元素。
        # 一个节点的序号是 x 那他的两个叶子节点的序号是 2x+1， 2x+2
        res = [[0, 1, 2]]
        for _ in range((N - 3) // 2):
            print("1111", res)
            tmp = []
            for situation in res:
                print("2222", situation)
                for i in situation:
                    # 如果 2*i+1 in situation，这个点不是根节点，我们不能再这个点后面加节点
                    if 2 * i + 1 not in situation:
                        tt = sorted(situation + [i * 2 + 1, i * 2 + 2])
                        if tt not in tmp:
                            tmp.append(tt)
            print("333", tmp)
            res = tmp
        res_res = []
        for L in res:
            tmp = [TreeNode(0) for _ in L]
            res_res.append(tmp[0])
            for j, node in zip(L, tmp):
                if j * 2 + 1 in L:
                    print(j * 2 + 1, L)
                    node.left = tmp[L.index(j * 2 + 1)]
                    node.right = tmp[L.index(j * 2 + 2)]
        return res_res
        # print(len(res), res)


rrr = Solution().allPossibleFBT(7)
print(rrr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
