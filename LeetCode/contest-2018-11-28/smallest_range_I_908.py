#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/28 12:06
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 908. 最小差值 I

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Easy

给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i](即A[i] = A[i]+x) 中。

在此过程之后，我们得到一些数组 B。

返回 B 的最大值和 B 的最小值之间可能存在的最小差值。



示例 1：

输入：A = [1], K = 0
输出：0
解释：B = [1]

示例 2：

输入：A = [0,10], K = 2
输出：6
解释：B = [2,8]

示例 3：

输入：A = [1,3,6], K = 3
输出：0
解释：B = [3,3,3] 或 B = [4,4,4]



提示：

    1 <= A.length <= 10000
    0 <= A[i] <= 10000
    0 <= K <= 10000
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        a, b = min(A), max(A)
        res = 0 if 2*K >= abs(b-a) else abs(b-a)-2*K
        return res


A = [1,3,6]
K = 3
res = Solution().smallestRangeI(A,K)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
