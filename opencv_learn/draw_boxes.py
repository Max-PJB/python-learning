#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/25 10:26
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
from opencv_learn.order_points import order_points

colors = [(0, 0, 127), (255, 255, 0), (0, 255, 0),
          (0, 255, 255), (255, 0, 255), (0, 0, 255)]
class_names = ["speed_limited", "speed_unlimited", "green_go",
               "yellow_back", "pedestrian_crossing", "red_stop"]


def draw_boxes(image, boxes):
    """
    在照片中把所有的 框框 都画出来
    :param image: 原图，可以是 cv2.imread 后的 ndarray, 也可以是地址 image_path
    :param boxes: 所有的框,[ [[x,y],[x,y]], [[x,y],[x,y]]……] 或者 [ [x_min,y_min,x_max,y_max],[x_min,y_min,x_max,y_max]……]
    :return:
    """
    if isinstance(image, str) and os.path.exists(image):
        # image 如果是字符串，表示这是一个地址
        image = cv2.imread(image)
    if isinstance(image, np.ndarray):
        for box in boxes:
            box = np.array(box, dtype=np.int32)
            if box.ndim == 2:
                # boxes = [[[x, y], [x, y]], [[x, y], [x, y]]……]
                x1, y1 = np.min(box, axis=0)
                x2, y2 = np.max(box, axis=0)
                image = cv2.rectangle(image, (x1, y1), (x2, y2), 255, 3)
            elif box.ndim == 1:
                x1, y1, x2, y2 = box
                image = cv2.rectangle(image, (x1, y1), (x2, y2), 255, 3)
            # 绘制多边形
            # box2 = order_points(box).astype(np.int32)
            # cv2.polylines(image, [box2], True, 255, 3)
        # cv2.imshow('polylines', image)
        return image
    return Exception('图片错误')


# 在图中画出检测框，输出类别信息
def draw_boxes_with_labels(image, bboxes, labels):
    """
    在照片中把所有的 框框 都画出来
    :param image: 原图，可以是 cv2.imread 后的 ndarray, 也可以是地址 image_path
    :param boxes: 所有的框,[ [[x,y],[x,y]], [[x,y],[x,y]]……] 或者 [ [x_min,y_min,x_max,y_max],[x_min,y_min,x_max,y_max]……]
    :return:
    """
    if isinstance(image, str) and os.path.exists(image):
        # image 如果是字符串，表示这是一个地址
        image = cv2.imread(image)
    thickness = 2
    font_scale = 1
    text_font = cv2.FONT_HERSHEY_SIMPLEX
    for box, label in list(zip(bboxes, labels)):
        box = np.array(box, dtype=np.int32)
        (x_min, y_min), (x_max, y_max) = (None, None), (None, None)
        if box.ndim == 2:
            # boxes = [[[x, y], [x, y]], [[x, y], [x, y]]……]
            x_min, y_min = np.min(box, axis=0)
            x_max, y_max = np.max(box, axis=0)
        elif box.ndim == 1:
            x_min, y_min, x_max, y_max = box
        draw_color = colors[class_names.index(label)]
        image = cv2.rectangle(image, (x_min, y_min), (x_max, y_max), draw_color, thickness)
        image = cv2.putText(image, label, (x_min, y_min + 25), text_font, font_scale, draw_color, thickness)
    return image


if __name__ == '__main__':
    # image = draw_boxes('./photo/x2996.jpg', [[[0, 0], [0, 100], [200, 100], [200, 0]]])
    image1 = draw_boxes('./photo/x2996.jpg', [[[0, 0], [200, 100]], [[210, 110], [410, 310]]])
    image2 = draw_boxes('./photo/x2996.jpg', [[0, 0, 200, 100], [210, 110, 410, 310]])
    image3 = draw_boxes_with_labels('./expand/0.jpg', [[334, 578, 598, 591], [334, 578, 598, 591]],
                        ['pedestrian_crossing', 'pedestrian_crossing'])
    cv2.imshow('polylines1', image1)
    cv2.imshow('polylines2', image2)
    cv2.imshow('polylines3', image3)
    cv2.waitKey()
    cv2.destroyAllWindows()
