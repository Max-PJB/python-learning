#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/22 23:38
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
n = int(input())


class ResIterator(int):
    def __init__(self, nn):
        self.x = nn

    def __next__(self):
        for i in range(2, self.x+1):
            if divmod(self.x, i)[1] == 0:
                self.x = divmod(self.x, i)[0]
                return i
        if self.x == 1:
            raise StopIteration

    def __iter__(self):
        return self

result = ResIterator(n)
print(n, "=", "*".join(map(str, result)))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
