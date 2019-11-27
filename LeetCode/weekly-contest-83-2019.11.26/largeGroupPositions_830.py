#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/26 22:39
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       830. 较大分组的位置 Positions of Large Groups
    https://leetcode-cn.com/contest/weekly-contest-83/problems/positions-of-large-groups/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        tmp_index = 0
        tmp_chr = None
        tmp_cnt = 0
        S = S+"#"
        for i, s in enumerate(S):
            if s == tmp_chr:
                tmp_cnt += 1
            else:
                if tmp_cnt >= 3:
                    res.append([tmp_index, i - 1])
                tmp_cnt = 1
                tmp_index = i
                tmp_chr = s

            print(tmp_cnt)
        return res


inin = "abcdddeeeeaabbbcd"
rr = Solution().largeGroupPositions(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
