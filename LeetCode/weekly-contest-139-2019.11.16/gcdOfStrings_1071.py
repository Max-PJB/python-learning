#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/16 19:32
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1071. 字符串的最大公因子 Greatest Common Divisor of Strings
    https://leetcode-cn.com/contest/weekly-contest-139/problems/greatest-common-divisor-of-strings/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        L1 = len(str1)
        L2 = len(str2)
        str_gcd = gcd(L1, L2)
        while str_gcd > 0:
            if not L1 % str_gcd and not L2 % str_gcd:
                if str1 == str2[0:str_gcd]*(L1//str_gcd) and str2 == str2[0:str_gcd]*(L2//str_gcd):
                    return str2[0:str_gcd]
            str_gcd -= 1
        return ""


str2 = "ABCABC"
str1 = "ABC"
rr = Solution().gcdOfStrings(str1, str2)
print(rr)

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
