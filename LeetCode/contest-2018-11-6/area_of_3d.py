#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/6 21:00
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   883 三维形体投影面积

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Easy

在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。

投影就像影子，将三维形体映射到一个二维平面上。

在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回所有三个投影的总面积。
示例 1：

输入：[[2]]
输出：5

示例 2：

输入：[[1,2],[3,4]]
输出：17

示例 3：

输入：[[1,0],[0,2]]
输出：8

示例 4：

输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：14

示例 5：

输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：21

-------------------------------------------------
"""
import time
from functools import reduce

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def area_of_3d(grid):
    xy = reduce(lambda x, y: x + len(y) - y.count(0), grid, 0)
    print(xy)
    xz = reduce(lambda x, y: x + max(y), grid, 0)
    print(xz)
    # list 求转置的方法 [[row[i] for row in grid] for i in range(len(grid[0]))]
    # 更高级的可以用 zip(*grid)
    # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元,组然后返回由这些元组组成的列表
    # 利用 * 号操作符，可以将元组解压为列表
    # 这里就是 * 将 grid 解压为 grid[0],grid[1],grid[2],..... 然后在 zip(grid[0],grid[1],grid[2]......)
    yz = reduce(lambda x, y: x + max(y), zip(*grid), 0)
    print(yz)
    print(list(zip(*grid)))
    return xy + xz + yz


# grid_in = [[1, 2], [3, 4]]
grid_in = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(area_of_3d(grid_in))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
