#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/23 14:14
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
import time
import xml.etree.ElementTree as ET
from opencv_learn.my_perspective_transform import perspective_transform
from opencv_learn.my_flip import flip_x
from opencv_learn.draw_boxes import draw_boxes, draw_boxes_with_labels
from opencv_learn.my_crop_scale import crop_scale
from opencv_learn.my_save_jpg_xml import save_jpg_xml

import json

allFileNum = 0


def get_all_jgp_xml_couple(folder_path: str) -> list:
    """
    :param folder_path: 读取文件的目录地址
    :return: 返回所有的 （图片-xml标注）
    """
    # 所有文件
    file_xml_couple_dict = dict()
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(folder_path)
    for file_name in files:
        # 判断是 xml 或者是 jpg,png 等就放进去
        if os.path.isfile(folder_path + '/' + file_name):
            name, file_type = os.path.splitext(file_name)
            if name not in file_xml_couple_dict:
                # 这个名字的图片或者xml从来没有出现过
                file_xml_couple_dict[name] = [None, None]
            # 判断文件是图片还是标注xml文件
            if file_type in {'.jpg', '.png', '.jpeg'}:
                # 后缀名可以再添加
                if file_xml_couple_dict[name][0] is not None:
                    print('文件夹中包含多张以 ', file_xml_couple_dict[name], '为名称的图片，请检查！')
                else:
                    file_xml_couple_dict[name] = [file_name, file_xml_couple_dict[name][1]]
            elif file_type in {'.xml'}:
                # 标注文件
                file_xml_couple_dict[name] = [file_xml_couple_dict[name][0], file_name]
            # print(file_xml_couple_dict)
    return list(file_xml_couple_dict.values())


def get_all_xmls(folder_path: str) -> list:
    """
    :param folder_path: 读取文件的目录地址
    :return: 返回所有的 （xml标注）
    """
    # 所有文件
    xmls = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(folder_path)
    for file_name in files:
        # 判断是 xml 或者是 jpg,png 等就放进去
        if os.path.isfile(os.path.join(folder_path, file_name)):
            _, file_type = os.path.splitext(file_name)
            if file_type in {'.xml'}:
                xmls.append(file_name)
    return xmls


# Python读取一个目录下的所有文件
def printPath(level, path):
    global allFileNum
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if os.path.isdir(path + '/' + f):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if f[0] == '.':
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if os.path.isfile(path + '/' + f):
            # 添加文件
            fileList.append(f)
            # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if i_dl == 0:
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            print('- ' * (int(dirList[0])), dl)
            # 打印目录下的所有文件夹和文件，目录级别+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        # 打印文件
        print('- ' * (int(dirList[0])), fl)
        # 随便计算一下有多少个文件
        allFileNum = allFileNum + 1


# 保存图片，加上图片的四边作为描述信息存储,如果是保存原图就先不处理 顶点信息
def save_img(save_dir: str, img: np.array, points=None):
    # save_dir = os.path.dirname(img_path)
    # if not os.path.exists(os.path.dirname(save_path)):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    k = len(os.listdir(save_dir))
    img_path = os.path.join(save_dir, str(k) + '.jpg')
    cv2.imwrite(img_path, img)
    if 'pic_classes' not in save_dir:
        json_dir = os.path.join(save_dir, 'json')
        if not os.path.exists(json_dir):
            os.mkdir(json_dir)
        if points is not None:
            h, w = img.shape[0:2]
            points = [[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]]
            # rr = cv2.fillPoly(img, [np.array(points, dtype=np.int32)], 255)
            # cv2.imshow('rrrrrrr', rr)
        json_path = os.path.join(json_dir, str(k) + '.json')
        with open(json_path, 'w', encoding='utf8') as fp:
            fp.write(json.dumps({'points': points}))


