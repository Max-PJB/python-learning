#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/16 20:11
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1072. 按列翻转得到最大值等行数
    https://leetcode-cn.com/contest/weekly-contest-139/problems/flip-columns-for-maximum-number-of-equal-rows/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        res = {}
        for row in matrix:
            row_key1 = "".join(map(str, row))
            row_key2 = "".join(map(lambda x: str(1 - x), row))
            res[row_key1] = res.setdefault(row_key1, 0) + 1
            res[row_key2] = res.setdefault(row_key2, 0) + 1
        print(res)
        return max(res.values())


inin = [[0,1],[1,1]]
rr = Solution().maxEqualRowsAfterFlips(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
