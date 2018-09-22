#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/21 17:24
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
    Description :    关键字参数 **
-------------------------------------------------
"""
__author__ = 'Max_Pengjb'


# 定义一个plus函数，有3个参数，返回值是3个参数之和
def plus(x, y, z):
    return x + y + z


# 有一个dict列表，当中3个键的值分别为1,2,3
dict = {'x': 1, 'y': 2, 'z': 3}
# 将dict列表中的3个值传入plus函数中，得到返回值d
d = plus(dict['x'], dict['y'], dict['z'])
# 输出d
print(d)
# 用关键字参数的方法将dict列表中的3个值传入plus函数中，得到返回值d
d = plus(**dict)
# 输出d
print(d)


# 定义一个包含必选参数、默认参数、可变参数和关键字参数的函数plus
def plus1(x, y, z=0, *args, **kw):
    print('x=', x)
    print('y=', y)
    print('z=', z)
    print('args=', args)
    print('kw=', kw)


# 调用函数plus，输入两个参数1,2
plus1(1, 2)


# 定义一个包含必选参数、默认参数、可变参数和关键字参数的函数plus


def plus3(x, y, z=0, *args, **kw):
    print('x=', x)
    print('y=', y)
    print('z=', z)
    print('args=', args)
    print('kw=', kw)


# 调用函数plus，输入参数x=1,y=2,z=3,args=(4,5,6),kw={}
plus3(1, 2, 3, 4, 5, 6)
print('\n')
# 调用函数plus，输入参数x=1,y=2,z=3,args=(4,5,6),kw={'k':7, 'm':8}
plus3(1, 2, 3, 4, 5, 6, k=7, m=8)

# 定义并调用一个函数，功能是对输入的列表中的数值元素进行累加，列表中元素的个数没有确定；
# 将累加结果存储到变量d中；
# 输出累加结果d。
# 创建一个空列表numbers
numbers = []
# str用来存储输入的数字字符串，lst1是将输入的字符串用空格分割，存储为列表
str_input = input()
lst1 = str_input.split(' ')
# 将输入的数字字符串转换为整型并赋值给numbers列表
for i in range(len(lst1)):
    numbers.append(int(lst1.pop()))
# 请在此添加代码，实现编程要求
# ********** Begin *********#
# 定义并调用一个函数，功能是对输入的列表中的数值元素进行累加，列表中元素的个数没有确定；
# 将累加结果存储到变量d中；
# 输出累加结果d。
print(numbers)


def sum_all(*args):
    re = 0
    for k in args:
        re += k
    return re

res = sum_all(*numbers)
# ********** End **********#
print(res)
