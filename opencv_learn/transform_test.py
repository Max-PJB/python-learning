#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/24 17:09
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
from matplotlib import pyplot as plt

DEFAULT_PRNG = np.random


# 定义图片转换参数
class TransformParameters:
    def __init__(
            self,
            fill_mode='nearest',
            interpolation='linear',
            cval=0,
            relative_translation=True,
    ):
        self.fill_mode = fill_mode
        self.cval = cval
        self.interpolation = interpolation
        self.relative_translation = relative_translation

    def cvBorderMode(self):
        if self.fill_mode == 'constant':
            return cv2.BORDER_CONSTANT
        if self.fill_mode == 'nearest':
            return cv2.BORDER_REPLICATE
        if self.fill_mode == 'reflect':
            return cv2.BORDER_REFLECT101
        if self.fill_mode == 'wrap':
            return cv2.BORDER_WRAP

    def cvInterpolation(self):
        if self.interpolation == 'nearest':  # 最近邻插值
            return cv2.INTER_NEAREST
        if self.interpolation == 'linear':  # 双线性插值，适合放大图片
            return cv2.INTER_LINEAR
        if self.interpolation == 'cubic':  # 4x4像素邻域的双三次插值，适合放大图片
            return cv2.INTER_CUBIC
        if self.interpolation == 'area':  # 局部像素重采样，适合缩小图片
            return cv2.INTER_AREA
        if self.interpolation == 'lanczos4':
            return cv2.INTER_LANCZOS4  # 8x8像素插值法


# 随机转动一定角度
def random_rotation(min, max, prng=DEFAULT_PRNG):
    angle = prng.uniform(min, max)

    rotation_reslut = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    return rotation_reslut


# 随机平移
def random_translation(min, max, prng=DEFAULT_PRNG):
    min = np.array(min)
    max = np.array(max)
    assert min.shape == max.shape
    assert len(min.shape) == 1
    translation = prng.uniform(min, max)
    translation_result = np.array([
        [1, 0, translation[0]],
        [0, 1, translation[1]],
        [0, 0, 1]
    ])
    return translation_result


# 随机错切
def random_shear(min, max, prng=DEFAULT_PRNG):
    angle = prng.uniform()
    shear_result = np.array([
        [1, -np.sin(angle), 0],
        [0, np.cos(angle), 0],
        [0, 0, 1]
    ])
    return shear_result


# 随机缩放
def random_scaling(min, max, prng=DEFAULT_PRNG):
    min = np.array(min)
    max = np.array(max)
    assert min.shape == max.shape
    assert len(min.shape) == 1
    factor = prng.uniform(min, max)
    scaling_result = np.array([
        [factor[0], 0, 0],
        [0, factor[1], 0],
        [0, 0, 1]
    ])
    return scaling_result


# 随机翻转
def random_flip(flip_x_chance, flip_y_chance, prng=DEFAULT_PRNG):
    flip_x = prng.uniform(0, 1) < flip_x_chance
    flip_y = prng.uniform(0, 1) < flip_y_chance
    factor = (1 - 2 * flip_x, 1 - 2 * flip_y)
    flip_result = np.array([
        [factor[0], 0, 0],
        [0, factor[1], 0],
        [0, 0, 1]
    ])
    return flip_result


# 对图片进行随机变换，图片增强等操作，在不断的迭代训练中，其实是在变相增加训练集
def random_transform(
        min_rotation=0,
        max_rotation=0,
        min_translation=(0, 0),
        max_translation=(0, 0),
        min_shear=0,
        max_shear=0,
        min_scaling=(1, 1),
        max_scaling=(1, 1),
        flip_x_chance=0,
        flip_y_chance=0,
        prng=DEFAULT_PRNG):
    return np.linalg.multi_dot([
        random_rotation(min_rotation, max_rotation, prng),
        random_translation(min_translation, max_translation, prng),
        random_shear(min_shear, max_shear, prng),
        random_scaling(min_scaling, max_scaling, prng),
        random_flip(flip_x_chance, flip_y_chance, prng)
    ])


# 创建图片变形生成器
def random_transform_generator(prng=None, **kwargs):
    if prng is None:
        prng = np.random.RandomState()
    while True:
        yield random_transform(prng=prng, **kwargs)


# 调整预处理
def adjust_transform_for_image(transform=None, image=None, relative_translation=True, transform_parameters=None):
    height, width, channels = image.shape
    result = transform  # tranform_generator
    if relative_translation:
        result[0:2, 2] *= [width, height]
    result = change_transform_origin(transform, (0.5 * width, 0.5 * height))

    image = apply_transform(transform, image, transform_parameters)
    return image


# 改变变形的中心点
def change_transform_origin(transform, center):
    center = np.array(center)

    return np.linalg.multi_dot([translation(center), transform, translation(-center)])


def translation(translation):
    return np.array([
        [1, 0, translation[0]],  # 0.5width, -0.5width
        [0, 1, translation[1]],  # 0.5height, -0.5height
        [0, 0, 1]
    ])


def apply_transform(matrix, image, params):
    output = cv2.warpAffine(
        image,  # 输入图像
        matrix[:2, :],  # 变换矩阵，为inputArray类型的3x3矩阵
        dsize=(image.shape[1], image.shape[0]),  # 输出图像的大小，尺寸保持不变
        flags=params.cvInterpolation(),  # 插值方法
        borderMode=params.cvBorderMode(),  # 边界像素模式
        borderValue=params.cval,  # 边界填充，默认值为0
    )
    return output


if __name__ == '__main__':
    # 初始化一个图像处理参数对象
    transform_parameters = TransformParameters()
    # 创建一个图片转换迭代器
    # flip = {'flip_x_chance':0.5,'flip_y_chance':0.5}
    transform_generator = random_transform_generator()
    # 迭代
    for i, transform in enumerate(transform_generator):

        # 打开图片
        data_dir = './photo'
        image_name = 'x2996'
        extension = '.jpg'
        path = os.path.join(data_dir, image_name + extension)
        image = cv2.imread(path)
        # 进行图片变形
        image_transformed = adjust_transform_for_image(transform=transform, image=image,
                                                       transform_parameters=transform_parameters)
        # 将图片转换成RGB图像
        image = cv2.cvtColor(image_transformed, cv2.COLOR_BGR2RGB)
        # 打印图片
        cv2.imshow('image', image)
        cv2.waitKey()
        # 写入图片
        path_write = os.path.join(data_dir, image_name + str(i) + extension)
        cv2.imwrite(path_write, image_transformed)
        i += 1
        if i > 9:
            break
