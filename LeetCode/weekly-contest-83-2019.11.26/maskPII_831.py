#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/26 22:49
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       831. 隐藏个人信息 Masking Personal Information
    https://leetcode-cn.com/contest/weekly-contest-83/problems/masking-personal-information/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()

s = "sasbfssssffffffsdsdkk"
d = "sm"
import re

print(re.search(d, s))
print(re.match(d, s))
print(re.findall(d, s))


# 下面写上代码块
class Solution:
    def maskPII(self, S: str) -> str:
        S = S.lower()
        import re
        have_at = re.search('@', S)
        if have_at:
            return S[0] + '*' * 5 + S[have_at.span()[0] - 1:]
        else:
            digitals = re.findall('\d', S)
            # print(digitals)
            n = len(digitals)
            if n > 10:
                return '+' + '*' * (n - 10) + '-***-***-' + "".join(digitals[-4:])
            else:
                return '***-***-' + "".join(digitals[-4:])


inin = "86-(10)12345678"
rr = Solution().maskPII(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
