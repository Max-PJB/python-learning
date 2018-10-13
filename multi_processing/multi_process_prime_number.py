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
import math
from multiprocessing import cpu_count
from multiprocessing import Pool

__author__ = 'Max_Pengjb'
start = time.time()
# 下面写上代码块
# 用多进程实现求区间[1,n]里素数的个数。


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 计算给定区间含有多少个质数
def howMany(T):
    sum = 0;
    for i in range(T[0], T[1] + 1):
        if isPrime(i):
            sum += 1
    return sum


# 对整个数字空间N进行 分段CPU_COUNT
def seprateNum(N, CPU_COUNT):
    list = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)] for i in range(0, CPU_COUNT)]
    list[0][0] = 1
    if list[CPU_COUNT - 1][1] < N:
        list[CPU_COUNT - 1][1] = N
    return list


if __name__ == '__main__':
    N = int(input())
    # 多进程
    CPU_COUNT = cpu_count()  ##CPU内核数 本机为8
    pool = Pool(CPU_COUNT)
    sepList = seprateNum(N, CPU_COUNT)
    result = []
    for i in range(CPU_COUNT):
        result.append(pool.apply_async(howMany, (sepList[i],)))
    pool.close()
    pool.join()
    ans = 0
    list = [res.get() for res in result]
    print(sum(list), end='')  # end='' 表示取消 /n

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



