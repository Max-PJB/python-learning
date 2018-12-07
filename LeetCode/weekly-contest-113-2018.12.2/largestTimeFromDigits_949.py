#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/2 10:32
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  949. 给定数字能组成的最大时间

    用户通过次数 0
    用户尝试次数 0
    通过次数 0
    提交次数 0
    题目难度 Easy

给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。

最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。

以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。



示例 1：

输入：[1,2,3,4]
输出："23:41"

示例 2：

输入：[5,5,5,5]
输出：""



提示：

    A.length == 4
    0 <= A[i] <= 9
-------------------------------------------------
"""
import time
import itertools

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        cur_hour = -1
        cur_minute = -1
        for i in range(4):
            for j in range(4):
                if j != i:
                    for k in range(4):
                        if k != i and k != j:
                            hour = A[i] * 10 + A[j]
                            minute = A[k] * 10 + A[6 - i - j - k]
                            if hour < 24 and minute < 60:
                                if hour > cur_hour:
                                    cur_hour = hour
                                    cur_minute = minute
                                elif hour == cur_hour and minute > cur_minute:
                                    cur_hour = hour
                                    cur_minute = minute
        if cur_hour == -1 or cur_hour == -1:
            return ""
        return "{:0>2}:{:0>2}".format(cur_hour, cur_minute)

    def largestTimeFromDigits2(self, A):
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""


A_in = [1, 2, 3, 4]
res = Solution().largestTimeFromDigits(A_in)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
