#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/1 11:32
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       不浪费原料的汉堡制作方案 Number of Burgers with No Waste of Ingredients
    https://leetcode-cn.com/contest/weekly-contest-165/problems/number-of-burgers-with-no-waste-of-ingredients/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        total_jumbo = tomatoSlices - cheeseSlices * 2
        if total_jumbo < 0 or total_jumbo % 2:
            return []
        else:
            total_jumbo //= 2
            if total_jumbo > cheeseSlices:
                return []
            return [total_jumbo, cheeseSlices - total_jumbo]


a = 16
b = 7
rr = Solution().numOfBurgers(a, b)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
