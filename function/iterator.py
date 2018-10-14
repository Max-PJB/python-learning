#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/22 10:43
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

"""
迭代器的优点

    迭代器访问与for循环访问非常相似，但是也有不同之处。
    对于支持随机访问的数据结构如元组和列表，迭代器并无优势，因为迭代器在访问的时候会丢失数据索引值，
    但是如果遇到无法随机访问的数据结构如集合时，迭代器是唯一访问元素的方式。
    迭代器仅仅在访问到某个元素时才使用该元素，在这之前，元素可以不存在，所以迭代器很适用于迭代一些无法预先知道元素总数的巨大的集合。
    迭代器提供了一个统一的访问集合的接口，定义iter()方法对象，就可以使用迭代器访问。

理解迭代器

可直接作用于for循环的数据类型如:list、tuple、dict等统称为可迭代对象:Iterable。可以使用方法isinsteance()判断一个对象是否是可迭代对象。
例如: isinstance(obj, Iterable)  判断是不是迭代对象
"""
from collections import Iterable

result = isinstance([], Iterable)
print(result)
result = isinstance((), Iterable)
print(result)
result = isinstance('python', Iterable)
print(result)
result = isinstance(213, Iterable)
print(result)

"""  
结果为:

    True
    True
    True
    False
isinstance(obj,Class)判断某个对象是否属于某个类 来判断一个对象是否是可迭代对象。isinstance(obj, Iterable)
Checking isinstance(obj, Iterable) detects classes that are registered as Iterable or that have an __iter__() method,
but it does not detect classes that iterate with the __getitem__() method.
The only reliable way to determine whether an object is iterable is to call iter(obj).
"""

"""
可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator。next()函数访问每一个对象，直到对象访问完毕返回一个StopIteration异常。
例如: isinstance(obj, Iterator)  判断是不是迭代器
"""
from collections import Iterator

result = isinstance([], Iterator)
print(result)
result = isinstance((), Iterator)
print(result)
result = isinstance((x for x in range(10)), Iterator)
print(result)

"""
结果为:

    False
    False
    True

所有的Iterable都可以通过iter()函数转化为Iterator。
"""

"""
定义迭代器

当自己定义迭代器时，需要定义一个类，类里面包含一个iter()函数，这个函数能够返回一个带next()方法的对象。
例如:
"""


class MyIterable:
    def __iter__(self):
        return MyIterator()


class MyIterator:
    def __init__(self):
        self.num = 0

    def __next__(self):
        self.num += 1
        if self.num >= 10:
            raise StopIteration
        return self.num


class OwnIteror(Iterator):
    def __init__(self, arrs):
        self.index = 0
        self.arrs = arrs

    def __next__(self):
        if self.index > len(self.arrs) - 1:
            raise StopIteration
        else:
            self.index += 1
            return self.arrs[self.index - 1]


# 可迭代对象
class OwnIterable(Iterable):
    def __init__(self, arrs):
        self.arrs = arrs

    def __iter__(self):
        return OwnIteror(self.arrs)


for item in OwnIterable([1, 2, 3, 4, 4, 6]):
    print(item)


my_iterator = MyIterable()
print("aaaaa")
print(isinstance(my_iterator, Iterable))
print(isinstance(iter(my_iterator), Iterator))

a = iter(my_iterator)
while True:
    try:
        b = next(a)
        print(b)
    except StopIteration:
        break


"""
复制迭代器

迭代器当一次迭代完毕后就结束了，在此调用便会引发StopIteration异常。
如果想要将迭代器保存起来，可以使用复制的方法:copy.deepcopy():x = copy.deepcopy(y)，
不可使用赋值的方法，这样是不起作用的。
"""



