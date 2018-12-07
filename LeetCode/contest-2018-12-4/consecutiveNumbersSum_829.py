#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/4 14:36
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    829. 连续整数求和

    虚拟 用户通过次数 5
    虚拟 用户尝试次数 9
    虚拟 通过次数 5
    虚拟 提交次数 9
    题目难度 Hard

给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?

示例 1:

输入: 5
输出: 2
解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。

示例 2:

输入: 9
输出: 3
解释: 9 = 9 = 4 + 5 = 2 + 3 + 4

示例 3:

输入: 15
输出: 4
解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

说明: 1 <= N <= 10 ^ 9
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = []
        k = 1
        cnt = 0
        while k * (k + 1) // 2 <= N:
            tmp = N - k * (k - 1) // 2
            if tmp % k == 0:
                n = tmp // k
                res.append([n + i for i in range(k)])
                cnt += 1
            k += 1
        return res

    def consecutiveNumbersSum2(self, N):
        r = 1
        i = 2
        N -= 1
        while N >= i:
            if N % i == 0: r += 1
            N -= i
            i += 1

        return r


N_in = 15
res = Solution().consecutiveNumbersSum(N_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
