#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/30 21:10
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import re
import linecache

res = []
with open('test', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        # print(line)
        search_file = re.search('C:/Users/pengj/Desktop/workspace/winlong/xmall-front-master', line)
        if search_file:
            file_url = line[search_file.span()[0]:len(line) - 2]
            # print(search_file)
            # print("haha", file_url)
            res.append([file_url, []])
        else:
            search_line = re.search(':', line)
            if search_line:
                # print(line)
                ss = line.split()
                line_num = ss[0].split(':', 1)
                print(ss)
                # print(line_num)
                row = int(line_num[0])
                col = int(line_num[1])
                # print("line_num", row, col, line)
                res[-1][1].append((row, col))
        line = f.readline()

    for one_file in res:
        with open(one_file[0], "r", encoding='utf-8') as ff:
            file_data = ff.readlines()
        for row, col in one_file[1]:
            line = file_data[row - 1]
            if len(line) <= col:
                file_data[row - 1] = line + ";"
            else:
                file_data[row - 1] = line[:col] + ";" + line[col:]
        print(type(file_data))
        print(file_data)
        for l in file_data:
            print(l)
        with open(one_file[0], "w", encoding='utf-8') as ff:
        # with open('.ts.txt', "w", encoding='utf-8') as ff:
            ff.writelines(file_data)
