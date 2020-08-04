import os
import shutil
import cv2
import numpy as np
from random import random, randint
from math import sin, cos, atan2, pi, sqrt


class Perspective:
    '''
        图形斜切变换

        args:
            img - 图片（类型: cv::mat）
            bbox - 边框
                [{'filename': '0.jpg', 'name': 'red_stop', 'bndbox': [299, 300, 373, 442]}, {...}, ...]
                类别, [左上角x坐标, 左上角y坐标, 右下角x坐标, 右下角y坐标]
    '''
    def __init__(self):
        self.count = 1          # 操作次数
        self.warp_rate = 0.2    # 四个角斜切大小占图像的比例

    def __call__(self, img, bboxes):
        for bbox in bboxes:
            for _ in range(self.count):
                new_img, new_bbox = self._perspective(img, bbox)
                img = new_img                                   # 修改图片
                bbox['bndbox'] = new_bbox                       # 修改bbox
        return img, bboxes
    
    def _perspective(self, img, bbox):
        new_bbox = bbox['bndbox']

        x1, y1, x2, y2 = bbox['bndbox']
        roi_img = img[y1:y2, x1:x2, :].copy()   # 要处理的区域
        img[y1:y2, x1:x2, :] = 0                # 原区域置黑

        h, w, _ = roi_img.shape
        hr, wr = h*self.warp_rate, w*self.warp_rate

        # 左上，右上，左下，右下
        pts = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
        pts_dst = np.float32([
            [wr*random(), hr*random()], 
            [w-wr*random(), hr*random()], 
            [wr*random(), h-hr*random()], 
            [w-wr*random(), h-hr*random()]
        ])

        M = cv2.getPerspectiveTransform(pts, pts_dst)
        p_img = cv2.warpPerspective(roi_img, M, (h, w))

        # 调整bbox
        new_h, new_w, _ = p_img.shape
        x2, y2 = x1+new_w, y1+new_h     # 右下角坐标
        img[y1:y2, x1:x2, :] = p_img    # 将修改的区域放置图中
        new_bbox = [x1, y1, x2, y2]     # 修改bbox

        return img, new_bbox
