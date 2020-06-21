#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/13 12:49
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
    def maxSubArray(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        n = len(nums)
        # dp[i] 表示以第 i 个nums[i-1] 结尾的连续子数组的最大和
        dp = [-2147483647 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = max(nums[i - 1], dp[i - 1] + nums[i - 1])
        return max(dp)


ini = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
rr = Solution().maxSubArray(ini)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
