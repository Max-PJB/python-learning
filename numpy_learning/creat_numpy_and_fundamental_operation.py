#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/6 10:15
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
import numpy as np

__author__ = 'Max_Pengjb'
start = time.time()

# 下面写上代码块
a = np.arange(5)
b = np.array([np.arange(6), np.arange(6)])
x = [y for y in range(6)]
c = np.array([x] * 4)
c[0] += 1
e = np.array([np.arange(4, 10), np.arange(5, 11)])
f = np.array([np.arange(2, 8), np.arange(8, 14)])
print(a)
print(b)
print(c)
print("e", e)
print("f", f)
print("e+f=", e + f)
print("e-f=", e - f)
print("e*f=", e * f)
m = np.mat([[1, 2, 3, 4, 5]])
n = np.mat([[1], [2], [3], [4], [5]])
m2 = np.array([[1, 2, 3], [4, 5, 6]])
n2 = np.array([[4, 5, 6], [1, 2, 3]])
print("matrix m * n : ", m * n)
print("matrix np.multiply(m, n) : ", np.multiply(m, n))
print("array m2 * n2 ： ", m2 * n2)
print("array np.multiply(m2, n2) ： ", np.multiply(m2, n2))
# 矩阵的转置和逆
"""
需要注意 在 array 和 matrix 中， 符号 * 作用不一样
在 array 中 * 和 multiply 的作用是一样的，对应元素想乘 dot 是向量内积
在 matrix 中， * 和 dot 的作用是一样的 
"""
zz = np.array([[2, 2, 3], [4, 5, 6], [7, 8, 9]])
nn = np.linalg.inv(zz)
print("逆", np.linalg.inv(zz))
print("转置 ", zz.T)
# nn = np.array([[1, -2, 1],[-2, 1, 0],[1, 0.66666667, -0.66666667]])
print(zz.dot(nn))

asplit = np.array([[1, 2, 3, 4, 5], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16]])
"""
注意这里的区别  
asplit[1, :2:] 结果是一个一维数组    [7 8]
asplit[1:2:, :2:] 得到的是一个二维的数组   [[7 8]]
"""
print(asplit[1][:2:])
print(asplit[1, :2:])
print(asplit[1:2:, :2:])
# 花式索引
print(asplit[[1, 0]])
print(asplit)

# reshape 数组的堆叠 改变数组形状
bb = np.arange(24).reshape(2, 3, 4)
print("reshape", bb)

# ravel  拆解,将多维数组变成一维数组
c = bb.ravel()
print("ravel", c)
d = bb.flatten()
print("flatten", d)
# flatten  拉直，其功能与ravel()相同，但是flatten()返回的是真实的数组，需要分配新的内存空间，而ravel()仅仅是改变视图
c[1] = 100
print("ravel ", bb, c)
# flatten 是返回了一份 copy.deepcopy 拷贝，改变 d 不会改变原来 b 的值
d[1] = 99
print("flatten", bb, d)
# shape 方法， reshape 函数有返回值
cc = bb.reshape(6, 4)
bb.shape = (6, 4)
print("cc", cc)
print("bb", bb)

# transpose 和 T 是一个东西
print("bb.T", bb.T)
print(bb)
bb.transpose()
print("bb.transpose", bb.transpose())

# 数组的堆叠
kk = np.arange(9).reshape(3, 3)
kk2 = kk * 2
# hstack() 水平叠加
hs = np.hstack((kk, kk2))  # 注意 这里是两层括号
print("hs", hs)
# vstack() 垂直叠加
vs = np.vstack((kk, kk2))  # 注意 这里是两层括号
print("vs", vs)
# dstack 增加一层深度
print(kk)
ds = np.dstack((kk, kk2))
print("ds", ds)
print(kk)

# 拆分数组
ff = np.arange(9).reshape(3, 3)
# hsplit() 横向拆分成 n 等分
hsp = np.hsplit(ff, 3)
print("ff", ff)
print("hsp", hsp)
# vsplit() 纵向拆分 成 n 等分
vsp = np.vsplit(ff, 3)
print("vsp", vsp)
# dsplit()
dds = np.arange(27).reshape(3, 3, 3)
print("dds", dds)
print("dsp", np.dsplit(dds, 3))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
