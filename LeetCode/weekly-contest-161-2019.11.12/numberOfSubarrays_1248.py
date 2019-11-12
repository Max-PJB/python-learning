#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/12 9:30
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1248. 统计「优美子数组」Count Number of Nice Subarrays
    https://leetcode-cn.com/contest/weekly-contest-161/problems/count-number-of-nice-subarrays/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 我的思路：
        #     1. 把所有的 odd number 找出来
        #     2. 统计每个 odd 左边有 x 个 even ，右边有 y 个 even
        #     3. 那么，按题设，k 个 odd 的子数组，最两端的两个 odd 分别是  odd_left,odd—_right,
        #         他们再连上 odd_left 左边的 even ，odd—_right 右边的 even，就可以有 （x+1)*(y+1) 种组合
        # 代码优化后，时间复杂度 o（2n)
        dp = []
        tmp = 0
        nums.insert(0, 1)
        nums.append(1)
        for i, num in enumerate(nums):
            if num % 2:
                if dp:
                    dp[-1].append(i - tmp)
                dp.append([i - tmp])
                tmp = i
        print(dp)
        dp.pop(0)
        dp.pop(-1)
        if len(dp) < k:
            return 0
        i, j = 0, k - 1
        res = 0
        while j < len(dp):
            res += dp[i][0] * dp[j][1]
            i += 1
            j += 1
        return res


nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
rr = Solution().numberOfSubarrays(nums, k)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
