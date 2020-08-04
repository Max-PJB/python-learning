from sys import exit
import os
import shutil
import cv2
from collections import OrderedDict
import xmltodict as xd
import random


filter_list = []

def augmentation(compose, in_dir, out_dir):
    '''
        加载图片，调用图形变换
    '''
    if len(os.listdir(in_dir)) == 0:
        print('no file!')
        exit(0)
    imgs_name = [name.split('.')[0].split('_')[0] for name in os.listdir(in_dir) if name.endswith('.jpg')]
    imgs_path = [os.path.join(in_dir, name+'.jpg') for name in imgs_name]
    xmls_name = [name.split('.')[0].split('_')[0] for name in os.listdir(in_dir) if name.endswith('.xml')]
    xmls_path = [os.path.join(in_dir, name+'.xml') for name in xmls_name]

    for img_path, img_name, xml_path, xml_name in zip(imgs_path, imgs_name, xmls_path, xmls_name):
        if img_name in filter_list:
            continue

        img = cv2.imread(img_path)
        bboxes = get_bbox_from_xml(xml_path)
        compose(img, bboxes)

def get_bbox_from_xml(xml_path):
    bboxes = []
    with open(xml_path, 'r') as f:
        xml_str = f.read()
        xml = xd.parse(xml_str)
    
    if not isinstance(xml['annotation']['object'], list):
        xml['annotation']['object'] = [xml['annotation']['object']]

    for b in xml['annotation']['object']:
        obj = {}
        obj['filename'] = xml['annotation']['filename'].split('.')[0]
        obj['name'] = b['name']
        obj['bndbox'] = []
        obj['bndbox'].append(int(b['bndbox']['xmin']))
        obj['bndbox'].append(int(b['bndbox']['ymin']))
        obj['bndbox'].append(int(b['bndbox']['xmax']))
        obj['bndbox'].append(int(b['bndbox']['ymax']))
        bboxes.append(obj)
    return bboxes


class Compose:
    '''
        图形变换的调用，存储
    '''
    def __init__(self, transforms, save_dir='/tmp/', use_new_img=False, is_show=False):
        self.transforms = transforms
        self.save_dir = save_dir
        self.use_new_img = use_new_img      # 是否使用原图
        self.is_show = is_show              # 是否显示
        self.t = None   # current transforms

    def __call__(self, img, bboxes):
        for t in self.transforms:
            self.t = t
            if self.use_new_img:
                _img, _bboxes = t(img.copy(), [b.copy() for b in bboxes])
                self._save(_img, _bboxes)
            else:
                img, bboxes = t(img, bboxes)
                self._save(img, bboxes)
            if self.is_show:
                self.show(img, bboxes)

    def _save(self, img, bboxes):
        # set file name
        filename = f'{bboxes[0]["filename"]}_{self.t.__class__.__name__}'
        # save image
        cv2.imwrite(os.path.join(self.save_dir, filename+'.jpg'), img)
        # save xml
        self._save_xml(filename, img, bboxes)
    
    def _save_xml(self, filename, img, bboxes):
        with open('template.xml', 'r') as f:
            xml_str = f.read()
            xml = xd.parse(xml_str)
            xml['annotation']['object'] = []

        xml['annotation']['filename'] = filename + '.jpg'
        size = OrderedDict()
        size['height'], size['width'], size['depth'] = img.shape
        xml['annotation']['size'] = size
        
        for bbox in bboxes:
            filename = bbox['filename']
            name = bbox['name']
            xmin, ymin, xmax, ymax = bbox['bndbox']
            obj = OrderedDict()
            obj['name'] = name
            bndbox = OrderedDict()
            bndbox['xmin'] = xmin
            bndbox['ymin'] = ymin
            bndbox['xmax'] = xmax
            bndbox['ymax'] = ymax
            obj['bndbox'] = bndbox
            xml['annotation']['object'].append(obj)
        
        with open(os.path.join(self.save_dir, filename+'.xml'), 'w') as f:
            f.write(xd.unparse(xml))
    
    @staticmethod
    def show(img, bboxes):
        img_show = img.copy()

        for b in bboxes:
            Compose.plot_one_box(img_show, b)

        cv2.imshow('', img_show)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    
    @staticmethod
    def plot_one_box(img, bbox):
        tl = round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
        color = [random.randint(0, 255) for _ in range(3)]
        x1, y1, x2, y2 = bbox['bndbox']
        c1, c2 = (x1, y1), (x2, y2)
        cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
        tf = max(tl - 1, 1)
        t_size = cv2.getTextSize(bbox['name'], 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, bbox['name'], (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        
        return img


class Orign:
    '''
        保存原图
    '''
    def __call__(self, img, bboxes):
        return img, bboxes



if __name__ == "__main__":
    data_dir = '/tmp/haixuan'
    out_dir = '/tmp/out'

    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.mkdir(out_dir)

    print('start ...')
    compose = Compose([
        Orign(),
        Perspective(),
        # 往这加自己的类
    ],
    save_dir=out_dir,
    use_new_img=True)
    augmentation(compose, data_dir, out_dir)

    print('end!')

