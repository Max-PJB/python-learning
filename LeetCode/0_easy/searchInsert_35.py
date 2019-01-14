#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/1/9 21:31
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    35. 搜索插入位置
题目描述
评论 (119)
官方题解
提交记录

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2

示例 2:

输入: [1,3,5,6], 2
输出: 1

示例 3:

输入: [1,3,5,6], 7
输出: 4

示例 4:

输入: [1,3,5,6], 0
输出: 0
-------------------------------------------------
"""
import bisect
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        print("res", bisect.bisect(nums, target))

        def bise(low, high):
            """
            :param low:int
            :param high: int
            :return:
            """
            print(low, high)
            if low == high:
                return low
            mid = (low + high) // 2
            if target <= nums[mid]:
                return bise(low, mid)
            else:
                return bise(mid + 1, high)

        print(bise(0, len(nums)))


Solution().searchInsert([1, 3, 5, 6], 7)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
