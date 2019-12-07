#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/5 21:20
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1160. 拼写单词 Find Words That Can Be Formed by Characters
    https://leetcode-cn.com/contest/weekly-contest-150/problems/find-words-that-can-be-formed-by-characters/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        char = Counter(chars)
        res = 0
        print(char)
        for w in words:
            wc = Counter(w)
            r = wc - char
            if not r:
                print(r,w)
                res += len(w)
        return res


words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
rr = Solution().countCharacters(words,chars)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
