#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/17 16:58
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
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        n = len(A)
        res = [None for _ in range(n)]
        import bisect
        for i, b in enumerate(B):
            j = bisect.bisect(A, b)
            if j < len(A):
                res[i] = A.pop(j)
        for i, r in enumerate(res):
            if r is None:
                res[i] = A.pop()
        return res

    def advantageCount2(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        n = len(A)
        res = [None for _ in range(n)]
        for i in range(n):
            for a in A:
                if a > B[i]:
                    res[i] = a
                    A.remove(a)
                    break
        for i, r in enumerate(res):
            if r is None:
                res[i] = A.pop()
        return res


A = [12, 24, 8, 32]
B = [13, 25, 32, 11]
rr = Solution().advantageCount(A, B)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
