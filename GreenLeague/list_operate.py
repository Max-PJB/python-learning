#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/11 19:31
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :     数列操作200

    过关任务
    评论6

挑战任务

给定一个长度为N的数组A[]。对于子序列A[L], A[L+1], ..., A[R]中，这里定义以下两个费用：

    左费用定义为：

Lcost=∑i=LRA[i]×(i−L+1)L_{cost} = \sum_{i=L}^{R}{A[i] \times (i - L + 1)}L​cost​​=∑​i=L​R​​A[i]×(i−L+1)

    右费用定义为：

Rcost=∑i=LRA[i]×(R−i+1)R_{cost} = \sum_{i=L}^{R}{A[i] \times (R - i + 1)}R​cost​​=∑​i=L​R​​A[i]×(R−i+1)

现给定M个对序列的操作，每个操作有以下形式：

C x y：将A[x]修改为y；
L x y：求区间A[x], ..., A[y]的左费用；
R x y：求区间A[x], ..., A[y]的右费用。

要求按照顺序处理每个请求，并且求出所有L操作和R操作的答案的和。因为答案可能会非常大，只要返回最终答案对1e9+7取模的结果即可。
    data = {1, 2, 3, 4, 5};
    operations = {
            {'L', 1, 3},
            {'C', 1, 10},
            {'R', 1, 3}};
输出：
60
样例解释：
最开始时要处理的数组为{1, 2, 3, 4, 5}
然后求L 1 3：2*(1-1+1) + 3*(2-1+1) + 4*(3-1+1) = 20
然后求C 1 10：数组变为{1, 10, 3, 4, 5}
然后求R 1 3：10*(3-1+1) + 3*(3-2+1) + 4*(3-3+1) = 40
最后结果为20 + 40 = 60
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Operation:
    def __init__(self, op, x, y):
        self.op = op
        self.x = x
        self.y = y


def list_operate(data, operations):
    res = 0
    l_dict = {}
    r_dict = {}
    for opera in operations:
        if opera.op == "C":
            data[opera.x] = opera.y
            l_dict = {}
            r_dict = {}
            # print("do C", l_dict, r_dict)
        elif opera.op == "L":
            # print(opera.op, opera.x, opera.y, left_sum(data[opera.x:opera.y + 1:]))
            if opera.x in l_dict:
                if opera.y in l_dict[opera.x]:
                    l_sum = l_dict[opera.x][opera.y]
                    res += l_sum
                    # print("do L in dict x y", l_dict, r_dict)
                else:
                    gap = 10 ** 9 + 7
                    k = 0
                    for i in l_dict[opera.x].keys():
                        ls = abs(i - opera.y)
                        if ls < gap:
                            k = i
                            gap = ls
                    if k < opera.y:
                        l_sum = l_dict[opera.x][k] + left_sum(data[k + 1:opera.y + 1:]) + sum(
                            data[k + 1:opera.y + 1:]) * (k - opera.x + 1)
                    # else k > opera.y
                    else:
                        l_sum = l_dict[opera.x][k] - left_sum(data[opera.y + 1:k + 1:]) - sum(
                            data[opera.y + 1:k + 1:]) * (
                                        opera.y - opera.x + 1)
                l_dict[opera.x] = {opera.y: l_sum}
                # print("do L in dict x", l_dict, r_dict)
                res += l_sum
            # else opera.x not in l_dict
            else:
                l_sum = left_sum(data[opera.x:opera.y + 1:])
                l_dict[opera.x] = {opera.y: l_sum}
                res += l_sum
                # print("do L not in dict", l_dict, r_dict)
        # opera.op == "R":
        else:
            # print(opera.op, opera.x, opera.y, right_sum(data[opera.x:opera.y + 1:]))
            if opera.y in r_dict:
                if opera.x in r_dict[opera.y]:
                    l_sum = r_dict[opera.y][opera.x]
                    res += l_sum
                    # print("do R in dict x y", l_dict, r_dict)
                else:
                    gap = 10 ** 9 + 7
                    k = 0
                    for i in r_dict[opera.y].keys():
                        ls = abs(i - opera.x)
                        if ls < gap:
                            k = i
                            gap = ls
                    if opera.x < k:
                        r_sum = r_dict[opera.y][k] + right_sum(data[opera.x:k:]) + sum(data[opera.x:k:]) * (
                                opera.y - k + 1)
                        r_dict[opera.y] = {opera.x: r_sum}
                        res += r_sum
                    # else opera.x > k:
                    else:
                        r_sum = r_dict[opera.y][k] - right_sum(data[k:opera.x:]) - sum(
                            data[k:opera.x:]) * (opera.y - opera.x + 1)
                        res += r_sum
                        r_dict[opera.y] = {opera.x: r_sum}
                    # print("do R in dict y", l_dict, "r_dict:", r_dict)
            # else:opera.y not in r_dict:
            else:
                r_sum = right_sum(data[opera.x:opera.y + 1:])
                r_dict[opera.y] = {opera.x: r_sum}
                res += r_sum
                # print("do R not in dict", l_dict, r_dict)
    res = res % (10 ** 9 + 7)
    # print(res)
    return res


def lr_sum(x_list):
    res = 0
    for i, j in enumerate(x_list):
        res += (i + 1) * j
    return res, sum(x_list) * (len(x_list) + 1) - res


def left_sum(x_list):
    res = 0
    for i, j in enumerate(x_list):
        res += (i + 1) * j
    return res


def right_sum(x_list):
    res = 0
    n = len(x_list)
    for i, j in enumerate(x_list):
        res += (n - i) * j
    return res


# 另一个方法
def list_operate2(data, operations):
    n = len(data)
    data_dict = dict(zip([x for x in range(n)], zip(data, [0 for _ in range(n)])))
    # print(data_dict)
    res = 0
    for opera in operations:
        if opera.op == "C":
            res += data_dict[opera.x][0] * data_dict[opera.x][1]
            data_dict[opera.x] = (opera.y, 0)
            # print(data_dict)
            # print(res)
        if opera.op == "L":
            for cnt, x in enumerate(range(opera.x, opera.y + 1)):
                data_dict[x] = (data_dict[x][0], data_dict[x][1] + cnt + 1)
                # print("L", data_dict)
        if opera.op == "R":
            for cnt, x in enumerate(range(opera.y, opera.x - 1, -1)):
                data_dict[x] = (data_dict[x][0], data_dict[x][1] + cnt + 1)
                # print("R cnt x", cnt, x, data_dict)
    for i in range(n):
        res += data_dict[i][0]*data_dict[i][1]
    # print(res)
    return res


data_in = [1, 2, 3, 4, 5]
a = Operation('L', 1, 3)
b = Operation('C', 1, 10)
c = Operation('R', 1, 3)
d1 = Operation('C', 3, 6)
d2 = Operation('L', 2, 6)
d3 = Operation('C', 7, 19)
d4 = Operation('C', 1, 18)
d5 = Operation('R', 7, 8)
d6 = Operation('L', 7, 7)
d7 = Operation('L', 4, 9)
d8 = Operation('R', 5, 5)
d9 = Operation('R', 2, 8)
d10 = Operation('R', 2, 8)
operations_in = [a, b, c]
data_in2 = [16, 15, 10, 2, 18, 16, 6, 5, 12, 19]
operations_in2 = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
# print(list_operate(data_in, operations_in))
# print(list_operate(data_in2, operations_in2))
print(list_operate2(data_in2, operations_in2))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
