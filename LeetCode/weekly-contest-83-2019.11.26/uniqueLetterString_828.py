#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/27 9:57
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       828. 独特字符串 Unique Letter String
    https://leetcode-cn.com/contest/weekly-contest-83/problems/unique-letter-string/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def uniqueLetterString(self, S: str) -> int:
        dd = {chr(ord('A') + i): [-1, -1] for i in range(26)}
        res = 0
        pre = 0
        MOD = 10 ** 9 + 7
        for i, s in enumerate(S):
            pre = pre + i - 2 * dd[s][1] + dd[s][0]
            dd[s][0], dd[s][1] = dd[s][1], i
            res = (pre + res) % MOD
        return res


inin = "ABA"
rr = Solution().uniqueLetterString(inin)
print(rr)

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
