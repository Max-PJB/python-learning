#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/20 13:47
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :      https://leetcode-cn.com/contest/weekly-contest-153/problems/maximum-subarray-sum-with-one-deletion/
    1186. 删除一次得到子数组最大和 显示英文描述
用户通过次数131
用户尝试次数478
通过次数134
提交次数1365
题目难度Medium
给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。

换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。

注意，删除一个元素后，子数组 不能为空。
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # 动态规划，ap[i] 表示以i结尾的没有删除元素的最大子数组 dp[i] 表示以 i 结尾的删了一个元素的最大子数组
        # 那么  ap[i+1] = arr[i] if ap[i] < 0 else ap[i]+arr[i+1]
        #       dp[i+1] = max(ap[i] ， dp[i-1]+arr[i+1])  #删除过的dp[i]加上本身 和 没有删除过的ap[i]删除arr[i+1] 取大值
        ap_pre = arr[0]
        dp_pre = 0
        big = ap_pre
        for i in range(1, len(arr)):
            ap = max(arr[i], ap_pre + arr[i])
            dp = max(ap_pre, dp_pre + arr[i])
            ap_pre, dp_pre = ap, dp
            big = max(big, ap, dp)
        return big


arr = [1,-2,-2,3]
res = Solution().maximumSum(arr)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
