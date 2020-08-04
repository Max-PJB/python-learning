#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/24 11:17
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       定义一个 order_points 函数，需要传入参数 pts，是一个包含矩形四个点的(x, y)坐标的列表。

对矩形中的四个点进行 一致的排序 是非常重要的，实际的排序可以是任意的，只要它在整个实现过程中是一致的。

对于我来说，我习惯将点按照 “左上，右上，右下，左下” 进行排序。

代码里使用 np.zeros 为四个点分配内存。根据 x 与 y 之和最小找到左上角的点，x 与 y 之和最大找到右下角的点。

然后使用 np.diff 函数，根据 x 与 y 之差（y-x）最小找到右上角的点，x 与 y 之差最大找到左下角的点。

最后将排好序的点返回给调用函数。
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

# transform.py
import numpy as np
import cv2


def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype="float32")

    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # return the ordered coordinates
    return rect
