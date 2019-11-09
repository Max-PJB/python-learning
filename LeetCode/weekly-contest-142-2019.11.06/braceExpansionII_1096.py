#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/7 11:44
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1096. 花括号展开 II
    https://leetcode-cn.com/contest/weekly-contest-142/problems/brace-expansion-ii/
-------------------------------------------------
"""
import time
from typing import List
import itertools
from functools import reduce
import re

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # {a}，{b} 类型 -> {a} + {b}
        def unlock_comma(start, end):
            print("unlock_comma", start, end, expression[start:end + 1])
            stack = []
            res = []
            flag_have_comma = False
            cur = start
            for i in range(start, end + 1):
                ch = expression[i]
                if ch == "{":
                    stack.append(i)
                elif ch == "}":
                    stack.pop()
                elif ch == ",":
                    if not stack:
                        flag_have_comma = True
                        res += unlock_brace(cur, i - 1)
                        cur = i + 1
                        if i < end:
                            res += unlock_comma(i + 1, end)

            if not flag_have_comma:
                return unlock_brace(start, end)
            return res

        # {a}{b}类型 -> axb
        def unlock_brace(start, end):
            print("unlock_brace", start, end, expression[start:end + 1])

            if "{" not in expression[start:end] and "}" not in expression[start:end] and "," not in expression[
                                                                                                    start:end]:
                return [expression[start:end + 1]]
            stack = []
            res = [""]
            cur = start
            for i in range(start, end + 1):
                ch = expression[i]
                if ch == "{":
                    if not stack and cur != i:
                        res = [x + y for x, y in list(itertools.product(res, unlock_brace(cur, i - 1)))]
                        cur = i
                    stack.append(i)
                elif ch == "}":
                    stack.pop()
                    if not stack:
                        res = [x + y for x, y in list(itertools.product(res, unlock_comma(cur + 1, i - 1)))]
                        cur = i + 1
            if cur <= end:
                res = [x + y for x, y in list(itertools.product(res, unlock_brace(cur, end)))]
            return res

        return list(set(unlock_comma(0, len(expression) - 1)))


inin = "{a,b}c{d,e}f"
res = Solution().braceExpansionII(inin)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
s = [[1,2,3,4,5],[1,2,3,4,5]]
kk = {j + i for i in s.pop() | s.pop() for j in s[-1]}
print(kk)