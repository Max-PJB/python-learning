#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/20 
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""
__author__ = 'Max_Pengjb'

import collections


def CreatePoint():
    # 在此处创建并返回一个命名元组实例，有属性x,y，初值都为0
    # Point = collections.namedtuple("Point", "x,y")
    # Point = collections.namedtuple('Point', 'x, y')
    # Point = collections.namedtuple("Point", "x,y")
    # Point = collections.namedtuple("Point", "x y")
    # Point = collections.namedtuple('Point', 'x y')
    return collections.namedtuple('Point', 'x y')(x=2, y=2)


def IncX(p):
    # 在此处对变量p的x坐标进行+1操作，然后返回修改过后的新对象
    return p._replace(x=p.x + 1)


def IncY(p):
    # 在此处对参数p的y坐标进行+1操作，然后返回修改过后的新对象
    return p._replace(y=p.y + 1)


#
def PrintPoint(p):
    # 按照:"当前位置:x = XXX,y = XXX" 的格式打印参数p
    print("当前位置:x = {},y = {}".format(p.x, p.y))


p = CreatePoint()
PrintPoint(p)
p = IncX(p)
PrintPoint(p)
p = IncY(p)
PrintPoint(p)

c = collections.Counter("aaaaabbbbbccccccc")
print(c["c"])
print(c.most_common(2))
c2 = collections.Counter(a=2, b=2, c=1, d=1)
print(c2['a'])
c2['a'] = 10
print(c2['a'])
print(c)
print(c2)
print(c + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2 + c2)
print(c - c2)
for k, v in c2.items():
    print(k, v)
print(list(c2.elements()))
c3 = collections.Counter()
print(c3)

c4 = collections.Counter('which')
print(c4)
c4.subtract('witch')  # subtract elements from another iterable
print(c4)
c4.subtract(collections.Counter('watch'))  # subtract elements from another counter
print(c4)

de = collections.deque()
for i in range(0, 10, 2):
    de.append(i)
    de.appendleft(i+1)
print(list(de))

