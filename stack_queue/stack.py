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

__author__ = 'Max_Pengjb'


class Stack:
    def __init__(self, length):
        self.length = length
        self.stack = []
        self.top = 0

    def push(self, x):
        if self.top >= self.length:
            print("push {} failed".format(x))
            pass
        else:
            self.stack.append(x)
            self.top += 1
            print("push {} success".format(x))

    def pop(self):
        if self.top > 0:
            self.top -= 1
            print("pop {} success".format(self.stack.pop(self.top)))
        else:
            print("pop failed")
        pass

    def __repr__(self):
        return str(self.stack)

    pass


st = Stack(5)
st.push(1)
print(st)
st.pop()
print(st)
st.pop()
print(st)
st.push(2)
print(st)
st.push(3)
print(st)
st.push(4)
print(st)
st.push(5)
print(st)
st.push(6)
print(st)
st.push(7)
print(st)
st.pop()
print(st)
st.pop()
print(st)
st.pop()
print(st)
st.pop()
print(st)
st.pop()
print(st)
st.pop()
print(st)
