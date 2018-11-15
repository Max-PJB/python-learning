#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/13 22:25
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    螺旋矩阵 II

给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
# 别人的这个改变方向的方法很巧妙啊
def generate_matrix2(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    max_num = n * n
    output = []
    for i in range(n):
        lists = [0 for i in range(n)]
        output.append(lists)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0
    for num in range(1, max_num + 1):
        if output[r][c] == 0:
            output[r][c] = num
        cr, cc = r + dr[di], c + dc[di]
        # if 0 <= cr < n and 0 <= cc < n and output[cr][cc] == 0:
        if n > cr >= 0 == output[cr][cc] and 0 <= cc < n:
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
    return output


def generate_matrix(x):
    i = 0
    j = 0
    ii = 0
    jj = 0
    m = x
    n = x
    res = [[1 for _ in range(x)] for _ in range(x)]
    cnt = 1
    while ii <= i < m and jj <= j < n:
        while ii <= i < m and jj <= j < n:
            res[i][j] = cnt
            cnt += 1
            j += 1
        ii += 1
        j -= 1
        print(i, ii, m, j, jj, n, res, "->")
        i += 1
        while ii <= i < m and jj <= j < n:
            res[i][j] = cnt
            cnt += 1
            i += 1
        n -= 1
        i -= 1
        print(i, ii, m, j, jj, n, res, "\\/")
        j -= 1
        while ii <= i < m and jj <= j < n:
            res[i][j] = cnt
            cnt += 1
            j -= 1
        m -= 1
        j += 1
        print(i, ii, m, j, jj, n, res, "<-")
        i -= 1
        while ii <= i < m and jj <= j < n:
            res[i][j] = cnt
            cnt += 1
            i -= 1
        jj += 1
        i += 1
        print(i, ii, m, j, jj, n, res, "/\\")
        j += 1
    print(res)
    return res


generate_matrix(3)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
