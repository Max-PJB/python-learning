#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/27 9:06
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       829. 连续整数求和 Consecutive Numbers Sum
    https://leetcode-cn.com/contest/weekly-contest-83/problems/consecutive-numbers-sum/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        i = 2
        res = 0
        while (i + 1) * i // 2 <= N:
            if (2 * N - i * i + i) % (2 * i) == 0:
                print(i)
                res += 1
            i += 1
        return res + 1
#     这个方法猛啊
        # 1个数时，必然有一个数可构成N
        # 2个数若要构成N，第2个数与第1个数差为1，N减掉这个1能整除2则能由商与商+1构成N
        # 3个数若要构成N，第2个数与第1个数差为1，第3个数与第1个数的差为2，N减掉1再减掉2能整除3则能由商、商+1与商+2构成N
        # 依次内推，当商即第1个数小于等于0时结束
#         res, i = 0, 1
#         while N > 0:
#             res += N % i == 0
#             N -= i
#             i += 1
#         return res
#
# 作者：yybeta
# 链接：https://leetcode-cn.com/problems/consecutive-numbers-sum/solution/pythonchao-hao-li-jie-de-onsuan-fa-by-yybeta/
#

inin = 5
rr = Solution().consecutiveNumbersSum(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
