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
import time
import multiprocessing
import os

__author__ = 'Max_Pengjb'
start = time.time()
# 下面写上代码块

"""
怎么实现多进程

Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

实现多进程可以使用python官方提供的一个类Process。

Process类用来描述一个进程对象。创建子进程的时候，只需要传入一个执行函数和函数的参数即可完成Process示例的创建。
•star()方法启动进程；
•join()方法实现进程间的同步，等待所有进程退出；(等所有子进程执行完了，在执行后面的代码)
•close()用来阻止多余的进程涌入进程池 Pool造成进程阻塞；

    multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

•target是函数名字，需要调用的函数；
•args函数需要的参数，以tuple的形式传入。

首先我们来写一个简单的多进程程序！
"""


def run_proc(name):
    print('Child process {0} {1} Running '.format(name, os.getpid()))


if __name__ == '__main__':
    print('Parent process {0} is Running'.format(os.getpid()))
    for i in range(5):
        p = multiprocessing.Process(target=run_proc, args=(str(i),))
        print('process start')
        p.start()
    p.join()  # 这一句加上就表示等所有子进程执行完了，在执行后面的代码
    print('Process close')

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
