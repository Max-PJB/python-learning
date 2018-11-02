#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/1 20:01
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
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
import sys

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def int_32_reverse(x):
    a = int(str(abs(x))[::-1])
    res = 0 if abs(a) > 2 ** 31 else a
    res = -res if x < 0 else res
    return res
    pass


print(sys.maxsize)
n = 123456789547544555
print(int_32_reverse(n))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



