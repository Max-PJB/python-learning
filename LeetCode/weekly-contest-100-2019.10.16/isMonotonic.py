#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/16 10:16
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    896. 单调数列 显示英文描述
用户通过次数311
用户尝试次数332
通过次数320
提交次数733
题目难度Easy
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。



示例 1：

输入：[1,2,2,3]
输出：true
示例 2：

输入：[6,5,4,4]
输出：true
示例 3：

输入：[1,3,2]
输出：false
示例 4：

输入：[1,2,4,5]
输出：true
示例 5：

输入：[1,1,1]
输出：true


提示：

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        monotone = 0
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                if monotone == 1:
                    return False
                else:
                    monotone = -1
            elif A[i] < A[i + 1]:
                if monotone == -1:
                    return False
                else:
                    monotone = 1
            else:
                continue
        return True


a = [1, 2, 2, 3]
res = Solution().isMonotonic(a)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
