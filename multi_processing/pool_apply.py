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
# 下面写上代码块
"""
apply 和 apply_async 的区别

apply是阻塞式的。
首先主进程开始运行，碰到子进程，操作系统切换到子进程，等待子进程运行结束后，在切换到另外一个子进程，直到所有子进程运行完毕。然后在切换到主进程，运行剩余的部分。

apply_async是异步非阻塞式的。
首先主进程开始运行，碰到子进程后，主进程说：让我先运行个够，等到操作系统进行进程切换的时候，再交给子进程运行。以为我们的程序太短，然而还没等到操作系统进行进程切换，主进程就运行完毕了。想要子进程执行，就告诉主进程：你等着所有子进程执行完毕后，在运行剩余部分。

一般建议：废弃apply，使用apply_async。
"""


def run_task(name):
    print('Task {0} pid {1} is running, parent id is {2}'.format(name, os.getpid(), os.getppid()))
    time.sleep(1)
    print('Task {0} end.'.format(name))


if __name__ == '__main__':
    print('current process {0}'.format(os.getpid()))
    p = multiprocessing.Pool(processes=3)
    for i in range(6):
        p.apply(run_task, args=(i,))
    print('Waiting for all subprocesses done...')  # 这个要等子进程全执行完，按照顺序来，和单进程没有区别啦
    p.close()
    p.join()
    print('All processes done!')

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



