#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/24 15:31
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import numpy as np
import cv2
import os


# 水平翻转
def flip_x(image, boxes=None):
    """
    水平翻转
    :param image: 图片，np.array
    :param boxes: 所有的框,[ [[x,y],[x,y]], [[x,y],[x,y]]……]
    :return: 翻转后的图和框
    """
    if isinstance(image, str) and os.path.exists(image):
        # image 如果是字符串，表示这是一个地址
        image = cv2.imread(image)
    h, w = image.shape[0:2]
    res_img = image[:, ::-1]
    if boxes is not None:
        print(boxes)
        boxes = np.array(boxes)
        boxes = np.abs([w - 1, 0] - boxes)
    return res_img, boxes


if __name__ == '__main__':
    from opencv_learn.draw_boxes import draw_boxes

    image, boxes = flip_x('./photo/x2996.jpg', [[[0, 0], [200, 100]]])
    # cv2.imshow('before_draw', image)
    image = draw_boxes(image, boxes)
    cv2.imshow('after_draw', image)

    cv2.waitKey()
    cv2.destroyAllWindows()
