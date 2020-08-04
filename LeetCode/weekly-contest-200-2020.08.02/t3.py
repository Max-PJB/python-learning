#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/19 10:27
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        ch_region = {}
        for i, ch in enumerate(s):
            if ch in ch_region:
                ch_region[ch] = [ch_region[ch][0], i]
            else:
                ch_region[ch] = [i, i]
        regions = ch_region.values()
        # print(regions)
        res = []
        for start, end in regions:
            ss = set()
            while ss != set(s[start:end + 1]):
                ss = set(s[start:end + 1])
                # print(ss)
                for cha in ss:
                    start = min(start, ch_region[cha][0])
                    end = max(end, ch_region[cha][1])
            res.append([start, end])
        res.sort(key=lambda x: x[1] - x[0])
        # print(res)
        r = []
        while res:
            start, end = res.pop(0)
            r.append(s[start:end + 1])
            t = []
            for st, en in res:
                if en < start or st > end:
                    t.append([st, en])
            res = t
        return r


ss = "cabcccbaa"
rr = Solution().maxNumOfSubstrings(ss)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
