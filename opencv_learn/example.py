class Perspective:
    '''
        图形斜切变换

        args:
            img - 图片（类型: cv::mat）
            bbox - 边框
                [{'name': 'red_stop', 'bndbox': [299, 300, 373, 442]}, {...}, ...]
                类别, [左上角x坐标, 左上角y坐标, 右下角x坐标, 右下角y坐标]
    '''
    def __init__(self):
        # 设置参数
        self.count = 1          # 操作次数

    def __call__(self, imgs, bboxes):
        for img, bbox in zip(imgs, bboxes):
            for _ in range(self.count):
                self._perspective(img, bbox)    # 调用处理函数
        return self.new_imgs, self.new_bboxes
    
    def _perspective(self, img, bbox):
        # TODO 处理图片，bbox

        return new_img, new_bbox # 返回新图片和边框