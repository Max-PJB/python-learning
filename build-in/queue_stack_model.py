#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/30 16:22
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
import queue

__author__ = 'Max_Pengjb'
start = time.time()

# 下面写上代码块
# put 进  get 出
# 队列
que = queue.Queue()
que.put(1)
que.put(2)
a = que.get()
print(a)
print(que.get())
# 栈，就是个 后进先出 队列
stack = queue.LifoQueue()
stack.put(3)
stack.put(4)
print(stack.get())
print(stack.get())
# queue.PriorityQueue() : 队列，基于优先级
q = queue.PriorityQueue(3)  # 优先级,优先级用数字表示,数字越小优先级越高
q.put((10, 'a'))
q.put((-1, 'b'))
q.put((100, 'c'))
print(q.get())
print(q.get())
print(q.get())

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
