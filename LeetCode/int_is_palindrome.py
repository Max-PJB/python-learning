#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 17:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    回文数

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true

示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:

你能不将整数转为字符串来解决这个问题吗？
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0:
        #     return False
        # elif x == 0:
        #     return True
        if not x % 10 and x != 0:
            return False
        p = x
        k = 0
        while p >= k:
            print(p, k)
            if k == p or k == int(p/10):
                return True
            k = k * 10 + p % 10
            p = int(p / 10)

        return False


x_in = 10
res = Solution().isPalindrome(x_in)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
