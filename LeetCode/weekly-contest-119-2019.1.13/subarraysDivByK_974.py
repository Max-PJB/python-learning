#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/1/13 11:11
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :974. 和可被 K 整除的子数组
显示英文描述

    用户通过次数 23
    用户尝试次数 82
    通过次数 23
    提交次数 143
    题目难度 Medium

给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。



示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]



提示：

    1 <= A.length <= 30000
    -10000 <= A[i] <= 10000
    2 <= K <= 10000
-------------------------------------------------
"""
import time
from functools import reduce

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        global k
        k = 0
        n = len(A)

        # def next(ss, i, p):
        #     global k
        #     if ss % K == 0:
        #         k += 1
        #         print(p, ss)
        #     for j in range(i + 1, n):
        #         next(ss + A[j], j, p + "->" + str(j))
        #
        # for s in range(n):
        #     next(A[s], s, str(s))
        # return k
        # ls = [-1 for _ in range(n)]
        # for i in range(n):
        #     ls_i = 0
        #     for j in range(i, n):
        #         print(ls_i)
        #         ls_i += A[j]
        #         if j == 4:
        #             print(ls_i, i, j)
        #         if ls_i % K == 0:
        #             ls[i] = j
        #             break
        # print(ls)
        #
        # def findnext(i):
        #     global k
        #     if ls[i] != -1:
        #         k += 1
        #         j = ls[i] + 1
        #         if j < n:
        #             findnext(j)
        #
        # for i in range(n):
        #     findnext(i)
        # return k
        ls = [[0, 0] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            ls_i = 0
            for j in range(i, n):
                ls_i += A[j]
                if ls_i % K == 0:
                    ls[i][0] = j
                    ls[i][1] = 1
                    if j + 1 < n:
                        ls[i][1] += ls[j + 1][1]
                    break
        return reduce(lambda x, y: x + y[1], ls, 0)


A = [4, 5, 0, -2, -3, 1]
K = 5
res = Solution().subarraysDivByK(A, K)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
