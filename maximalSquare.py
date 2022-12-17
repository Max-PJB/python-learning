#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/13 12:12
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
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            tmp = 0
            for j in range(1, m + 1):
                tmp += int(matrix[i - 1][j - 1])
                if i == 0:
                    dp[i][j] = tmp
                else:
                    dp[i][j] = dp[i - 1][j] + tmp
        for d in dp:
            print(d)

        def big_tangle(x1, y1):
            res = 1
            x2, y2 = x1 + res, y1 + res
            while x2 < n + 1 and y2 < m + 1 and dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1] == (
                    res + 1) * (res + 1):
                res += 1
                x2, y2 = x1 + res, y1 + res
            return res
        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == '1':
                    print(i, j, big_tangle(i, j))
                    res = max(res, big_tangle(i, j))
        return res * res


inin = [["1", "1", "1", "1"], ["1", "1", "1", "1"], ["1", "1", "1", "1"]]
rr = Solution().maximalSquare(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))

a= __import__('build_in')
b = __import__('build_in.heap', fromlist=(' ',))
print(a)
print(b)
print(a.heap.Heap.left_child(2))
print(b.Heap.left_child(2))
import build_in as bi
print(bi.heap.Heap.left_child(2))
import importlib
c = importlib.import_module('build_in.heap')
print(c.Heap.left_child(2)+9)
import pkgutil
print(a.__path__, a.__name__)
for p in pkgutil.walk_packages(a.__path__,a.__name__+'.'):  # 会递归
    print(p,1)
for p in pkgutil.iter_modules(a.__path__,a.__name__+'.'):  # 不会递归到最深层
    print(p,2)
    