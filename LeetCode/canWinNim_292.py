#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/5/26 18:54
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


class Solution:
    def canWinNim(self, n: int) -> bool:
        # dp[k][x] = 0/1 表示 桌子上剩下 k 块石头，此时我的 x=1 先手 / x=0 后手 是否获胜
        dp = [[False for _ in range(2)] for _ in range(n + 1)]
        dp[1][1] = True
        dp[2][1] = True
        dp[3][1] = True
        for i in range(4, n + 1):
            for j in range(i - 3, i):
                if dp[j][0]:
                    dp[i][1] = True
            dp[i][0] = not dp[i][1]
        print(dp)


rr = Solution().canWinNim(10)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
