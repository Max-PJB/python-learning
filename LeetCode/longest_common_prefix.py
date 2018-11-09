#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/2 21:07
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def longest_common_prefix(strs):
    res = ""
    if not strs:
        return res
    ss = list(map(list, strs))
    nums = len(ss)
    # if ss[0][0] != ss[1][0] or ss[0][0] != ss[2][0]:
    #     return res
    for i in range(min(list(map(lambda x: len(x), ss)))):
        for j in range(nums-1):
            if ss[j][i] != ss[j+1][i]:
                return res
        res += ss[0][i]
    return res


# strings = ["dog", "racecar", "car"]
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
