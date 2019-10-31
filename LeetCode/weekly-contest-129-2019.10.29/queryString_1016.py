#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/30 16:44
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1016. 子串能表示从 1 到 N 数字的二进制串
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        # 易知，对于任意整数n，其二进制表示的字符串均包含右移一位后的子串，即
        # n / 2
        # 取整后的二进制表示。我们注意到末位为1和0的值均包含同一子序列，则不妨设n = 2
        # k，则整数序列(k + 1, k + 2,..
        # .2
        # k)的二进制表示将包含整数序列(k + 1 / 2, ...
        # k) 的二进制表示。
        # 根据简单归纳得知该序列将包含右移至末尾后所有子序列的求和，即整数序列(1, 2...k)。故只需要遍历[N >> 1 + 1, N]
        # 的范围即可
        res = True
        if N < 2: return res
        for i in range(N >> 1 + 1, N + 1):
            s = str(bin(i))[2:]
            if (s in S):
                res &= True
            else:
                res &= False
                break
        return res


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
