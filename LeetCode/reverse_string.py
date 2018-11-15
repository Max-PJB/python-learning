#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/13 20:11
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  反转字符串

编写一个函数，其作用是将输入的字符串反转过来。

示例 1:

输入: "hello"
输出: "olleh"

示例 2:

输入: "A man, a plan, a canal: Panama"
输出: "amanaP :lanac a ,nalp a ,nam A"
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def reverse_string(s):
    if not s:
        return s
    res = ""
    for i in s:
        res = i + res
    return res


s_in = "A man, a plan, a canal: Panama"
print(reverse_string(s_in))
print(s_in[::-1])

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



