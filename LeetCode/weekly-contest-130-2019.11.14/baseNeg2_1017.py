#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/14 13:23
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1017. 负二进制转换 Convert to Base -2
    https://leetcode-cn.com/contest/weekly-contest-130/problems/convert-to-base-2/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def baseNeg2(self, N: int) -> str:
        res = []
        if N == 0:
            return "0"
        while N > 0:
            N, r = divmod(N, 2)
            res.append(r)
        print(res)
        r = [0 for _ in range(len(res) * 2)]
        for i, b in enumerate(res):
            if b == 1:
                if i % 2 == 0:
                    if r[i] == 1:
                        r[i] = 0
                        r[i+1] = 1
                        r[i+2] = 1
                    else:
                        r[i] = 1
                else:
                    if r[i] == 1:
                        r[i] = 0
                    else:
                        r[i] = 1
                        r[i+1] = 1
        flag = False
        rr = ""
        for i in r[::-1]:
            if not flag:
                if i:
                    rr = str(i)
                    flag = True
            else:
                rr += str(i)
        return rr

inin = 6
rr = Solution().baseNeg2(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
