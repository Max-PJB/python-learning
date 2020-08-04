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
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        pp = [[0, 0]]
        res = 0
        M = 10 ** 9 + 7
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                pp.append([i, j])
                i += 1
                j += 1
        pp.append([n1, n2])
        for k in range(len(pp) - 1):
            pi, pj = pp[k]
            i, j = pp[k + 1]
            res += max(sum(nums1[pi:i]), sum(nums2[pj:j]))

        res = res % M
        return res


nums1 = [2, 4, 5, 8, 10]
nums2 = [4, 6, 8, 9]
rr = Solution().maxSum(nums1, nums2)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
