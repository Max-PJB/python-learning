#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/2 16:24
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    python中zip 和 izip , izip_longest比较
     zip是build-in方法

而izip是itertools中的一个方法
-------------------------------------------------
"""
import time
import itertools

__author__ = 'Max_Pengjb'

# 下面写上代码块
""" 
zip
文档中这样描述：

Make an iterator that aggregates elements from each of the iterables. Like zip() except 
that it returns an iterator instead of a list. Used for lock-step iteration over several iterables at a time.

把不同的迭代器的元素聚合到一个迭代器中。类似zip（）方法，但是返回的是一个迭代器而不是一个list。
用于同步迭代一次几个iterables

因为返回的是一个迭代器，并且同步迭代，所以速度比较快。

 izip_longest

Make an iterator that aggregates elements from each of the iterables. 
If the iterables are of uneven length, missing values are filled-in with fillvalue. 
Iteration continues until the longest iterable is exhausted

也就是说这个zip_longest方法使用izip一样的原理，但是会使用最长的迭代器来作为返回值的长度，
并且可以使用fillvalue来制定那些缺失值的默认值
"""
a = range(10)
b = range(10)
start = time.time()
x = zip(a, b)
print(a)
end = time.time()
print('Running zip time: %s Seconds' % (start - end))

start = time.time()
y = itertools.zip_longest(a, b)
print(b)
end = time.time()
print('Running zip_tools time: %s Seconds' % (start - end))
# 上面中间写上代码块
print(list(x))
print(list(y))
