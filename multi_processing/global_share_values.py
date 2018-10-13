#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/23 22:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import multiprocessing

__author__ = 'Max_Pengjb'

# Python 进程之间共享数据(全局变量)

# 1.进程之间共享数据(数值型)：


def func1(num):
    num.value = 10.78  # 子进程改变数值的值，主进程跟着改变


if __name__ == "__main__":
    num = multiprocessing.Value("d", 10.0)  # d表示数值,主进程与子进程共享这个value。（主进程与子进程都是用的同一个value）
    print(num.value)

    p = multiprocessing.Process(target=func1, args=(num,))
    p.start()
    p.join()

    print(num.value)

# 2.进程之间共享数据(数组型)：


def func2(num):
    num[2] = 9999  # 子进程改变数组，主进程跟着改变


if __name__ == "__main__":
    num = multiprocessing.Array("i", [1, 2, 3, 4, 5])  # 主进程与子进程共享这个数组
    print(num[:])

    p = multiprocessing.Process(target=func2, args=(num,))
    p.start()
    p.join()

    print(num[:])

# 3.进程之间共享数据(dict,list)：


def func3(mydict, mylist):
    mydict["index1"] = "aaaaaa"  # 子进程改变dict,主进程跟着改变
    mydict["index2"] = "bbbbbb"
    mylist.append(11)  # 子进程改变List,主进程跟着改变
    mylist.append(22)
    mylist.append(33)


if __name__ == "__main__":
    with multiprocessing.Manager() as MG:  # 重命名
        mydict = multiprocessing.Manager().dict()  # 主进程与子进程共享这个字典
        mylist = multiprocessing.Manager().list(range(5))  # 主进程与子进程共享这个List

        p = multiprocessing.Process(target=func3, args=(mydict, mylist))
        p.start()
        p.join()

        print(mylist)
        print(mydict)
