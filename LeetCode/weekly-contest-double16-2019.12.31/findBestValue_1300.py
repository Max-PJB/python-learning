#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/31 12:57
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1300. 转变数组后最接近目标值的数组和 Sum of Mutated Array Closest to Target
-------------------------------------------------
"""
import bisect
import time
from itertools import accumulate
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr_sort = sorted(arr)
        acc = [0] + list(accumulate(arr_sort))
        # TODO 这个题目答案都有问题，下面的例子就是我写的，答案没有考虑到这种情况


arr = [1, 1, 1, 1, 11, 100]
target = 60
rr = Solution().findBestValue(arr, target)
print(rr)

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
