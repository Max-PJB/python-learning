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
import math
from multiprocessing import cpu_count
from multiprocessing import Pool

__author__ = 'Max_Pengjb'


# 对整个数字空间N进行 分段CPU_COUNT
def seprateNum(N, CPU_COUNT):
    list = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)] for i in range(0, CPU_COUNT)]
    list[0][0] = 1
    if list[CPU_COUNT - 1][1] < N:
        list[CPU_COUNT - 1][1] = N
    return list


def get_max(list):
    if list:
        x = list[0]
        for i in list:
            if x < i:
                x = i
        return x


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
if __name__ == '__main__':
    CPU_COUNT = cpu_count()
    pool = Pool(CPU_COUNT)

    ml = map(int, input().split())
    # python3下的map()函数返回类型为iterators，不再是list，所以可将上述语句修改为
    # print(next(ml))
    # print(next(ml))
    # print(next(ml))
    ml = list(ml)
    N = len(ml)
    sepList = seprateNum(N, CPU_COUNT)
    result = []
    for i in range(CPU_COUNT):
        result.append(pool.apply_async(get_max, (ml[sepList[i][0] - 1:sepList[i][1]:1],)))
    pool.close()
    pool.join()
    # 去除结果中的 None  [res.get() for res in result] 当数据少时会产生None
    list = [x for x in [res.get() for res in result] if x is not None]
    print(list)
    print(get_max(list), end='')  # end='' 表示取消 /n

"""
多线程比多进程性能高？

误导！

应该说，多线程比多进程成本低，但性能更低。

在UNIX环境，多进程调度的开销和多线程调度的开销没有显著区别，就是说，UNIX进程调度效率是很高的。内存消耗方面，二者只差全局数据区，现在内存都很便宜，服务器内存动辄若干G，根本不是问题。

多进程是立体交通系统，虽然造价高，上坡下坡多耗点油，但是不堵车。

多线程是平面交通系统，造价低，但红绿灯太多，老堵车。

我们现在都开跑车，油（主频）有的是，不怕上坡下坡，就怕堵车。
线程和进程的优缺点

我们介绍了多进程和多线程，这是实现多任务最常用的两种方式。现在，我们来讨论一下这两种方式的优缺点。

多进程：

　　多进程优点：

    每个进程互相独立，不影响主程序的稳定性，子进程崩溃没关系；

    通过增加CPU，就很容易扩充性能；

    可以尽量减少线程加锁/解锁的影响，极大提高性能，就算是线程运行的模块算法效率低也没关系；

    每个子进程都有2GB地址空间和相关资源，总体能够达到的性能上限非常大。

　　多进程缺点：

    逻辑控制复杂，需要和主程序交互；

    需要跨进程边界，如果有大量数据需要传送，就不太好，适合少量数据传送、密集运算，多进程调度开销比较大；

    最好是多进程和多线程结合，即根据实际的需要，每个CPU开启一个子进程，这个子进程开启多线程可以为若干同类型的数据进行处理。当然你也可以利用多线程+多CPU+轮询方式来解决问题……

    方法和手段是多样的，关键是自己看起来实现方便有能够满足要求，代价也合适。

多线程：

　　多线程的优点：

    无需跨进程边界；

    程序逻辑和控制方式简单；

    所有线程可以直接共享内存和变量等；

    线程方式消耗的总资源比进程方式好。

　　多线程缺点：

    每个线程与主程序共用地址空间，受限于2GB地址空间；

    线程之间的同步和加锁控制比较麻烦；

    一个线程的崩溃可能影响到整个程序的稳定性；

    到达一定的线程数程度后，即使再增加CPU也无法提高性能，例如Windows Server 2003，大约是1500个左右的线程数就快到极限了（线程堆栈设定为1M），如果设定线程堆栈为2M，还达不到1500个线程总数；

    线程能够提高的总性能有限，而且线程多了之后，线程本身的调度也是一个麻烦事儿，需要消耗较多的CPU。
    线程切换

无论是多进程还是多线程，只要数量一多，效率肯定上不去，为什么呢？

我们打个比方，假设你不幸正在准备中考，每天晚上需要做语文、数学、英语、物理、化学这5科的作业，每项作业耗时1小时。

如果你先花1小时做语文作业，做完了，再花1小时做数学作业，这样，依次全部做完，一共花5小时，这种方式称为单任务模型，或者批处理任务模型。

假设你打算切换到多任务模型，可以先做1分钟语文，再切换到数学作业，做1分钟，再切换到英语，以此类推，只要切换速度足够快，这种方式就和单核CPU执行多任务是一样的了，以幼儿园小朋友的眼光来看，你就正在同时写5科作业。

但是，切换作业是有代价的，比如从语文切到数学，要先收拾桌子上的语文书本、钢笔（这叫保存现场），然后，打开数学课本、找出圆规直尺（这叫准备新环境），才能开始做数学作业。操作系统在切换进程或者线程时也是一样的，它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。

所以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好。
线程和进程的应用场景

是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型。

计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。

计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。

IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差
"""