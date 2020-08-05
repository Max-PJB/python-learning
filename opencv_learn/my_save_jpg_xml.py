#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/8/5 14:21
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import os
import xml.etree.ElementTree as ET
import cv2

__author__ = 'Max_Pengjb'

xml_frame_str = """        
<annotation>
    <folder>NA</folder>
    <filename> </filename>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>1280</width>
        <height>720</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
</annotation>
"""
obj_xml_str = """
<object>
    <name> </name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <occluded>0</occluded>
    <bndbox>
        <xmin>0</xmin>
        <ymin>0</ymin>
        <xmax>0</xmax>
        <ymax>0</ymax>
    </bndbox>
</object>"""


def save_jpg_xml(save_dir, image, bboxes, labels):
    """
        # 保存图片，加上图片的四边作为描述信息存储,如果是保存原图就先不处理 顶点信息
    :param save_dir: 保存的文件夹
    :param image: np.darray 图片
    :param bboxes: box 所有的框,[ [x_min,y_min,x_max,y_max],[x_min,y_min,x_max,y_max]……]
    :param labels:标签
    :return: 保存的 xml 文件的名字
    """
    # save_dir = os.path.dirname(img_path)
    # if not os.path.exists(os.path.dirname(save_path)):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    if isinstance(image, str) and os.path.exists(image):
        # image 如果是字符串，表示这是一个地址
        image = cv2.imread(image)
    k = len(os.listdir(save_dir)) // 2
    img_path = os.path.join(save_dir, str(k) + '.jpg')
    xml_path = os.path.join(save_dir, str(k) + '.xml')
    cv2.imwrite(img_path, image)
    # tree1 = ET.parse('./template_frame.xml')
    # root = tree1.getroot()
    root = ET.fromstring(xml_frame_str)
    root.find('filename').text = str(k) + '.jpg'
    for label, box in list(zip(labels, bboxes)):
        # tree2 = ET.parse('./template_obj.xml')
        # obj_element = tree2.getroot()
        obj_element = ET.fromstring(obj_xml_str)
        obj_element.find('name').text = label
        obj_element.find('bndbox').find('xmin').text = str(box[0])
        obj_element.find('bndbox').find('ymin').text = str(box[1])
        obj_element.find('bndbox').find('xmax').text = str(box[2])
        obj_element.find('bndbox').find('ymax').text = str(box[3])
        root.append(obj_element)
    etree = ET.ElementTree(root)
    etree.write(xml_path)
    return xml_path


if __name__ == '__main__':
    save_expand = r'D:\car_data\0'
    # save_expand = r'D:\car_data_origin\test'

    # save_jpg_xml(save_expand './photo/x2996.jpg', [[764, 190, 945, 403], [334, 578, 598, 591]], ["speed_unlimited", "pedestrian_crossing"])

    # 保存了，在打开检查一下，对不对
    from opencv_learn.cv_utils import get_all_xmls, parse_xml_bboxes
    from opencv_learn.draw_boxes import draw_boxes_with_labels

    file_names = get_all_xmls(save_expand)
    for i, file in enumerate(file_names):
        # rectangles ：[ [detection_type, xmin, ymin, xmax, ymax],]
        # xml 和 jpg 必须在同级目录
        pic_path, rectangles = parse_xml_bboxes(os.path.join(save_expand, file))
        bboxes = list(map(lambda x: [x[1], x[2], x[3], x[4]], rectangles))
        labels = list(map(lambda x: x[0], rectangles))
        print(bboxes, labels)
        img = draw_boxes_with_labels(pic_path, bboxes, labels)
        cv2.imshow(str(i), img)
        cv2.waitKey()
    cv2.destroyAllWindows()
