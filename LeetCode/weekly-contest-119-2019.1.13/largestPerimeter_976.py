#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/1/13 10:51
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  976. 三角形的最大周长
显示英文描述

    用户通过次数 63
    用户尝试次数 79
    通过次数 63
    提交次数 101
    题目难度 Easy

给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。



示例 1：

输入：[2,1,2]
输出：5

示例 2：

输入：[1,2,1]
输出：0

示例 3：

输入：[3,2,3,4]
输出：10

示例 4：

输入：[3,6,2,3]
输出：8



提示：

    3 <= A.length <= 10000
    1 <= A[i] <= 10^6

Python3
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        第一种情况：知道a是最大的边，最小的两个数相加是不是大于最大的那个数，判断b+c>a，成立就能构成三角形
        第二种情况，不知道大小，要求a+b>c;b+c>a;c+a>b三个式子都符合就能构成三角形
        """
        A.sort(reverse=True)
        print(A)
        n = len(A)
        for a in range(n - 2):
            for b in range(a + 1, n - 1):
                for c in range(b + 1, n):
                    if A[a] < A[b] + A[c]:
                        return A[a] + A[b] + A[c]
                    else:
                        break
        return 0


A = [1, 2, 3, 4, 5, 8]
res = Solution().largestPerimeter(A)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
