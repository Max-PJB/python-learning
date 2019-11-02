#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/2 10:53
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       893. 特殊等价字符串组
    https://leetcode-cn.com/contest/weekly-contest-99/problems/groups-of-special-equivalent-strings/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        # 思路：取出奇数的单词，偶数的字母。排序后分别拼接成2个单词，再合并成一个单词。这就是特殊等价字符串的特征形式
        res = {}
        for a in A:
            res["".join(sorted(a[0::2]))+"".join(sorted(a[1::2]))] = 1
        return len(res)


inin = ["abcd","cdab","adcb","cbad"]
rrr = Solution().numSpecialEquivGroups(inin)
print(rrr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
