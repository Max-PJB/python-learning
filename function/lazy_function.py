#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/21 18:54
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""
__author__ = 'Max_Pengjb'


# 定义求和函数，返回的并不是求和结果，而是计算求和的函数
def lazy_plus(*args):
    def plus():
        s = 0
        for n in args:
            s = s + n
        return s

    return plus


# 调用函数f时，得到真正求和的结果
f = lazy_plus(1, 2, 3, 4, 5)
print(f())
"""
当我们调用lazy_plus()时，返回的并不是求和结果，而是计算求和的函数：
在上述例子中，我们在函数lazy_plus中又定义了函数plus，而且内部函数plus是可以引用外部函数lazy_plus的参数和局部变量的，
当函数lazy_plus返回函数plus时，相关参数和变量也将会保存在返回的函数中，这种方式也称为“闭包（Closure）”。
"""
#   调用lazy_plus()时，返回的并不是求和结果，而是求和函数
print(f)
# 输出结果：
# <function lazy_plus.<locals>.plus at 0x000001DAC97F9950>
# 再次解释了什么叫返回函数 当我们调用lazy_plus()时，返回的并不是求和结果，而是计算求和的函数：

