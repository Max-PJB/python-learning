#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/25 18:58
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
import math

__author__ = 'Max_Pengjb'
start = time.time()
# 下面写上代码块


class privatization(object):
    def __init__(self, var):
        self._var = var
        self.__var = var
        self.__var__ = var
        self.varation = var


pr = privatization(2)
print(pr._var)
print(pr.__var__)
print(pr.varation)
#   Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性
print(pr._privatization__var)   # __var只能在类实例对象内部访问，也就是self__var才能取到值，实例化后，实例对象.__var取不到值
#print(pr.__var)     # AttributeError: 'privatization' object has no attribute '__var'

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))

# 类中的方法可以分为实例方法、类方法、静态方法和特殊方法几大类。
# 普通实例方法和特殊方法都必须使用self作为第一个参数，表示对象本身。
# 对象的私有数据成员在实例方法和特殊方法中可以使用self作为前缀直接访问。


class Vector3d:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
    pass

    def length(self):
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)


x, y, z = map(int, input().split(','))
v = Vector3d(x, y, z)
print(v._Vector3d__x, v._Vector3d__y, v._Vector3d__z, sep=':')
print(v.length())
