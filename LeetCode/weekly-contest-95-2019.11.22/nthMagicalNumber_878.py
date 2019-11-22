#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/22 15:10
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       878. 第 N 个神奇数字 Nth Magical Number
    https://leetcode-cn.com/contest/weekly-contest-95/problems/nth-magical-number/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        if A > B:
            A, B = B, A

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        lcm = A * B // gcd(A, B)
        l_a = lcm // A
        l_b = lcm // B
        cnt = l_a + l_b - 1
        t, less = divmod(N, cnt)
        res = 0
        i_a = 1
        i_b = 1
        print(res, t, less)
        for _ in range(less):
            if i_a * A < i_b * B:
                res = i_a * A
                i_a += 1
            else:
                res = i_b * B
                i_b += 1
        return (t * lcm + res) % (10 ** 9 + 7)


N = 3
A = 6
B = 4
rr = Solution().nthMagicalNumber(N, A, B)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
