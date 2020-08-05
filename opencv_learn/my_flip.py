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
    :param boxes: 所有的框,[ [[x,y],[x,y]], [[x,y],[x,y]]……] 或者 [ [x_min,y_min,x_max,y_max],[x_min,y_min,x_max,y_max]……]
    :return: 翻转后的图和框
    """
    if isinstance(image, str) and os.path.exists(image):
        # image 如果是字符串，表示这是一个地址
        image = cv2.imread(image)
    h, w = image.shape[0:2]
    res_img = image[:, ::-1]
    if boxes is not None:
        boxes = np.array(boxes)
        if boxes.ndim == 3:
            # boxes = [[[x, y], [x, y]], [[x, y], [x, y]]……]
            boxes = np.abs([w - 1, 0] - boxes)
            boxes = np.reshape(boxes, (-1, 4))
        elif boxes.ndim == 2:
            boxes = np.abs([w - 1, 0, w - 1, 0] - boxes)
        for box in boxes:
            if box[0] > box[2]:
                box[0], box[2] = box[2], box[0]
            if box[1] > box[3]:
                box[1], box[3] = box[3], box[1]
        # print(boxes)
    return res_img, boxes


if __name__ == '__main__':
    from opencv_learn.draw_boxes import draw_boxes

    image1 = draw_boxes('./photo/x2996.jpg', [[[0, 0], [200, 100]]])
    cv2.imshow('before_flip', image1)

    image, boxes = flip_x('./photo/x2996.jpg', [[[0, 0], [200, 100]]])
    image2 = draw_boxes(image, boxes)
    cv2.imshow('after_flip', image2)

    cv2.waitKey()
    cv2.destroyAllWindows()