def background_target_generator(img_path, save_folder, type_tangels):
    """
    把目标区域扣出来，把扣掉目标区域后的背景找出来
    :param img_path: 来源图片路径
    :param save_folder: 生成图片的保存路径
    :param type_tangels: 【[detection_type, xmin, ymin, xmax, ymax]，】形式的一个数组
    :return: None
    """
    cur_img = cv2.imread(img_path)
    # h, w = cur_img.shape[0:2]
    # print('h, w',cur_img.shape)
    # 扣背景的掩码
    # mask = np.ones(cur_img.shape)
    for rec in type_tangels:
        # rec 形式： [detection_type, xmin, ymin, xmax, ymax]
        xmin, ymin, xmax, ymax = rec[1:5]
        # 根据 xmin，ymin，xmax，ymax 裁剪图片，抠出来，然后保存
        target_img = cur_img[ymin:ymax, xmin:xmax]
        save_dir = os.path.join(save_folder, rec[0])
        cv2.imshow('target_img', target_img)
        save_img(save_dir, target_img)
        # TODO 填充被扣掉的这些区域, 这一部分效果不太好，需要 看看别人的算法咯！
        # y1, y2 = ymin, ymax
        # step = 1
        # while y1 < y2:
        #     if ymin - k >= 0:
        #         cur_img[y1:y1 + k, xmin:xmax] = cur_img[ymin - k:ymin, xmin:xmax]
        #         y1 = y1 + k
        #     if ymax + k < h:
        #         cur_img[y2 - k:y2, xmin:xmax] = cur_img[ymax:ymax + k, xmin:xmax]
        #         y2 = y2 - k
        #     step <<= 2
        # w_, h_ = xmax - xmin, ymax - ymin
        # w1, w2, h1, h2 = max(0, xmin - w_ // 2), min(w - 1, xmax + w_ // 2), max(0, ymin - h_ // 2), min(h - 1, ymax + h_ // 2)
        # cur_img[h1:h2, w1:w2] = cv2.medianBlur(cur_img[h1:h2, w1:w2], 3)
        cur_img[ymin:ymax, xmin:xmax] = 0  # 把图扣了后，原图就置为 黑色0了
        cv2.waitKey()
    save_img(save_folder + 'background/', cur_img)


def augmentation(save_dir, img_path):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    json_dir = os.path.join(save_dir, 'json')
    if not os.path.exists(json_dir):
        os.mkdir(json_dir)
    image = cv2.imread(img_path)
    # 原图的四个顶点
    # th, tw = image.shape[0:2]
    # vertexes = np.array([(0, 0), (tw - 1, 0), (tw - 1, th - 1), (0, th - 1)], dtype=np.float32)
    # TODO 透视变换的策略
    for x in range(-45, 45, 20):
        # perspective_transform 会返回一张图，加 4 个顶点 [[x,y],]
        # 这里做一些图片的变换，需要返回变换后的图片 + 变换后图片的四个顶点坐标
        trans_img, points = perspective_transform(image, x, 0, 0)
        save_img(save_dir, trans_img)
    for y in range(-45, 45, 20):
        # perspective_transform 会返回一张图，加 4 个顶点 [[x,y],]
        # 这里做一些图片的变换，需要返回变换后的图片 + 变换后图片的四个顶点坐标
        trans_img, points = perspective_transform(image, 0, y, 0)
        save_img(save_dir, trans_img)
    # TODO flip 水平翻转 + 平移 + 缩放
    # 水平翻转： 只有 红绿灯+ 车道线 进行水平翻转。 减速标志不进行
    do_flip = []

    trans_img, _ = flip_x(image)
    save_img(save_dir, trans_img)

    # TODO scale 缩放


# 解析 xml 文件，把其中的表示 框框的部分解析出来成 rectangles
def parse_xml_bboxes(xml_path):
    """
    解析 xml， xml 和 jpg 必须在同级目录
    :param xml_path:  xml 文件的路径
    :return: rectangles ：(image_path, [detection_type, xmin, ymin, xmax, ymax])
    """
    #  xml.etree.ElementTree 可以直接从文件中解析 xml 文件
    tree = ET.parse(xml_path)
    root = tree.getroot()
    # for child in root:
    #     print(child.attrib,child.text)
    # for elem in tree.iter():
    #     print(elem.tag, elem.attrib, elem.text)
    # Element.findall() 仅查找当前元素的直接子元素中带有指定标签的元素。
    # Element.find() 找带有特定标签的 第一个 子级，然后可以用 Element.text 访问元素的文本内容
    pic_name_node = root.find('filename')
    pic_name = pic_name_node.text
    # 这里处理德江留下来的坑。
    _, xml_name = os.path.split(xml_path)
    if xml_name.startswith('x') and not pic_name.startswith('x'):
        pic_name = 'x' + pic_name
    rectangles = []
    # 遍历所有 object
    for obj in root.findall('object'):
        detection_type = obj.find('name').text
        xmin = int(obj.find('bndbox').find('xmin').text)
        ymin = int(obj.find('bndbox').find('ymin').text)
        xmax = int(obj.find('bndbox').find('xmax').text)
        ymax = int(obj.find('bndbox').find('ymax').text)
        rectangles.append([detection_type, xmin, ymin, xmax, ymax])
    return os.path.join(os.path.dirname(xml_path), pic_name), rectangles


