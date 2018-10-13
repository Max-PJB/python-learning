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
import math
__author__ = 'Max_Pengjb'

if __name__ == '__main__':
    N = int(input())
    CPU_COUNT = 8  ## 线程数设为 8
    num = 0

    def isCompositive(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False

    # 对整个数字空间N进行 分段CPU_COUNT
    def seprateNum(N, CPU_COUNT):
        list = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)] for i in range(0, CPU_COUNT)]
        list[0][0] = 1
        if list[CPU_COUNT - 1][1] < N:
            list[CPU_COUNT - 1][1] = N
        return list

    # 计算给定区间含有多少个质数
    def howMany(T):
        sum = 0;
        for i in range(T[0], T[1] + 1):
            if isCompositive(i):
                sum += 1
        return sum

    def thread_do(sepList):
        global num
        for i in range(sepList[0], sepList[1]+1):
            if isCompositive(i):
                num += 1


    sepList = seprateNum(N, CPU_COUNT)
    for i in range(CPU_COUNT):
        t = threading.Thread(target=thread_do, args=(sepList[i],))
        t.start()
        t.join()
    print(num)
