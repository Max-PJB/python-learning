#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/16 10:34
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  897. 递增顺序查找树 显示英文描述
用户通过次数82
用户尝试次数208
通过次数82
提交次数591
题目难度Easy
给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。



示例 ：

输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9


提示：

给定树中的结点数介于 1 和 100 之间。
每个结点都有一个从 0 到 1000 范围内的唯一整数值。
-------------------------------------------------
"""
import time
from typing import List
import queue

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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        res = []
        tmp = root
        while tmp or stack:
            if tmp:
                stack.append(tmp)
                tmp = tmp.left
            elif stack:
                tmp = stack.pop()
                res.append(tmp)
                tmp = tmp.right
        for i in range(len(res)-1):
            res[i].left = None
            res[i].right = res[i+1]
        return res[0]

    def increasingBST2(self, root: TreeNode) -> TreeNode:
        stack = queue.LifoQueue()
        new_root = TreeNode(0)
        new_pre = new_root

        while root or not stack.empty():
            if root:
                stack.put(root)
                root = root.left
            else:
                root = stack.get()
                new_pre.left = None
                new_pre.right = root
                new_pre = root
                root = root.right
        return new_root.right


root2 = TreeNode(379)
root2.left = TreeNode(826)
res = Solution().increasingBST(root2)
while res:
    print(res.val, "-->", end=" ")
    res = res.right
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
