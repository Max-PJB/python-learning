#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/27 16:11
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import csv
import requests

# url = 'http://127.0.0.1:5000/api/v1/product/add_good'
url = 'http://api.ailemong.com/api/v1/product/add_good'

files = ['tmp/bngy.CSV', 'tmp/cy.CSV', 'tmp/jkfa.CSV', 'tmp/ls.CSV',
         'tmp/mrff.CSV', 'tmp/zs.CSV', 'tmp/zsfjp.CSV', 'tmp/zycbp.CSV']
for file_one in files:
    with open(file_one, 'r', encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile)
        type_this = next(readCSV)
        print(type_this[0])
        print(type_this[1])
        next(readCSV)
        for row in readCSV:
            # print(row)
            name = row[0]
            title = row[1]
            json_data = {'type': type_this[0], 'category': type_this[1], 'name': row[0], 'title': row[1],
                         'cur_price': int(row[2]), 'origin_price': int(row[3]),
                         'swiperImages': [{'order': 1, 'sm_url': row[4]}], 'descImages': [{'order': 1, 'sm_url': row[4]}]}
            print(json_data)
            res = requests.post(url, json=json_data)
            print(res.json())
