#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 17:21
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 反转整数

给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321

 示例 2:

输入: -123
输出: -321

示例 3:

输入: 120
输出: 21

注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        x_g = int(str(x)[::-1].strip("-+0"))
        if x_g > 2**31 -1 or x_g < -2**31:
            return 0
        res = x_g if x > 0 else -x_g
        return res


x_in = 1534236469
res = Solution().reverse(x_in)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



