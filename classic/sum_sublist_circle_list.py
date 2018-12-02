#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/30 13:55
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  如果数组是循环的，该如何呢

这时分两种情形：

（1）最大的子数组没有跨过vec[n-1]到vec[0]: start < end

（2）最大的子数组跨过vec[n-1]到vec[0]: start > end

对于第二种情形，相当于从原数组中挖掉了一块(vec[end+1], …, vec[start-1]) ,

那么我们只要使挖掉的和最小即可，这就变成了求最小子数组和最大子数组（求最小子数组和最大子数组方法类似)
比较 sum(all)-min(sublist) 和 max(sublist),
-------------------------------------------------
"""
import time
from classic import sum_subList_2_ways

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
# 这里我们实现求最小子数组，然后import之前求最大子数组的代码进来
# 一、分治法
def min_sub1(A):
    """
    :param A:List[int]
    :return: List[(int,int,int)]
    """

    def sub_min(start, end):
        """
        :param start: int
        :param end: int
        :return: List[(int,int,int)]
        """
        if start == end:
            return [(A[start], start, end)]
        else:
            mid = (start + end) // 2
            res_left = sub_min(start, mid)
            res_right = sub_min(mid + 1, end)
            l_min = A[mid]
            l_min_start = mid
            r_min = A[mid + 1]
            r_min_end = mid + 1
            l_ls = 0
            r_ls = 0
            for i in range(mid, start - 1, -1):
                l_ls += A[i]
                if l_ls < l_min:
                    l_min, l_min_start = l_ls, i
            for j in range(mid + 1, end + 1):
                r_ls += A[j]
                if r_ls < r_min:
                    r_min, r_min_end = r_ls, j
            res_over = (l_min + r_min, l_min_start, r_min_end)
            print("res = ", res_left, res_right, res_over)
            smallest = min(res_left[0][0], res_right[0][0], res_over[0])
            res = []
            if res_left[0][0] == smallest:
                res.extend(res_left)
            if res_right[0][0] == smallest:
                res.extend(res_right)
            if res_over[0] == smallest:
                res.append(res_over)
            return res

    return sub_min(0, len(A) - 1)


# 二、动态规划法
def min_sub2(A):
    """
    :param A:List[int]
    :return: List[(int,int,int)]
    """
    if not A:
        return None
    else:
        smallest = A[0]
        pre_min = A[0]
        pre_start = 0
        min_list_interval = [(A[0], 0, 0)]
        for i in range(1, len(A) - 1):
            a = A[i]
            if pre_min + a > a:
                pre_min = a
                pre_start = i
            else:
                pre_min += a
                pass
            min_list_interval.append((pre_min, pre_start, i))
            smallest = smallest if smallest < pre_min else pre_min
        res = list(filter(lambda x: x[0] == smallest, min_list_interval))
        return res


print("--------------方法（一）---------------------")
A_in1 = [1, 2, 3, -3, -4, -3, 1, 2, 3]
res1 = min_sub1(A_in1)
print(res1)
print("--------------方法（二）---------------------")
A_in2 = [1, 2, 3, -3, -4, -3, 1, 2, 3]
res2 = min_sub2(A_in2)
print(res2)

print("--------------循环数组最大和---------------------")
circle_in = [-2, -3, -1]
situation_1 = sum_subList_2_ways.sub_list2(circle_in)
sum_all = sum(circle_in)
situation_2 = list(map(lambda x: (sum_all - x[0], x[2] + 1, x[1] - 1), min_sub2(circle_in)))
print(situation_1, situation_2)
res_max = max(situation_1[0][0], situation_2[0][0])
res = []
if res_max == situation_1[0][0]:
    res.extend(situation_1)
if res_max == situation_2[0][0]:
    res.extend(situation_2)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
