#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/15 13:28
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
        return -1
    head = nums[0]
    n = len(nums)
    tail = nums[n-1]
    if head > tail:
        if target >= head:
            # 从前往后找
            i = 0
            while i < n and target >= nums[i] >= tail:
                print("111")
                if nums[i] == target:
                    return i
                i += 1
        # elif target < nums[0]:
        else:
            # 从后往前找
            j = n - 1
            while j >= 0 and target <= nums[j] <= head:
                print("222")
                if nums[j] == target:
                    return j
                j -= 1
    else:
        for i,j in enumerate(nums):
            if j == target:
                return i
    return -1


nums = [1, 3]
target = 1
print(search(nums, target))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
