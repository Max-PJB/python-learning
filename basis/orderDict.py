#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/21 
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""
import collections

__author__ = 'Max_Pengjb'

data = [('a', 1), ('b', 3), ('c', 2)]
od = collections.OrderedDict(sorted(data, key=lambda s: s[0]))  # 按数据中key值的大小排序
print(od)
od = collections.OrderedDict(sorted(data, key=lambda s: s[1]))  # 按数据中value值的大小排序
print(od)
# 这里使用的sorted函数，它返回对一个可迭代对象排序后的结果，如果可迭代对象的元素不能直接进行比较（比如元素是一个list或tuple等），则需要指定key函数。
#
# 这里使用lambda表达式lambda s:s[0]和lambda s:s[1]，分别指定key为data中每个元素（tuple类型）的第一个元素和第二个元素。
od['a'] = 4
print(od)

dt = {'a': 1, 'b': 3, 'c': 2}
print(dt.items())
for ii in dt.items():
    print(ii[1])

dt = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
oo = collections.OrderedDict(dt)
print(oo)
# dictionary sorted by key
"""
看到没有， dict 变成 orderedDict 需要用items(), sorted()之后变成了list
"""
odd = collections.OrderedDict(sorted(dt.items(), key=lambda t: t[0]))
print(odd)
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
odd2 = sorted(odd.items(), key=lambda x: x[1])
print(odd2)
print(odd2[0])

# OrderedDict对象的字典对象，如果其顺序不同那么Python也会把他们当做是两个不同的对象，请看事例：
print('Regular dictionary:')
d2 = {}
d2['a'] = 'A'
d2['b'] = 'B'
d2['c'] = 'C'

d3 = {'c': 'C', 'a': 'A', 'b': 'B'}
print(d2 == d3)

print('\nOrderedDict:')
d4 = collections.OrderedDict()
d4['a'] = 'A'
d4['b'] = 'B'
d4['c'] = 'C'

d5 = collections.OrderedDict()
d5['c'] = 'C'
d5['a'] = 'A'
d5['b'] = 'B'

print(d4 == d5)

#下面可以看到，当oderedDIct和普通的dict比较的时候，顺序其实是无关的，也就是先把 oderedDict转为普通dict
print(d2 == d4)
print(d3 == d4)
print(d2 == d5)
print(d3 == d5)

"""
输出：
Regular dictionary:
True
OrderedDict:
False
True
True
True
True
"""
dict11 = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "a5": 5}
list11 = [("a1", 1, 2), ("a2", 2, 3), ("a3", 3, 3), ("a4", 4, 3), ("a5", 5, 3)]
print("dict11 :")
print(dict11.items())
for k, v in dict11:
    print(k, v)
print("list11 :")
# print(list11.items()) list并没有items方法
for k, v, m in list11:
    print(k, v, m)
print("list11 for k in list11 :")
for k in list11:
    print(k)

