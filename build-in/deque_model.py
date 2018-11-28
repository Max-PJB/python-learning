#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/28 10:20
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    collections.deque 双端队列
                基本操作和 List 差不多，多了 popleft appendleft  extendleft 三个左端快捷操作的方法
-------------------------------------------------
"""
import time
from collections import deque

__author__ = 'Max_Pengjb'
start = time.time()

# 下面写上代码块
d = deque()
# append(往右边添加一个元素)
d.append(1)
d.append(2)
print(d)
# appendleft（往左边添加一个元素）
d.append(3)
d.appendleft(4)
print(d)
# clear(清空队列)
d.clear()
print(d)
# count(返回指定元素的出现次数)
d.append(1)
d.append(1)
print(d.count(1))
# extend(从队列右边扩展一个列表的元素)
d.extend([3,4,5])
print(d)
# extendleft(从队列左边扩展一个列表的元素)
d.extendleft([6,7,7])
print(d)
# index（查找某个元素的索引位置）
d.extend(['a','b','c','d','e'])
print(d)
print(d.index('e'))
print(d.index('c',9,11))  #指定查找区间
# insert（在指定位置插入元素）
d.insert(2,'z')
print(d)
# pop（获取最右边一个元素，并在队列中删除）
x = d.pop()
print(x,d)
# popleft（获取最左边一个元素，并在队列中删除）
x = d.popleft()
print(x,d)
# remove（删除指定元素）
d.remove('c')
print(d)
# reverse（队列反转）
d.reverse()
print(d)
# rotate（把右边元素放到左边）
d.rotate(2)   #指定次数，默认1次
print(d)

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



