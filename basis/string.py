#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/19
    @   IDE     :       PyCharm
    @   Site    :
-------------------------------------------------
"""
__author__ = 'Max_Pengjb'

# step1: 将输入的源字符串source_string首尾的空格删除
# step2: 将step1处理后的字符串的所有单词的首字母变为大写，并打印输出；
# step3: 将step2转换后的字符串的长度打印输出出来
# 获取待处理的源字符串
source_string = input()
# 请在下面添加字符串转换的代码
print("{}\n{}".format(source_string.strip().title(), len(source_string.strip().title())))
# step1: 查找输入字符串source_string中是否存在day这个子字符串，并打印输出查找结果；
# step2: 对输入字符串source_string执行字符替换操作，将其中所有的day替换为time,并打印输出替换后的字符串；
# step3：对step2进行替换操作后的新字符串，按照空格进行分割，并将分割后的字符列表打印输出出来
print(source_string.find('day'))
print(source_string.replace('day', 'time'))
print((source_string.replace('day', 'time').split()))
print('++1++2++3+4++'.split('+'))
####### End #######







