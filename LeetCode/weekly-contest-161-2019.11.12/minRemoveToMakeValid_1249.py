#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/12 9:15
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :     1249. 移除无效的括号
    https://leetcode-cn.com/contest/weekly-contest-161/problems/minimum-remove-to-make-valid-parentheses/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        re = []
        s = list(s)
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    re.append(i)
        print(stack,re)
        for j in sorted(stack + re,reverse=True):
            s.pop(j)
        return "".join(s)


s = "))(("
rr = Solution().minRemoveToMakeValid(s)
print(rr)

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
