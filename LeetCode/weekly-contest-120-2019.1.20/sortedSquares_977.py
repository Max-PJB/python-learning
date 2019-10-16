#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/1/20 10:30
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    977. 有序数组的平方
显示英文描述

    用户通过次数 0
    用户尝试次数 0
    通过次数 0
    提交次数 0
    题目难度 Easy

给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。



示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]



提示：

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A 已按非递减顺序排序。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        i = 0
        j = n - 1
        r = []
        while i <= j:
            if A[i] + A[j] < 0:
                r.insert(0, A[i] ** 2)
                i += 1
            else:
                r.insert(0, A[j] ** 2)
                j -= 1
        # print(r)
        return r


A_in = [-4, -1, 0, 3, 10]
res = Solution().sortedSquares(A_in)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
