#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/8/5 15:54
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import os
import numpy as np
import cv2

__author__ = 'Max_Pengjb'


def bright_contrast(image, lower=0.9, upper=1.2):
    """
    # 通过 alpha, beta 来调整 对比度和亮度
    :param image: 图片，np.array 或者 路径
    :param lower: alpha,区间 min
    :param upper: alpha 区间 max
    :return: 修改后的图片
    """
    if isinstance(image, str) and os.path.exists(image):
        # image 如果是字符串，表示这是一个地址
        image = cv2.imread(image)
    alpha = np.random.uniform(lower, upper)  # np.random.randn()返回一个或一组服从标准正态分布的随机样本值。
    beta = np.random.uniform() * np.mean(image) / 2  # 提高亮度
    # print(alpha, beta)
    blank = np.zeros(image.shape, image.dtype)
    image = cv2.addWeighted(image, alpha, blank, 1 - alpha, beta)
    return image


if __name__ == '__main__':
    img = cv2.imread('./photo/x2996.jpg')
    cv2.imshow('img', img)
    image = bright_contrast(img)
    cv2.imshow('af', image)
    cv2.waitKey()
    cv2.destroyAllWindows()
