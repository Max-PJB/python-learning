#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/8 21:16
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   945. 使数组唯一的最小增量

    用户通过次数 123
    用户尝试次数 180
    通过次数 129
    提交次数 496
    题目难度 Medium

给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。

返回使 A 中的每个值都是唯一的最少操作次数。

示例 1:

输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。

示例 2:

输入：[3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。

提示：

    0 <= A.length <= 40000
    0 <= A[i] < 40000
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    # 这个竟然都超时
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a_dict = {}
        cnt = 0
        for i in A:
            while i in a_dict:
                cnt += 1
                i += 1
            a_dict[i] = 1
        return cnt

    def minIncrementForUnique2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        pre = -1
        cnt = 0
        for i in A:
            if i > pre:
                pre = i
            else:
                pre += 1
                cnt += pre - i
        return cnt


in_p = []
res = Solution().minIncrementForUnique2(in_p)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
