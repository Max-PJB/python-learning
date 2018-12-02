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

__author__ = 'Max_Pengjb'
start = time.time()
# 下面写上代码块
"""
求不超过某个正整数x内的所有素数，有一个著名的算法——埃拉托斯特尼筛法。其算法描述为：
    先用一个数组vis，把不大于该正整数x的所有正整数标记为0，表示没有访问。
    然后从第一个素数2开始遍历整个区间，如果当前访问的数没有访问过，则可以认为它是一个素数，
那么就将它在该区间内所有的倍数全部标记为已访问，这样就保证外部的循环发现的没有访问过的数都是素数。
其具体实现如下述代码所示：
"""


def prime_numbers_below1(x):
    ss = [0 for _ in range(x + 1)]
    prime = []
    for i in range(2, x + 1):
        if ss[i] == 0:
            prime.append(i)
        for j in range(i * 2, x + 1, i):
            ss[j] = 1
    return prime


# 欧拉筛法，这里只给出其代码实现，希望大家能仔细去体会。
def prime_numbers_below2(x):
    vis = [0 for i in range(x + 1)]
    prime_table = []
    ln = 0
    for num in range(2, x + 1):
        if vis[num] == 0:
            prime_table.append(num)
            ln += 1
        for j in range(ln):
            if num * prime_table[j] > x:
                break
            vis[num * prime_table[j]] = 1
            if num % prime_table[j] == 0:
                break
    return prime_table


"""
判断一个正整数是不是素数（快速方法）：
质数有一个特点，就是它总是等于 6x-1 或者 6x+1，其中 x 是大于等于1的自然数。

如何论证这个结论呢，其实不难。
首先 6x 肯定不是质数，因为它能被 6 整除；
其次 6x+2 肯定也不是质数，因为它还能被2整除；
依次类推，6x+3 肯定能被 3 整除；6x+4 肯定能被 2 整除。
那么，就只有 6x+1 和 6x+5 (即等同于6x-1) 可能是质数了。
所以循环的步长可以设为 6，然后每次只判断 6 两侧的数即可。
"""


def is_prime(x):
    if x < 2:
        return False
    elif x <= 3:
        return True
    k = x % 6
    if k != 1 and k != 5:
        return False
    sqrt_x = int(math.sqrt(x))
    for i in range(5, sqrt_x + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True
# print(prime_numbers_below1(9999999))
print(prime_numbers_below2(999))

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))