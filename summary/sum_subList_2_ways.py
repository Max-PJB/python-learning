#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/30 10:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  数组 A， 求 A 的子集中所有项的和最大的那个
         [1,-2,3] 有子集[1],[1,-2][1,-2,3][-2][-2,3][3] 最大的是 【3】
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
# 一、分治法，A 在点 n/2 处 分成 左右两块 A0= A[0]~A[n/2-1]，和 A1= A[n/2]~A[n]。再考虑结果可能横跨A0和A1
# 分别求 sublist(A0) 最大子集，sublist(A1)最大子集，还有横跨 A0 A1 的情况（在A中包含A[n/2-1]向左找最大和，A[n/2]向右找最大和
# 所以，最后结果只有三种情况：
# 1. res = sublist(A0)
# 2. res = sublist(A1)
# 3. res = sublist( A0<-A[n/2-1],A[n/2]->a[n] )

def sub_list(A):
    """
    :param A:List[int]
    :return: List[(int,int,int)]
    """

    def subsub(start, end):
        """
        :param start:int
        :param end: int
        :return: List[(int,int,int)]
        """
        if start == end:
            left = right = start
            print("start==end= ", [(A[start], left, right)])
            return [(A[start], left, right)]
        else:
            mid = (end + start) // 2
            # 算 A0
            print("fenfenfen", A[start:mid + 1], A[mid + 1:end + 1])
            res_left = subsub(start, mid)
            # 算 A1
            res_right = subsub(mid + 1, end)
            # 算横跨 A0 A1 且 同时包含 mid ， mid+1
            over_left = mid
            l_max = A[mid]
            over_right = mid + 1
            r_max = A[mid + 1]
            ls = 0
            for i in range(mid + 1, end + 1):
                ls += A[i]
                if ls > r_max:
                    r_max = ls
                    over_right = i
            ls = 0
            for i in range(mid, start - 1, -1):
                ls += A[i]
                if ls > l_max:
                    l_max = ls
                    over_left = i
            over_sum = l_max + r_max
            res_over = (over_sum, over_left, over_right)
            bigest = max(res_left[0][0], res_right[0][0], over_sum)
            res = []
            if bigest == res_left[0][0]:
                res.extend(res_left)
            if bigest == res_right[0][0]:
                res.extend(res_right)
            if bigest == over_sum:
                res.append(res_over)
            print("res = ", res_left, res_right, res_over, bigest, res)
            return res

    return subsub(0, len(A) - 1)


print("--------------方法（一）---------------------")
A_in1 = [1, 2, 3, -3, -4, -3, 1, 2, 3]
res1 = sub_list(A_in1)
print(res1)


# 二、动态规划
# 数组为vec[]，设dp[i] 是以vec[i]结尾的子数组的最大和，
# 对于元素vec[i+1], 它有两种选择：
# 1.vec[i+1]接着前面的子数组构成最大和
# 2.vec[i+1]自己单独构成子数组。意思就是前面的一堆和是负数,并且还是比自己还小的负数（想想，如果前面是正数，那肯定就是加上它啊)
# 则dp[i+1] = max{dp[i]+vec[i+1],  vec[i+1]}
def sub_list2(A):
    """
    :param A:List[int]
    :return: List[(int,int,int)]
    """
    n = len(A)
    if n == 0:
        return None
    else:
        cur_most = A[0]
        cur_start = 0
        biggest = A[0]
        max_list_interval = [(cur_most, 0, 0)]
        for cur_end in range(1, n):
            if cur_most + A[cur_end] > A[cur_end]:
                cur_most += A[cur_end]
            else:
                cur_most = A[cur_end]
                cur_start = cur_end
            max_list_interval.append((cur_most, cur_start, cur_end))
            biggest = biggest if biggest >= cur_most else cur_most
    print(max_list_interval)
    res = list(filter(lambda x: x[0] == biggest, max_list_interval))
    return res


print("--------------方法（二）---------------------")
A_in2 = [1, 2, 3, -3, -4, -3, 1, 2, 3]
res2 = sub_list2(A_in2)
print(res2)
# 取负数，再求最大就是求最小了
# A_in3 = [-1, -2, -3, 3, 4, 3, -1, -2, -3]
A_in3 = [-1]
res3 = sub_list2(A_in3)
print(res3)
# he = sum(A_in2)
# res3 = list(map(lambda x:(he+x[0],x[2],x[1]),res3))
# print(res3)
# if he+res3[0][0] == res2[0][0]:

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
