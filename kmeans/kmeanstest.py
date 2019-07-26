# -*- coding: utf-8 -*-
# @Time    : 2019-7-8 15:35
# @Author  : zhuoby
import numpy as np
from sklearn.cluster import KMeans


def kmeans_building(x1, x2, types_num):
    X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)

    # 设置聚类数n_clusters的值为types_num
    kmeans_model = KMeans(n_clusters=types_num).fit(X)

    # 整理分类好的原始数据，并画出聚类图
    x1_result = []
    x2_result = []

    for i in range(types_num):
        temp = [];
        temp1 = []
        x1_result.append(temp)
        x2_result.append(temp1)

    # 画聚类点
    for i, label in enumerate(kmeans_model.labels_):
        x1_result[label].append(x1[i])
        x2_result[label].append(x2[i])

    x3_center = []
    x4_center = []
    for i in range(types_num):
        temp_center = [];
        temp_center1 = []
        x3_center.append(temp_center)
        x4_center.append(temp_center1)

    for i, label in enumerate(kmeans_model.labels_):
        x3_center[label].append(list(list(kmeans_model.cluster_centers_)[label])[0])
        x4_center[label].append(list(list(kmeans_model.cluster_centers_)[label])[1])

    return kmeans_model, x1_result, x2_result, x3_center, x4_center


import xlrd

print("step 1: load data...")
# 读取Excel表格中的商圈经纬度
workbook = xlrd.open_workbook(r'D:\MyData\pengjb4\Downloads\tentest.xlsx')
sheet2_name = workbook.sheet_names()[0]

# 根据sheet索引或者名称获取sheet内容，下面是的sheet索引从0开始
sheet2 = workbook.sheet_by_index(0)

# sheet的名称，行数，列数
print(sheet2.name, sheet2.nrows, sheet2.ncols)

# 获取整行和整列的值（数组）
rows = sheet2.row_values(3)  # 获取第四行内容
cols = sheet2.col_values(2)  # 获取第三列内容
x = []
y = []
# 遍历每一行的数据，X是添加第二列的数据，y是添加第三列的数据
for i in range(sheet2.nrows):
    x.append(sheet2.row_values(i)[1])
    y.append(sheet2.row_values(i)[2])

# 本例要分1200个类，注意 shapes和labels是对应的
kmeans_model, x1_result, x2_result, x1_center, x2_center = kmeans_building(x, y, 3)
print(kmeans_model)
print(x1_result)
print(x2_result)
print(x1_center)
print(x2_center)

# 输出聚类结果
with open('kmeans-result-test.txt', 'w') as fileobject:
    for i in range(len(x1_result)):
        for s in range(len(x1_result[i])):
            print(str(x1_result[i][s]) + " " + str(x2_result[i][s]))
            fileobject.write(str(x1_result[i][s]) + "\t" + str(x2_result[i][s]) + "\t" + str(i) + "\n")
        print("-------")


