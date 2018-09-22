#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/21 16:32
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""
__author__ = 'Max_Pengjb'
# Python中，数值类型（int和float）、字符串str、元组tuple都是不可变类型。而列表list、字典dict、集合set是可变类型。
a = 2


def sum_a(b):
    b += 1
    return


sum_a(a)  # 这里并不影响 a 的值。虽然是传递引用，但是由于不能改变原来引用的值，所以只能开辟新的内存空间，在复制原来值，进行改变
print(a)


# 默认参数
# 默认参数是指给函数参数提供默认值，如果在调用函数的时候没有给该参数传递值，则该参数使用默认值。例如：

# 定义加法函数plus，参数a是必选参数，参数b是默认值2的参数
def plus(x, y=2):
    c = x + y
    return c


# 调用函数plus时，必须给参数a传递值，若不给b传递值，则b默认为2
d = plus(4)
# 输出结果d
print(d)


# 定义一个包含关键字参数的函数，返回值为参数值
def plus(**kw):
    return kw


# 调用plus函数，参数值为空
d1 = plus()
# 调用plus函数，参数值为x=1
d2 = plus(x=1)
# 调用plus函数，参数值为x=1,y=2
d3 = plus(x=1, y=2)
# 输出d1,d2,d3
print(d1)
print(d2)
print(d3)


def plus1(x, y, z=0, *args, **kw):
    print('x=', x)
    print('y=', y)
    print('z=', z)
    print('args=', args)
    print('kw=', kw)

dict11 = {'x': 1, 'y': 2, 'z': 3}
# 调用函数plus，输入参数x=1,y=2,z=3,args=(4,5,6),kw={}
plus1(1, 2, 3, 4, 5, 6)
print('\n')
# 调用函数plus，输入参数x=1,y=2,z=3,args=(4,5,6),kw={'k':7, 'm':8}
plus1(1, 2, 3, 4, 5, 6, k=7, m=8)


# 定义一个plus函数，有3个参数，返回值是3个参数之和
def plus1111(x, y, z):
    return x + y + z


# 有一个dict列表，当中3个键的值分别为1,2,3
dict1 = {'x': 1, 'y': 2, 'z': 3}
# 用关键字参数的方法将dict列表中的3个值传入plus函数中，得到返回值d
d = plus1111(**dict1)
# 输出d
print(d)
