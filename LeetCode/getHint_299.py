#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/5/27 15:28
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
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        m = len(guess)
        a = 0
        from collections import defaultdict
        s_l = defaultdict(int)
        g_l = defaultdict(int)
        while n > 0 and m > 0:
            n -= 1
            m -= 1
            if secret[n] == guess[m]:
                a += 1
            else:
                s_l[secret[n]] += 1
                g_l[guess[m]] += 1
        b = 0
        for k, v in s_l.items():
            b += min(v, g_l[k])
        return str(a) + 'A' + str(b) + 'B'


rr = Solution().getHint('1807', '7810')
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
