#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/13 21:46
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   螺旋矩阵

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def spiral_order(matrix):
    if not matrix:
        return matrix
    i = 0
    j = 0
    ii = 0
    jj = 0
    m = len(matrix)
    n = len(matrix[0])
    res = []
    while ii <= i < m and jj <= j < n:
        while ii <= i < m and jj <= j < n:
            res.append(matrix[i][j])
            j += 1
        ii += 1
        j -= 1
        print(i,ii,m,j,jj,n,res,"->")
        i += 1
        while ii <= i < m and jj <= j < n:
            res.append(matrix[i][j])
            i += 1
        n -= 1
        i -= 1
        print(i,ii,m,j,jj,n,res,"\\/")
        j -= 1
        while ii <= i < m and jj <= j < n:
            res.append(matrix[i][j])
            j -= 1
        m -= 1
        j += 1
        print(i,ii,m,j,jj,n,res,"<-")
        i -= 1
        while ii <= i < m and jj <= j < n:
            res.append(matrix[i][j])
            i -= 1
        jj += 1
        i += 1
        print(i,ii,m,j,jj,n,res,"/\\")
        j += 1
    print(res)
    return res


matrix_in = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
spiral_order(matrix_in)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
