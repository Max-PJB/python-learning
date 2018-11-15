#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/11 15:43
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       病毒区域的个数100

    过关任务
    评论4

挑战任务

某地区爆发病毒，给定一个矩阵，x代表隔离墙，o代表病毒，病毒区域是由它水平方向或垂直方向上相邻的病毒连接而成，斜角连接不会构成病毒区域。你要计算出矩阵中有几个病毒区域（假设矩阵周边是被隔离墙包围的）。
编程要求

请在右侧编辑器中填充代码，补全virusArea(self,n,m,area):函数，对输入的矩阵进行计算，返回“病毒区域”的个数，函数参数说明如下：
n：矩阵的行
m：矩阵的列
area：待计算的矩阵
测试说明

样例1：

输入：

4 5
x o x x x
x x x o x
x x o o x
x x x x x

输出：2

样例2：

输入：

4 4
o o x x
x x x o
o o o x
x o x o

输出：4

样例3：

输入：

4 6
x o x o x x
x x x o o x
x o x x x x
x o x o o x

输出：4
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def virus_area(n, m, area):
    area_dict = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    stack = []
    for i in range(n):
        for j in range(m):
            if not area_dict[i][j] and area[i][j] == "o":
                stack.append([i, j])
                count += 1
                while stack:
                    ls = stack.pop()
                    ii = ls[0]
                    jj = ls[1]
                    if ii - 1 >= 0:
                        if area_dict[ii - 1][jj] == 0:
                            area_dict[ii - 1][jj] = 1
                            if area[ii - 1][jj] == "o":
                                stack.append([ii - 1, jj])
                    if jj - 1 >= 0:
                        if area_dict[ii][jj - 1] == 0:
                            area_dict[ii][jj - 1] = 1
                            if area[ii][jj - 1] == "o":
                                stack.append([ii, jj - 1])
                    if ii + 1 < n:
                        if area_dict[ii + 1][jj] == 0:
                            area_dict[ii + 1][jj] = 1
                            if area[ii + 1][jj] == "o":
                                stack.append([ii + 1, jj])
                    if jj + 1 < m:
                        if area_dict[ii][jj + 1] == 0:
                            area_dict[ii][jj + 1] = 1
                            if area[ii][jj + 1] == "o":
                                stack.append([ii, jj + 1])
    print(count)
    return count


# area_in = [["x", "o", "x", "x", "x"], ["x", "x", "x", "o", "x"], ["x", "x", "o", "o", "x"], ["x", "x", "x", "x", "x"]]
area_in = [["o", "o", "x", "x"],["x", "x", "x", "o"],["o", "o", "o", "x"],["x", "o","x", "o"]]
virus_area(4, 4, area_in)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
