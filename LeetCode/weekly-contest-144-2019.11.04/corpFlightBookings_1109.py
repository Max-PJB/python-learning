#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/5 9:19
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1109. 航班预订统计
    https://leetcode-cn.com/contest/weekly-contest-144/problems/corporate-flight-bookings/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 1.暴力法，肯定超时，不用想
        # res = [0 for _ in range(n)]
        # for (i,j,k) in bookings:
        #     while i <= j:
        #         res[i-1] += k
        #         i += 1
        # return res
        # 大牛动态规划，坐公交车问题的解释，太形象了
        # 解题思路：换一种思路理解题意，将问题转换为：
        # 某公交车共有 n 站，第 i 条记录 bookings[i] = [i, j, k] 表示在 i 站上车 k 人，乘坐到 j 站，在 j+1 站下车，
        # 需要按照车站顺序返回每一站车上的人数
        # 定义 counter[] 数组记录每站的人数变化，counter[i] 表示第 i+1 站。
        # 遍历 bookings[]：bookings[i] = [i, j, k] 表示在 i 站增加 k 人即 counters[i-1] += k，在 j+1 站减少 k 人即 counters[j] -= k
        # 遍历（整理）counter[] 数组，得到每站总人数： 每站的人数为前一站人数加上当前人数变化 counters[i] += counters[i - 1]
        res = [0 for _ in range(n+1)]
        for i, j, k in bookings:
            res[i-1] += k
            res[j] -= k
        for i in range(1, n):
            res[i] += res[i - 1]
        return res[:-1]


aa = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
rr = Solution().corpFlightBookings(aa, 5)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
