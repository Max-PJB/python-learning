#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/1/14 16:46
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       53. 最大子序和
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # if n < 2:
        #     return nums[0]
        # mid = n // 2
        # left = nums[:mid:]
        # right = nums[mid::]
        # res_left = self.maxSubArray(left)
        # res_right = self.maxSubArray(right)
        # biggest_left = left[mid - 1]
        # sum_left = left[mid - 1]
        # for i in range(mid - 2, -1, -1):
        #     sum_left += nums[i]
        #     if sum_left > biggest_left:
        #         biggest_left = sum_left
        # biggest_right, sum_right = right[0], right[0]
        # for j in range(mid + 1, n):
        #     sum_right += nums[j]
        #     if sum_right > biggest_right:
        #         biggest_right = sum_right
        # return max(res_left, res_right, biggest_left + biggest_right)
        num_sum = 0
        max_sum = -float("inf")
        for num in nums:
            num_sum += num
            if num_sum > max_sum:
                max_sum = num_sum
            if num_sum < 0:
                num_sum = 0
        return max_sum


input_in = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = Solution().maxSubArray(input_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
