#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 22:36
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   2的幂

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1

示例 2:

输入: 16
输出: true
解释: 24 = 16

示例 3:

输入: 218
输出: false
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 0:
            if n & 1 == 1 and n > 1:
                return False
            n >>= 1
        return True


s_in = 0
res = Solution().isPowerOfTwo(s_in)
print(res)

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



