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
import threading
import time
__author__ = 'Max_Pengjb'
"""
互斥锁

python 提供了一种 “相互排斥”的方法（互斥锁即由此得名）。两个线程不能同时对同一个互斥对象加锁。

互斥锁是这样工作的。如果线程 a 试图锁定一个互斥对象，而此时线程 b 已锁定了同一个互斥对象时，线程 a 就将进入睡眠状态。一旦线程 b 释放了互斥锁，线程 a 就能够锁定这个互斥对象。同样地，当线程 a 正锁定互斥对象时，如果线程 c 试图锁定互斥对象的话，线程 c 也将临时进入睡眠状态。对已锁定的互斥对象上调用互斥锁的所有线程都将进入睡眠状态，这些睡眠的线程将“排队”访问这个互斥对象。

那么上面那一个问题就可以使用互斥锁来解决。
"""


def run(n):
    lock.acquire()  # 获取锁
    global num
    print(n)
    num += 1
    lock.release()  # 释放锁


lock = threading.Lock()  # 实例化一个锁对象
num = 0
t_obj = []
for i in range(20000):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()
    t_obj.append(t)
for t in t_obj:
    t.join()
print("num:", num)