def my_augmentation(imgs_folder, save_expand, names):
    if not os.path.exists(save_expand):
        os.mkdir(save_expand)
    cnt = 0  # 记录一下一起生成了多少图片
    xml_names = []
    for file in names:
        print('-' * 8 + ' 进程 ' + str(os.getpid()) + ' 正在处理 ' + '-' * 2 + file + '-' * 3)
        res_list = []
        # rectangles ：[ [detection_type, xmin, ymin, xmax, ymax],]
        # xml 和 jpg 必须在同级目录
        pic_path, rectangles = parse_xml_bboxes(os.path.join(imgs_folder, file))
        bboxes = list(map(lambda x: [x[1], x[2], x[3], x[4]], rectangles))
        labels = list(map(lambda x: x[0], rectangles))
        # 做一下翻转看看 flip_x 要求传入的 boxes 格式: [ [[x,y],[x,y]], [[x,y],[x,y]]……]
        # 翻转只针对斑马线,红绿灯，如果包含 限速就不翻转了
        no_need_flip_class_names = {"speed_limited", "speed_unlimited"}
        CROP_NUMS = 10  # 使用 放大 裁剪 需要生成多少张图
        if not set(labels) & no_need_flip_class_names:  # 交集为空，就说明不存在了 限速标，可以翻转
            flip_img, flip_boxes = flip_x(pic_path, list(map(lambda x: [[x[1], x[2]], [x[3], x[4]]], rectangles)))
            # 展示一下
            # draw_image = draw_boxes_with_labels(flip_img, flip_boxes, labels)
            # cv2.imshow("draw_image", draw_image)
            # 保存,翻转不影响 labels
            res_list.append([flip_img, flip_boxes, labels])
            # 翻转了后，也再做一下裁剪扩充数据吧
            flip_crop_scale_res_list = crop_scale(flip_img, flip_boxes, labels, nums=CROP_NUMS)
            res_list.extend(flip_crop_scale_res_list)
        # 这里做一下 放大后裁剪,返回的是 nums 个图片+bboxes+labels: 【[image,bboxes,labels],[image,bboxes,labels]……】
        crop_scale_res_list = crop_scale(pic_path, bboxes, labels, nums=CROP_NUMS)
        res_list.extend(crop_scale_res_list)
        # 保存 图片 + bboxes + label 成个 jgp + xml 格式
        for res_image, res_boxes, res_labels in res_list:
            xml_name = save_jpg_xml(save_expand, res_image, res_boxes, res_labels)
            xml_names.append(xml_name)
        cnt += len(res_list)
    return cnt, xml_names


