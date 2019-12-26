#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/26 17:03
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1297. 子串的最大出现次数 Maximum Number of Occurrences of a Substring
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
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import Counter
        r = 0
        for l in range(minSize, maxSize + 1):
            res = []
            for i in range(len(s) - l + 1):
                tmp = s[i:i + l]
                print(tmp,l)
                if len(Counter(tmp)) <= maxLetters:
                    res.append(tmp)
            if res:
                r = Counter(res).most_common(1)[0][1]
                return r
        return r


s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
rr = Solution().maxFreq(s, maxLetters, minSize, maxSize)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
