#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/5/26 18:54
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big_heap = []
        self.small_heap = []

    def addNum(self, num: int) -> None:
        import heapq
        heapq.heappush(self.big_heap, -num)
        heapq.heappush(self.small_heap, -heapq.heappop(self.big_heap))
        if len(self.small_heap) > len(self.big_heap):
            heapq.heappush(self.big_heap, -heapq.heappop(self.small_heap))

    def findMedian(self) -> float:
        if not self.big_heap:
            return None
        elif len(self.big_heap) > len(self.small_heap):
            return -self.big_heap[0]
        else:
            return (-self.big_heap[0] + self.small_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# rr = Solution().wordPattern(pattern, str)
# print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
