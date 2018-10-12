#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/25 20:34
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'


class DelObject:
    def __init__(self):
        self.var = 100

    def __del__(self):
        class_name = self.__class__.__name__
        print("对象%s销毁" % class_name)


do1 = DelObject()
do2 = do1
do3 = do1
print(id(do1))
print(id(do2))
print(id(do3))
del do1
del do2
del do3
# 在这个例子中__del__()为一个析构函数，当删除对象时，会调用本身的函数，在对象删除完毕时也会再次调用这个函数。