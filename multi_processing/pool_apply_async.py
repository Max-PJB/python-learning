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
import os
import time

__author__ = 'Max_Pengjb'
start = time.time()

"""
Pool 类

如果进程数太多了，我一个人根本搞不过来，怎么办呢？还好有进程池Pool这个好基友啊，简单来说，Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。

Pool可以提供指定数量的进程供用户使用，默认是 CPU 核数。当有新的请求提交到Pool的时候，如果池子没有满，会创建一个进程来执行，否则就会让该请求等待。

    Pool对象调用join方法会等待所有的子进程执行完毕
    调用join方法之前，必须调用close
    调用close之后就不能继续添加新的Process了

pool.apply_async

apply_async方法用来同步执行进程，允许多个进程同时进入池子。
apply_async是异步非阻塞的。
异步处理就是，你现在问我问题，我可以不回答你，等我有时间了再处理你这个问题。同步就反其道而行之，同步信息会立即被处理。
"""
# 下面写上代码块


def run_task(name):
    print('Task {0} pid {1} is running, parent id is {2}'.format(name, os.getpid(), os.getppid()))
    time.sleep(1)
    print('Task {0} end.'.format(name))


if __name__ == '__main__':
    print('current process {0}'.format(os.getpid()))
    p = multiprocessing.Pool(processes=3)
    for i in range(15):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocesses done...')  # 这里没有等待上面的子进程，而是直接执行了，所以直接打印出来了
    p.close()
    p.join()
    print('All processes done!')

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
