#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/6 10:17
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1095. 山脉数组中查找目标值
    https://leetcode-cn.com/contest/weekly-contest-142/problems/find-in-mountain-array/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, a):
        self.ll = a

    def get(self, index: int) -> int:
        return self.ll[index]

    def length(self) -> int:
        return len(self.ll)


class Solution:
    """我的思路：
        一个mountainarray ， 我们中间取连续的 2 个数 a b ，那么他只有两种情况
        1. a < b
            1.1 若 target < a : 考虑左边右边都要考虑，先考虑左边，没有再考虑右边
            1.2 若 target = a ：return a
            1.3 若 a < target < b : 考虑右边
            1.3 若 target = b ：return b
            1.4 若 target > b : 考虑右边
        2. a > b
            2.1 target < b: 先考虑左边，再考虑右边
            2.2 target = b： 先考虑左边，右边 = index(b)
            2.3 b < target < a : 只考虑左边
            2.4 target = a ：先考虑左边，右边 = index（a)
            2.5 target > a : 只虑左边
            都要考虑左边，那就把左边提取出来吧
    """

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find(start, end):
            if start + 1 == end or start == end:
                if mountain_arr.get(start) == target:
                    return start
                elif mountain_arr.get(end) == target:
                    return end
                else:
                    return 10001
            mid = (start + end) // 2
            a = mountain_arr.get(mid)
            b = mountain_arr.get(mid + 1)
            if a < b:
                if target < a:
                    left = find(start, mid - 1)
                    if left < 10001:
                        return left
                    else:
                        return find(mid + 1, end)
                elif target == a:
                    return mid
                elif target == b:
                    return mid + 1
                else:
                    return find(mid + 1, end)
            if a > b:
                left = find(start, mid - 1)
                if left < 10001:
                    return left
                if target < b:
                    return min(left, find(mid + 1, end))
                elif target == b:
                    return min(left, mid + 1)
                elif a > target > b:
                    return left
                elif a == target:
                    return min(left, mid)
                else:
                    # target > a
                    return left

        res = find(0, mountain_arr.length() - 1)
        if res < 10001:
            return res
        else:
            return -1


array = [0,1,2,4,2,1]
haha = MountainArray(array)
res = Solution().findInMountainArray(3, haha)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
