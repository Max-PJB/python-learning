#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/11 16:27
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    最长凹谷100

    过关任务
    评论5

挑战任务

有一维数组X = [8,5,1,6,7,7,3,5]，我们把它画到坐标系中，其中凹下去的部分我们称为X数组的凹谷数组Y，其中凹陷的长度即为凹谷数组的长度（Y的长度大于3），其中持平的部分不计入凹谷数组的长度。如下所示，X有两个凹谷数组Y1 = [8,5,1,6,7]和Y2 = [7,3,5]，长度分别为5和3。我们则需要返回这个数组中的最长凹谷数组的长度，即5，如果数组中不含凹谷，则返回0。

本关任务就是判断系统输入的随机一维数组，返回其最长凹谷数组的长度。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def concave_valley(x):
    # print(x)
    n = len(x)
    count = 0
    if n < 3:
        return 0
    pre = x[0]
    down_or_up = 1
    i = 1

    while i < n:
        ls = 0
        up_l = []
        down_l = []
        while i < n and down_or_up:
            if pre > x[i]:
                down_l.append(pre)
                pre = x[i]
                ls += 1
                i += 1
               # print(11111)
            # elif pre == x[i]:
            #     pre = x[i]
            #     i += 1
            #     break
            #if pre < x[i]:
            elif ls != 0:
                down_l.append(pre)
                ls += 1
                down_or_up = 0
                # print(2222)
            else:
                pre = x[i]
                i += 1
        while i < n and not down_or_up:
            if pre < x[i]:
                up_l.append(x[i])
                pre = x[i]
                ls += 1
                i += 1
                # print(333)
            # elif pre == x[i]:
            #     pre = x[i]
            #     i += 1
            #     break
            # if pre > x[i]:
            else:
                pre = x[i]
                down_or_up = 1
                i += 1
                # print(444)
        count = ls if ls > count else count
        print(down_l, up_l)
    print(count)
    return count


X = [8,5,1,6,7,7,3,5]
# X = [5,2,4,5,8,10]
# X = [8,8,9,8,6,2,8,8,10]
concave_valley(X)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



