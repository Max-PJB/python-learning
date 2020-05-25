#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/23 22:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块


class FibIterator:
    # 补全这个迭代器的代码，实现要求的功能
    def __init__(self):
        self.m = 0
        self.n = 1

    def __next__(self):
        self.m, self.n = self.n, self.m + self.n
        return self.m

    def __iter__(self):
        return self


fib = FibIterator()
for _ in range(9):
    print(next(fib))

a, b, c, d, e, f = 1, 2, 3, 4, 5, 6
a, b, c, d, e, f = d, e, f, a, b, c
print(a, b, c, d, e, f)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
