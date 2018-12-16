#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/12 11:04
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  941. 有效的山脉数组

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Easy

给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

    A.length >= 3
    在 0 < i < A.length - 1 条件下，存在 i 使得：
        A[0] < A[1] < ... A[i-1] < A[i]
        A[i] > A[i+1] > ... > A[B.length - 1]



示例 1：

输入：[2,1]
输出：false

示例 2：

输入：[3,5,5]
输出：false

示例 3：

输入：[0,3,2,1]
输出：true



提示：

    0 <= A.length <= 10000
    0 <= A[i] <= 10000
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3:
            return False
        i = 0
        j = n - 1
        while i + 1 < n and A[i] < A[i+1]:
            i += 1
        while j > 0 and A[j] < A[j-1]:
            j -= 1
        if 0 < i == j < n - 1:
            return True
        else:
            return False


a_in = [0,2,3,1]
res = Solution().validMountainArray(a_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
