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
import threading

__author__ = 'Max_Pengjb'


"""
多线程的全局变量同步问题

首先借助一个小程序来看看多线程环境下全局变量的同步问题。

    import threading
    global_num = 0
    def thread_cal():
        global global_num
        for i in xrange(1000):
            global_num += 1
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=thread_cal))
        threads[i].start()
    for i in range(10):
        threads[i].join()
    print global_num

这里我们创建了10个线程，每个线程均对全局变量global_num进行1000次的加1操作（循环1000次加1是为了延长单个线程执行时间，使线程执行时被中断切换），当10个线程执行完毕时，全局变量的值是多少呢？答案是不确定。简单来说是因为 global_num += 1 并不是一个原子操作，因此执行过程可能被其他线程中断，导致其他线程读到一个脏值。以两个线程执行+1为例，其中一个可能的执行序列如下（此情况下最后结果为1）：

多线程中使用全局变量时普遍存在这个问题，解决办法也很简单，可以使用互斥锁、条件变量或者是读写锁。下面考虑用互斥锁来解决上面代码的问题，只需要在进行+1运算前加锁，运算完毕释放锁即可，这样就可以保证运算的原子性。

    l = threading.Lock()
    ...
        l.acquire()
        global_num += 1
        l.release()

在线程中使用局部变量则不存在这个问题，因为每个线程的局部变量不能被其他线程访问。下面我们用10个线程分别对各自的局部变量进行1000次加1操作，每个线程结束时打印一共执行的操作次数（每个线程均为1000）：

    def show(num):
        print threading.current_thread().getName(), num
    def thread_cal():
        local_num = 0
        for _ in xrange(1000):
            local_num += 1
        show(local_num)
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=thread_cal))
        threads[i].start()

可以看出这里每个线程都有自己的 local_num，各个线程之间互不干涉。
Thread-local 对象

上面程序中我们需要给 show 函数传递 local_num 局部变量，并没有什么不妥。不过考虑在实际生产环境中，我们可能会调用很多函数，每个函数都需要很多局部变量，这时候用传递参数的方法会很不友好。

为了解决这个问题，一个直观的的方法就是建立一个全局字典，保存进程 ID 到该进程局部变量的映射关系，运行中的线程可以根据自己的 ID 来获取本身拥有的数据。这样，就可以避免在函数调用中传递参数，如下示例：

示例如下：

    global_data = {}
    def show():
        cur_thread = threading.current_thread()
        print cur_thread.getName(), global_data[cur_thread]
    def thread_cal():
        cur_thread = threading.current_thread()
        global_data[cur_thread] = 0
        for _ in xrange(1000):
            global_data[cur_thread] += 1
        show()  # Need no local variable.  Looks good.
    ...

保存一个全局字典，然后将线程标识符作为key，相应线程的局部数据作为 value，这种做法并不完美。首先，每个函数在需要线程局部数据时，都需要先取得自己的线程ID，略显繁琐。更糟糕的是，这里并没有真正做到线程之间数据的隔离，因为每个线程都可以读取到全局的字典，每个线程都可以对字典内容进行更改。

为了更好解决这个问题，python 线程库实现了 ThreadLocal 变量（很多语言都有类似的实现，比如Java）。ThreadLocal 真正做到了线程之间的数据隔离，并且使用时不需要手动获取自己的线程 ID，如下示例：

    global_data = threading.local()
    def show():
        print threading.current_thread().getName(), global_data.num
    def thread_cal():
        global_data.num = 0
        for _ in xrange(1000):
            global_data.num += 1
        show()
    threads = []
    ...
    print "Main thread: ", global_data.__dict__ # {}

上面示例中每个线程都可以通过 global_data.num 获得自己独有的数据，并且每个线程读取到的 global_data 都不同，真正做到线程之间的隔离。
"""


data = threading.local()


def action():
    global x
    data.num = x
    for i in range(1000000):
        data.num += 1
        data.num -= 1
    x = data.num


x = int(input())
thread = []
for i in range(10):
    thread.append(threading.Thread(target=action))
    thread[i].start()
for i in range(10):
    thread[i].join()
print(x)
