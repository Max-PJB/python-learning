#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/19 10:27
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
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        import queue
        qe = queue.Queue()
        for a in arr:
            qe.put(a)
        c = 0
        s = qe.get()
        while c < k:
            t = qe.get()
            if s > t:
                c += 1
                qe.put(t)
            else:
                c = 1
                qe.put(s)
                s = t
        return s


arr = [2, 1, 3, 5, 4, 6, 7]
k = 2
rr = Solution().getWinner(arr, k)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
