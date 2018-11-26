#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/24 15:41
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   全排列

给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
-------------------------------------------------
"""
import time
from typing import List, Any

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global res
        res = []

        def full_permute(ls, left):
            """
            :param ls: List[List[int]]]
            :param left: List[int]
            :return: None
            """
            if not left:
                res.append(ls)
            for i in range(len(left)):
                full_permute(ls + [left[i]], left[0:i:]+left[i+1::])

        full_permute([], nums)
        return res


nums = [1, 2, 3]
res = Solution().permute(nums)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
