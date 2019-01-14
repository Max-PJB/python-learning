#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/1/6 10:32
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  970. 强整数
显示英文描述

    用户通过次数 0
    用户尝试次数 0
    通过次数 0
    提交次数 0
    题目难度 Easy

给定两个非负整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。

返回值小于或等于 bound 的所有强整数组成的列表。

你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。



示例 1：

输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释：
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2

示例 2：

输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]



提示：

    1 <= x <= 100
    1 <= y <= 100
    0 <= bound <= 10^6
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        x, y = (x, y) if x < y else (y, x)
        if bound < 2:
            return []
        if y == 1:
            return [2]
        r = {}
        yy = 1
        if y != 1 and x == 1:
            while yy < bound:
                r[yy+1] = 1
                yy *= y
        else:
            while yy < bound:
                xx = 1
                while xx + yy <= bound:
                    r[xx+yy] = 1
                    xx *= x
                yy *= y
        return list(r.keys())


res = Solution().powerfulIntegers(1, 2, 100)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
