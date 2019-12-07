#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/25 21:42
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

from app import create_app

app = create_app()
# 在Pycharm 2018中，如果想要开启debug模式和更改端口号，则需要编辑项目配置。直接在app.run中更改是无效的。
# https://blog.csdn.net/james_laughing/article/details/88714116
if __name__ == '__main__':
    app.run()

