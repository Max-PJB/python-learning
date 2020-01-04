#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/1/3 20:31
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = [root]
        tmp = []
        while que:
            for node in que:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if tmp:
                que = tmp
                tmp = []
            else:
                return sum(map(lambda x: x.val, que))
        # visit = 0
        # n = 1
        # while visit < n:
        #     cnt = 0
        #     while visit < n:
        #         node = que[visit]
        #         if node.left:
        #             que.append(node.left)
        #             cnt += 1
        #         if node.right:
        #             que.append(node.right)
        #             cnt += 1
        #         visit += 1
        #     n += cnt
        # pass


root = list_to_tree([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
print(root)
rr = Solution().deepestLeavesSum(root)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
