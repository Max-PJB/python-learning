#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/3 15:34
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
-------------------------------------------------
"""
import time
import sys

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def three_sum_smaller(nums, target):
    nums.sort()
    n = len(nums)
    deviation = sys.maxsize
    res = None
    for i in range(n-2):
        j = i + 1
        k = n - 1
        while j < k:
            sum3 = nums[i] + nums[j] + nums[k]
            res = sum3 if abs(sum3-target) < deviation else res
            deviation = abs(sum3-target) if abs(sum3-target) < deviation else deviation
            if sum3 - target < 0:
                j += 1
            elif sum3 - target > 0:
                k -= 1
            else:
                return res
    return res


nums_in = [0, 1, 2]
target_in = 3
print(three_sum_smaller(nums_in, target_in))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
