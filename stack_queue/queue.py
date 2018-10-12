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


class Queue:
    def __init__(self, length):
        self.front = 0
        self.rear = 0
        self.length = length + 1
        self.queue = [0 for _ in range(self.length)]
        print(str(self.queue))

    def en_queue(self, x):
        print("self.front is = ", self.front, "self.rear is = ", self.rear)
        if (self.rear + 1) % self.length == self.front:
            print("en {} failed".format(x))
        else:
            self.queue[self.rear] = x
            print("en {} success".format(self.queue[self.rear]))
            self.rear = (self.rear + 1) % self.length

    def de_queue(self):
        print("self.front is = ", self.front, "self.rear is = ", self.rear)
        if self.rear == self.front:
            print("null, de failed")
        else:
            print("de {} success".format(self.queue[self.front]))
            self.front = (self.front + 1) % self.length

    def __repr__(self):
        # return str(self.queue)
        if self.front <= self.rear:
            return str(self.queue[self.front:self.rear:])
        else:
            return str(self.queue[self.front:self.length:] + self.queue[:self.rear:])


que = Queue(5)
print(que)
que.en_queue(1)
que.en_queue(2)
print(que)
que.en_queue(3)
que.en_queue(4)
print(que)
que.en_queue(5)
que.en_queue(6)
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)
que.en_queue(7)
print(que)
que.en_queue(8)
print(que)
que.en_queue(9)
print(que)
que.en_queue(10)
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)
que.de_queue()
print(que)

s1 = [1, 2, 3]
s2 = [4]
print(s1 + s2)  # + 有返回值
print(s1.extend(s2))  # extend 灭有返回值
