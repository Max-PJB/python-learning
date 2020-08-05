#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/8/4 22:13
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       缩放
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import numpy as np
import cv2
import os
from opencv_learn.my_bright_contrast import bright_contrast


# 裁剪放大
def crop_scale(image, boxes, labels, scale=2.0, nums=1):
    """
    裁剪放大 生成 放大比例最大为 scale 的 nums 个图片
    :param image: 图片，np.array 或者 路径
    :param boxes: 所有的框,[ [x_min,y_min,x_max,y_max],[x_min,y_min,x_max,y_max]……]
    :param labels: 框对应的标签
    :param scale: scale 放大倍数最大值 scale > 1
    :param nums: 需要生成的图片数量
    :return: 翻转后的图 和 框+标签 【[image,bboxes,labels],[image,bboxes,labels]……】
    """
    if isinstance(image, str) and os.path.exists(image):
        # image 如果是字符串，表示这是一个地址
        image = cv2.imread(image)
    h, w = image.shape[0:2]
    res = []
    while len(res) < nums:
        # 放大 tmp_scale 倍数  属于区间 [1 ~ scale]
        tmp_scale = np.random.rand() * (scale - 1) + 1.1
        h_t, w_t = int(h * tmp_scale), int(w * tmp_scale)
        image2 = cv2.resize(image, (w_t, h_t))
        boxes_tmp = np.array(boxes) * tmp_scale
        boxes_tmp = boxes_tmp.astype(np.int32)
        # 裁剪 crop 裁剪的 h ，w 范围应该是 [0 - ht-h] [0 - wt-w]
        crop_rand_h, crop_rand_w = np.random.rand(2)
        crop_h, crop_w = int(crop_rand_h * (h_t - h)), int(crop_rand_w * (w_t - w))
        res_image = image2[crop_h:crop_h + h, crop_w:crop_w + w]
        # 图片对比度和亮度随机加进来
        res_image = bright_contrast(res_image)
        # 处理 boxes， 坐标要相应的改变
        boxes_tmp = np.maximum(boxes_tmp - [crop_w, crop_h, crop_w, crop_h], 0)
        boxes_tmp = np.minimum(boxes_tmp, [w - 1, h - 1, w - 1, h - 1])
        # 对 boxes 进行处理，有一些啥标签都没有的，就略过去了
        res_boxes = []
        res_labels = []
        for box, label in list(zip(boxes_tmp, labels)):
            if 0 <= box[0] < box[2] < w and 0 <= box[1] < box[3] < h:
                res_boxes.append(box)
                res_labels.append(label)
        # 结果里面有框框，就可以返回了
        if res_boxes:
            res.append((res_image, res_boxes, res_labels))
    return res


if __name__ == '__main__':
    from opencv_learn.draw_boxes import draw_boxes, draw_boxes_with_labels

    before = draw_boxes_with_labels('./photo/x2996.jpg', [[[0, 0], [200, 100]], [[210, 110], [410, 310]]],
                                    ["speed_limited", "speed_unlimited"])
    cv2.imshow('before', before)
    res_list = crop_scale('./photo/x2996.jpg', [[0, 0, 200, 100], [210, 110, 410, 310]],
                          ["speed_limited", "speed_unlimited"])
    for i, (res_image, res_boxes, res_labels) in enumerate(res_list):
        print('res_boxes', res_boxes)
        image = draw_boxes_with_labels(res_image, res_boxes, res_labels)
        cv2.imshow('after_draw_' + str(i), image)
    cv2.waitKey()
    cv2.destroyAllWindows()
