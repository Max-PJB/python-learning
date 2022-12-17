#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/30 19:59
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    python 内置的排列组合函数product 笛卡尔积　　（有放回抽样排列）

permutations 排列　　（不放回抽样排列）

combinations 组合,没有重复　　（不放回抽样组合）

combinations_with_replacement 组合,有重复　　（有放回抽样组合）

详细的参见官网。



import itertools
for i in itertools.product('ABCD', repeat = 2):
 print(i)
('A', 'A') ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'A') ('B', 'B') ('B', 'C') ('B', 'D') ('C', 'A') ('C', 'B') ('C', 'C') ('C', 'D') ('D', 'A') ('D', 'B') ('D', 'C') ('D', 'D')

for i in itertools.permutations('ABCD', 2):
print(i)
('A', 'B') ('A', 'C') ('A', 'D') ('B', 'A') ('B', 'C') ('B', 'D') ('C', 'A') ('C', 'B') ('C', 'D') ('D', 'A') ('D', 'B') ('D', 'C')

for i in itertools.combinations('ABCD', 2):
    print(i)
('A', 'B') ('A', 'C') ('A', 'D') ('B', 'C') ('B', 'D') ('C', 'D')

for i in itertools.combinations_with_replacement('ABCD', 2):
     print(i)
('A', 'A') ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'B') ('B', 'C') ('B', 'D') ('C', 'C') ('C', 'D') ('D', 'D')
     还有就是，combinations和permutations返回的是对象地址，原因是在python3里面，
     返回值已经不再是list,而是iterators（迭代器）,
     所以想要使用，只用将iterator 转换成list 即可，
     还有其他一些函数返回的也是一个对象，需要list转换，比如 list(map())等 。
-------------------------------------------------
"""
import time
import itertools

__author__ = 'Max_Pengjb'
start = time.time()

# 下面写上代码块

for i in itertools.product('ABCD', repeat=2):
    print(i)

for i in itertools.permutations('ABCD', 2):
    print(i)

for i in itertools.combinations('ABCD', 2):
    print(i)

for i in itertools.combinations_with_replacement('ABCD', 2):
    print(i)

print(len(list(itertools.combinations(range(3), 1))))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
