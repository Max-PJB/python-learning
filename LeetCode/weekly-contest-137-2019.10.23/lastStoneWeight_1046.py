#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/23 13:32
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  1046. 最后一块石头的重量 显示英文描述
用户通过次数465
用户尝试次数501
通过次数471
提交次数950
题目难度Easy
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。



提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000
-------------------------------------------------
"""
import time
from typing import List
import heapq

__author__ = 'Max_Pengjb'
start_time = time.time()
print(heapq.__all__)


# 下面写上代码块
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = [-i for i in stones]
        heapq.heapify(res)
        while len(res) > 1:
            x, y = heapq.heappop(res), heapq.heappop(res)
            z = x - y
            heapq.heappush(res, z)
        return -res[0]


st = [2, 7, 4, 1, 8, 1]
res = Solution().lastStoneWeight(st)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
