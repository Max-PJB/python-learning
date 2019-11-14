#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/14 13:14
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1018. 可被 5 整除的二进制前缀 Binary Prefix Divisible By 5
    https://leetcode-cn.com/contest/weekly-contest-130/problems/binary-prefix-divisible-by-5/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        tmp = 0
        for i in A:
            tmp = (tmp << 1) + i
            print(tmp)
            if tmp % 5:
                res.append(False)
            else:
                res.append(True)
        return res


inin = [0,1,1]
rr = Solution().prefixesDivBy5(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
