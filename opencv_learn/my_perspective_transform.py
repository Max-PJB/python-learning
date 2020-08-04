#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/22 10:03
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       https://blog.csdn.net/fengxueniu/article/details/77964375?%3E
    opencv中提供了getPerspectiveTransform函数来获取由四对点间的转换矩阵，输出矩阵为3*3，
    同时也提供了warpPerspective函数来对通过变换矩阵来对图像进行透视变换的操作，
    同时还提供了perspectiveTransform来提供对点的转换
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import cv2
import numpy as np


def rad(x):
    return x * np.pi / 180


def perspective_transform(image, ax, ay, az, af=42):
    # 原图的四个顶点
    th, tw = image.shape[0:2]
    vertexes = np.array([(0, 0), (tw - 1, 0), (tw - 1, th - 1), (0, th - 1)], dtype=np.float32)
    # 扩展图像，保证内容不超出可视范围 https://blog.csdn.net/chezhai/article/details/53229699
    img = cv2.copyMakeBorder(image, 200, 200, 200, 200, cv2.BORDER_CONSTANT, 0)
    vertexes += 200
    # print(vertexes)
    # for v in vertexes:
    #     cv2.circle(img, tuple((v[1],v[0])), 6, (0, 0, 255), -1)
    cv2.imshow("original", img)
    h, w = img.shape[0:2]

    anglex = ax
    angley = ay
    anglez = az
    fov = af

    z = np.sqrt(h ** 2 + w ** 2) / 2 / np.tan(rad(fov / 2))
    # 齐次变换矩阵
    rx = np.array([[1, 0, 0, 0],
                   [0, np.cos(rad(anglex)), -np.sin(rad(anglex)), 0],
                   [0, -np.sin(rad(anglex)), np.cos(rad(anglex)), 0, ],
                   [0, 0, 0, 1]], np.float32)

    ry = np.array([[np.cos(rad(angley)), 0, np.sin(rad(angley)), 0],
                   [0, 1, 0, 0],
                   [-np.sin(rad(angley)), 0, np.cos(rad(angley)), 0, ],
                   [0, 0, 0, 1]], np.float32)

    rz = np.array([[np.cos(rad(anglez)), np.sin(rad(anglez)), 0, 0],
                   [-np.sin(rad(anglez)), np.cos(rad(anglez)), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]], np.float32)

    r = rx.dot(ry).dot(rz)

    # 四对点的生成
    pcenter = np.array([w / 2, h / 2, 0, 0], np.float32)

    p1 = np.array([0, 0, 0, 0], np.float32) - pcenter
    p2 = np.array([h, 0, 0, 0], np.float32) - pcenter
    p3 = np.array([0, w, 0, 0], np.float32) - pcenter
    p4 = np.array([h, w, 0, 0], np.float32) - pcenter

    dst1 = r.dot(p1)
    dst2 = r.dot(p2)
    dst3 = r.dot(p3)
    dst4 = r.dot(p4)

    list_dst = [dst1, dst2, dst3, dst4]

    org = np.array([[0, 0],
                    [h, 0],
                    [0, w],
                    [h, w]], np.float32)

    dst = np.zeros((4, 2), np.float32)

    # 投影至成像平面
    for i in range(4):
        dst[i, 0] = list_dst[i][0] * z / (z - list_dst[i][2]) + pcenter[0]
        dst[i, 1] = list_dst[i][1] * z / (z - list_dst[i][2]) + pcenter[1]

    warpR = cv2.getPerspectiveTransform(org, dst)
    result = cv2.warpPerspective(img, warpR, (w, h))
    # 获取四个顶点变换后的新坐标 这个 perspectiveTransform 函数有一个坑，需要三维数据
    # https://stackoverflow.com/questions/27585355/python-open-cv-perspectivetransform
    points = cv2.perspectiveTransform(vertexes[None, :, :], warpR)
    # for v in points[0]:
    #     cv2.circle(result, tuple(v), 6, (0, 0, 255), -1)
    points = points.astype(int)  # float 类型转成 int
    xmin, ymin = np.min(points[0], axis=0)
    xmax, ymax = np.max(points[0], axis=0)
    # print(xmin, ymin, xmax, ymax)
    # cv2.circle(result, tuple([ymin, xmin]), 6, (0, 0, 255), -1)
    # cv2.circle(result, tuple([ymax, xmax]), 6, (0, 0, 255), -1)
    result = result[ymin:ymax, xmin:xmax]
    cv2.imshow("result_perspective_transform", result)
    points = points - np.array([xmin, ymin], dtype=np.int32)
    # rr = cv2.fillPoly(result, points, 255)
    # cv2.imshow('fill', rr)
    cv2.waitKey()
    return result, points[0].tolist()


if __name__ == '__main__':
    orginal_img = cv2.imread("1.jpg")
    perspective_transform(orginal_img, 0, 45, 0, 42)
    perspective_transform(orginal_img, 45, 0, 0, 42)
    cv2.waitKey()
    cv2.destroyAllWindows()
