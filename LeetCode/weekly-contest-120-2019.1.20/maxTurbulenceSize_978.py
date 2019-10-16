#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/1/20 10:38
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  978. 最长湍流子数组
显示英文描述

    用户通过次数 2
    用户尝试次数 3
    通过次数 2
    提交次数 3
    题目难度 Medium

当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：

    若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
    或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。

也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

返回 A 的最大湍流子数组的长度。



示例 1：

输入：[9,4,2,10,7,8,8,1,9]
输出：5
解释：(A[1] > A[2] < A[3] > A[4] < A[5])

示例 2：

输入：[4,8,12,16]
输出：2

示例 3：

输入：[100]
输出：1



提示：

    1 <= A.length <= 40000
    0 <= A[i] <= 10^9
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        r = 0
        cnt = 0
        flag = 2
        for i in range(len(A)-1):
            # print(i)
            if A[i] < A[i+1]:
                if flag == 2:
                    flag = 1
                    cnt = 2
                elif flag == 1:
                    cnt = 2
                elif flag == 0:
                    flag = 1
                    cnt += 1
            elif A[i] > A[i+1]:
                if flag == 2:
                    flag = 0
                    cnt = 2
                elif flag == 1:
                    flag = 0
                    cnt += 1
                elif flag == 0:
                    cnt = 2
            else:
                flag = 2
                cnt = 0
            print(cnt)
            if cnt > r:
                r = cnt
        return r


A_in = [9,4,2,10,7,8,8,1,9]
res = Solution().maxTurbulenceSize(A_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
