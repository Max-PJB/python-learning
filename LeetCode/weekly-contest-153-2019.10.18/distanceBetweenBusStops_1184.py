#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/18 11:03
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :      https://leetcode-cn.com/contest/weekly-contest-153/problems/distance-between-bus-stops/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = (start, destination) if start < destination else (destination, start)
        return min(sum(distance[start:destination]),sum(distance[0:start])+sum(distance[destination:]))


distance = [1,2,3,4]
start = 0
destination = 3
print(Solution().distanceBetweenBusStops(distance,start,destination))
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
