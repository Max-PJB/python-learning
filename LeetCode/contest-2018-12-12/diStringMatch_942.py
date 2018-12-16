#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/12 11:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   942. 增减字符串匹配

    虚拟 用户通过次数 41
    虚拟 用户尝试次数 48
    虚拟 通过次数 41
    虚拟 提交次数 48
    题目难度 Easy

给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

    如果 S[i] == "I"，那么 A[i] < A[i+1]
    如果 S[i] == "D"，那么 A[i] > A[i+1]



示例 1：

输出："IDID"
输出：[0,4,1,3,2]

示例 2：

输出："III"
输出：[0,1,2,3]

示例 3：

输出："DDI"
输出：[3,2,0,1]



提示：

    1 <= S.length <= 1000
    S 只包含字符 "I" 或 "D"。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        ans = [None for _ in range(n+1)]
        cur_s = 0
        cur_m = n
        index = 0
        while index < n:
            if S[index] == "I":
                ans[index] = cur_s
                cur_s += 1
            else:
                ans[index] = cur_m
                cur_m -= 1
            index += 1
        ans[n] = cur_m
        return ans


s_in = "DDI"
res = Solution().diStringMatch(s_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
