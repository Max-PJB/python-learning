#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/29 22:02
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1013. 将数组分成和相等的三个部分
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_3s = sum(A)
        sum_1s, remainder = divmod(sum_3s, 3)
        if remainder != 0:
            return False
        sum_start = 0
        flag = 1
        for i in A:
            sum_start += i
            if sum_start == sum_1s * flag:
                flag += 1
                if flag == 3:
                    return True
        print(flag)
        return False


aa = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
res = Solution().canThreePartsEqualSum(aa)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
