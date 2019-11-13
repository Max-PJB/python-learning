#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/13 9:44
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1053. 交换一次的先前排列 Previous Permutation With One Swap
    https://leetcode-cn.com/contest/weekly-contest-138/problems/previous-permutation-with-one-swap/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        # 不就是需要一个非递减序列嘛，如果从后往前存在一个j>i , A[j]<a[i] 那就就得到这个 i
        # i 和 i:end 中最大的那个数A[m]且A[m]<a[i]交换
        i = len(A) - 2
        while i >= 0:
            if A[i] > A[i + 1]:
                break
            i -= 1
        if i < 0:
            return A
        big = A[i + 1]
        big_index = i + 1
        for j in range(i + 1, len(A)):
            if A[i] > A[j] > big:
                big = A[j]
                big_index = j
        print(i, big_index)
        A[i], A[big_index] = A[big_index], A[i]
        return A


inin = [1, 1, 5]
res = Solution().prevPermOpt1(inin)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
