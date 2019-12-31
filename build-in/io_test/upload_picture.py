#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/27 13:27
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import requests
import os

url = 'http://127.0.0.1:5000/api/v1/img/img_upload_ui'
with open('haha.txt', 'a') as fs:
    for parent, dirnames, filenames in os.walk(
            r'C:\Users\pengj\Desktop\workspace\python-learning\build-in\io_test\img'):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            files = {'file': (filename, open(file_path, 'rb'))}
            res = requests.post(url, files=files)
            img_url = res.json()['result']['sm_url']
            print(parent, filename, img_url)
            print(res.json()['result']['sm_url'])
            fs.write(filename + '\t\t' + img_url + '\n')