if __name__ == '__main__':
    import time

    start_time = time.time()
    save_folder = './pic_classes/'
    # imgs_folder = './photo/'
    imgs_folder = r'D:\car_data_origin\data_7_22'
    # imgs_folder = r'D:\car_data_origin\test'
    # save_expand = './expand'
    save_expand = r'D:\car_data'
    # 引入多进程加快速度
    from multiprocessing import cpu_count
    from multiprocessing import Pool

    CPU_COUNT = cpu_count()  # CPU内核数 本机为 6
    pool = Pool(processes=CPU_COUNT)
    # printPath(1, './photo/')
    # print('总文件数 =', allFileNum)
    # file_names = get_all_jgp_xml_couple(imgs_folder)
    file_names = get_all_xmls(imgs_folder)
    N = len(file_names)
    sepList = [[i * (N // CPU_COUNT), (i + 1) * (N // CPU_COUNT)] for i in range(0, CPU_COUNT)]
    sepList[CPU_COUNT - 1][1] = N
    print(sepList)

    result = []
    for i in range(CPU_COUNT):
        result.append(pool.apply_async(my_augmentation,
                                       (imgs_folder, os.path.join(save_expand, str(i)),
                                        file_names[sepList[i][0]:sepList[i][1]])))
    pool.close()
    pool.join()
    list1 = [res.get()[0] for res in result]
    print(sum(list1), end='')  # end='' 表示取消 /n
    """
    cnt = 0  # 记录一下一起生成了多少图片
    for i, file in enumerate(file_names):
        res_list = []
        # rectangles ：[ [detection_type, xmin, ymin, xmax, ymax],]
        # xml 和 jpg 必须在同级目录
        pic_path, rectangles = parse_xml_bboxes(os.path.join(imgs_folder, file))
        bboxes = list(map(lambda x: [x[1], x[2], x[3], x[4]], rectangles))
        labels = list(map(lambda x: x[0], rectangles))
        # 做一下翻转看看 flip_x 要求传入的 boxes 格式: [ [[x,y],[x,y]], [[x,y],[x,y]]……]
        # 翻转只针对斑马线,红绿灯，如果包含 限速就不翻转了
        no_need_flip_class_names = {"speed_limited", "speed_unlimited"}
        CROP_NUMS = 10  # 使用 放大 裁剪 需要生成多少张图
        if not set(labels) & no_need_flip_class_names:  # 交集为空，就说明不存在了 限速标，可以翻转
            flip_img, flip_boxes = flip_x(pic_path, list(map(lambda x: [[x[1], x[2]], [x[3], x[4]]], rectangles)))
            # 展示一下
            # draw_image = draw_boxes_with_labels(flip_img, flip_boxes, labels)
            # cv2.imshow("draw_image", draw_image)
            # 保存,翻转不影响 labels
            res_list.append([flip_img, flip_boxes, labels])
            # 翻转了后，也再做一下裁剪扩充数据吧
            flip_crop_scale_res_list = crop_scale(flip_img, flip_boxes, labels, nums=CROP_NUMS)
            res_list.extend(flip_crop_scale_res_list)
        # 这里做一下 放大后裁剪,返回的是 nums 个图片+bboxes+labels: 【[image,bboxes,labels],[image,bboxes,labels]……】
        crop_scale_res_list = crop_scale(pic_path, bboxes, labels, nums=CROP_NUMS)
        res_list.extend(crop_scale_res_list)
        # 保存 图片 + bboxes + label 成个 jgp + xml 格式
        for res_image, res_boxes, res_labels in res_list:
            save_jpg_xml(save_expand, res_image, res_boxes, res_labels)
        cnt += len(res_list)
        # for i, (res_image, res_boxes, res_labels) in enumerate(res_list):
        #     # 显示出来看看
        #     print('res_boxes', res_boxes)
        #     image = draw_boxes_with_labels(res_image, res_boxes, res_labels)
        #     cv2.imshow('after_draw_' + str(i), image)
        # 切割数据，把背景切到 pic_classes/background ，把labels 切到对应 label 名的目录pic_classes/'$label'
        # TODO 这个 部分先暂时不弄了 这个是准备用来抠图然后贴上去搞
        # background_target_generator(pic_path, save_folder, rectangles)
        # 调用数据增强方法
        generator_dir = './generator'
        for folder in os.listdir(save_folder):
            if folder == 'background':
                break
            target_label_folder = os.path.join(save_folder, folder)
            for image_name in os.listdir(target_label_folder):
                target_image_path = os.path.join(target_label_folder, image_name)
                label_generator_dir = os.path.join(generator_dir, folder)
                if not os.path.exists(label_generator_dir):
                    os.mkdir(label_generator_dir)
                # augmentation(label_generator_dir, target_image_path)
    cv2.destroyAllWindows()
    print('-' * 10 + ' done ' + '-' * 5 + ' gennerate ' + str(cnt) + ' images' + '-' * 3)
    """
    end_time = time.time()
    print('Running time: %s Seconds' % (end_time - start_time))
