#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/28 14:25
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 910. 最小差值 II

    用户通过次数 7
    用户尝试次数 154
    通过次数 7
    提交次数 646
    题目难度 Medium

给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。

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
输出：3
解释：B = [4,6,3]
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        res = gap = max(A) - min(A)
        if gap <= K:
            return gap
        elif gap >= 4 * K:
            return gap - 2 * K
        # 半加半减情况则可将 A 视为俩部分 A1<A2，为了使差值最小，只能 A1 同加， A2 同减。
        # 那么整个 A 的最大值只能是 A1 尾或 A2 尾，最小值只能是 A1 头或 A2 头，比较这4个值就可以求得差值。
        else:
            for i in range(len(A) - 1):
                big = max(A[-1] - K, A[i] + K)
                small = min(A[0] + K, A[i + 1] - K)
                res = min(res, big - small)
        return res


A = [3, 2, 4, 2]
print(A)
K = 1
res = Solution().smallestRangeII(A, K)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
