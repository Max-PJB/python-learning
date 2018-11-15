#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/13 18:30
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    字符串相乘

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"

说明：

    num1 和 num2 的长度小于110。
    num1 和 num2 只包含数字 0-9。
    num1 和 num2 均不以零开头，除非是数字 0 本身。
    不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
-------------------------------------------------
"""
import time
from functools import reduce

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def string_multiply(num1, num2):
    # 产生一个乘法表，就是第一个字符串乘以 0-9 的字典 {1：xx,2:yy,3:zz.....9:rr}
    if num1[0] == "0" or num2[0] == "0":
        return "0"
    str_multiply_dic = {"0": "0"}
    for n in range(1, 10):
        jw = 0
        res = ""
        for i in num1[::-1]:
            k = int(i)
            tmp = (k * n + jw) % 10
            jw = int((k * n + jw) / 10)
            res = str(tmp) + res
        if jw != 0:
            res = str(jw) + res
        str_multiply_dic[str(n)] = res
    print(str_multiply_dic)
    str_list = []
    m = len(num2)
    for i, num in enumerate(num2):
        if num != '0':
            str_list.append(str_multiply_dic[num] + "0" * (m-i-1))
    print(str_list)
    print(sum(map(int, str_list)))
    res = reduce(str_plus_str, str_list)
    print(res)
    return res


def str_plus_str(str_num1, str_num2):
    jw = 0
    res = ""
    i = len(str_num1) - 1
    j = len(str_num2) - 1
    while i >= 0 and j >= 0:
        tmp = int(str_num1[i]) + int(str_num2[j]) + jw
        jw = int(tmp / 10)
        res = str(tmp % 10) + res
        i -= 1
        j -= 1
    while i >= 0:
        tmp = int(str_num1[i]) + jw
        jw = int(tmp / 10)
        res = str(tmp % 10) + res
        i -= 1
    while j >= 0:
        tmp = int(str_num2[j]) + jw
        jw = int(tmp / 10)
        res = str(tmp % 10) + res
        j -= 1
    if jw != 0:
        res = str(jw) + res
    # print(res)
    return res


num1_in = "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999990"
num2_in = "135799999999999999999999999999999999999999999999999999999999999999999999999"
# print(str_plus_str(num1_in, num2_in))
string_multiply(num1_in, num2_in)
print(int(num1_in)*int(num2_in))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
