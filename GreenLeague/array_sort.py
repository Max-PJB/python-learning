#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/11 15:03
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    数组排序100

    过关任务
    评论4

挑战任务

本关挑战任务是对一个数组进行排序，排序需要遵守一些规则：

    先对数组从左到右，相邻元素进行比较，如果第一个比第二个大，就交换它们，进行一个升序排序；
    再对数组从右到左，相邻元素进行比较，如果第一个比第二个小，就交换它们，进行一个降序排序；
    以此类推，持续的、依次的改变排序的方向，并不断缩小没有排序的数组范围；

按照这种规则依次给整个数组排序，并将排序过程打印到控制台。

比如给出一组数据4，1，3，5，2，排序过程如下：

最后得到结果：1 2 3 4 5。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def array_sort(xlist):
    count = 1
    is_do = 0
    while count != 0:
        count = 0
        for i in range(len(xlist) - 1):
            if xlist[i] > xlist[i + 1]:
                count += 1
                is_do = 1
                xlist[i], xlist[i + 1] = xlist[i + 1], xlist[i]
                print_sb(xlist)
        for i in range(len(xlist) - 1, 0, -1):
            if xlist[i] < xlist[i - 1]:
                count += 1
                is_do = 1
                xlist[i], xlist[i - 1] = xlist[i - 1], xlist[i]
                print_sb(xlist)
        if count == 0:
            break
    if not is_do:
        print_sb(xlist)


def print_sb(xx):
    for x in range(len(xx) - 1):
        print(xx[x], '', end='')
    print(xx[-1])


# list_in = [2, 3, 4, 5, 1]
list_in = [1, 5, 4, 3, 2, 6]
# list_in = [4, 1, 3, 5, 2]
# list_in = [1, 2, 3]
array_sort(list_in)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
