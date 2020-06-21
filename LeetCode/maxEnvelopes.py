#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/13 13:16
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
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        w_order = sorted(envelopes, key=lambda x: x[0])
        h_order = sorted(envelopes, key=lambda x: x[1])
        n = len(envelopes)
        # dp[i] 表示以 w_order 中第 i 个元素为结尾的套娃的数量
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            ws_set = set(w_order[:i+1])
            en = w_order[i]
            if en[0] > w_order[i-1][0]:
                ws.add(tuple(w_order[i - 1]))
            hs = set()
            for hen in h_order:
                if hen == en:
                    break
                hs.add(tuple(hen))

            dp[i] = len(ws & hs)+1
        return max(dp)


inin = [[5, 4], [6, 4], [6, 7], [2, 3]]
rr = Solution().maxEnvelopes(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
