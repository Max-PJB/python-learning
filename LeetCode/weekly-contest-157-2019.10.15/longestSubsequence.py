#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/15 16:54
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    1218. 最长定差子序列 显示英文描述
用户通过次数310
用户尝试次数642
通过次数317
提交次数1712
题目难度Medium
给你一个整数数组 arr 和一个整数 difference，请你找出 arr 中所有相邻元素之间的差等于给定 difference 的等差子序列，并返回其中最长的等差子序列的长度。



示例 1：

输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。
示例 2：

输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。
示例 3：

输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。


提示：

1 <= arr.length <= 10^5
-10^4 <= arr[i], difference <= 10^4
-------------------------------------------------
"""
import time
from typing import List
import collections

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        g = {}
        for i in arr:
            if i - difference not in g:
                g[i] = 1
            else:
                g[i] = g[i-difference] + 1
        print(g)
        return max(g.values())

    def longestSubsequence2(self, arr: List[int], difference: int) -> int:
        if difference == 0:
            return max(collections.Counter(arr).values())
        difference2 = abs(difference)
        rr = [[] for _ in range(difference2)]
        for a in arr:
            quotietent, remainder = divmod(a, difference2)
            rr[remainder].append(quotietent)
        res = 1
        for r in rr:
            if len(r) <= res:
                continue
            else:
                tmp = 1
                tmp2 = 1
                r.sort()
                for i in range(len(r) - 1):
                    if r[i + 1] - r[i] == 0:
                        continue
                    elif r[i + 1] - r[i] == 1:
                        tmp2 += 1
                        tmp = max(tmp, tmp2)
                    else:
                        tmp2 = 1
                res = max(res, tmp)
        return res


arr = [1, 3, 2, 3, 4]
difference = 1
rrrrr = Solution().longestSubsequence(arr, difference)
print(rrrrr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
