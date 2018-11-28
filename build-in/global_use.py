#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/27 12:00
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   global 的用法
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def gg():
    ss = 1
    dd = 2

    def gg2():
        print(dd)
        print(ss)
        # 看，这里就会出错。提示 ss 不存在，因为这里把 ss 看做本地变量了，但是本地又没有，所以出错
        ss = ss + 1

    gg2()


# gg()

# 正确的用法是使用 global
def mm():
    # 声明 nnn 为global
    global nnn
    nnn = 10

    def mm2():
        # 引用 global 中的 nnn
        global nnn
        nnn = 10
        print(nnn)
        nnn += 20
        print(nnn)

    mm2()


mm()
# 看，golbal 在这里还可以调用啊
print(nnn)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
