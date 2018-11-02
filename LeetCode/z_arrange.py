#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/1 19:03
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R

之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);

示例 1:

输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"

示例 2:

输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def z_arrange(s, numrows):
    if numrows < 2:
        return s
    res = [[] for _ in range(numrows)]
    circle = numrows * 2 - 2
    length = len(s)
    for i in range(length):
        t = i % circle if i % circle < numrows else circle - i % circle
        # if t < numrows:
        #     res[t].append(s[i])
        # else:
        #     t = circle - t
        res[t].append(s[i])
    print(res)
    return ''.join(map(lambda x: ''.join(x), res))


ss = "PAYPALISHIRING"
print(z_arrange(ss, 4))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
