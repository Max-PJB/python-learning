#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/5 11:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1111. 有效括号的嵌套深度
    https://leetcode-cn.com/contest/weekly-contest-144/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = []
        res = [0 for _ in seq]
        max_depth = 0
        for i,symbol in enumerate(seq):
            if symbol == "(":
                stack.append(i)
                max_depth = max(max_depth, len(stack))
            else:
                if len(stack) > max_depth//2:
                    res[i] = 1
                    j = stack.pop()
                    res[j] = 1
                else:
                    stack.pop()
            print(i,symbol,stack,max_depth)

        return res


seq = "(((()))((())))"
rr = Solution().maxDepthAfterSplit(seq)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
