#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/2 16:36
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   Python3 timeit的用法

Python3中的timeit模块可以用来测试小段代码的运行时间

其中主要通过两个函数来实现：timeit和repeat，代码如下：

def timeit(stmt="pass", setup="pass", timer=default_timer,
           number=default_number, globals=None):
    Convenience function to create Timer object and call timeit method.
    return Timer(stmt, setup, timer, globals).timeit(number)


def repeat(stmt="pass", setup="pass", timer=default_timer,
           repeat=default_repeat, number=default_number, globals=None):
    Convenience function to create Timer object and call repeat method.
    return Timer(stmt, setup, timer, globals).repeat(repeat, number)

在上面的代码中可见，无论是timeit还是repeat都是先生成Timer对象，然后调用了Timer对象的timeit或repeat函数。

在使用timeit模块时，可以直接使用timeit.timeit()、tiemit.repeat()，还可以先用timeit.Timer()来生成一个Timer对象，然后再用TImer对象用timeit()和repeat()函数，后者再灵活一些。

上述两个函数的入参：

stmt：用于传入要测试时间的代码，可以直接接受字符串的表达式，也可以接受单个变量，也可以接受函数。传入函数时要把函数申明在当前文件中，然后在 stmt = ‘func()’ 执行函数，然后使用 setup = ‘from __main__ import func’

setup：传入stmt的运行环境，比如stmt中使用到的参数、变量，要导入的模块等。可以写一行语句，也可以写多行语句，写多行语句时要用分号；隔开语句。

number：要测试的代码的运行次数，默认100000次，对于耗时的代码，运行太多次会比较慢，此时建议自己修改一下运行次数

repeat：指测试要重复几次，每次的结果构成列表返回，默认3次。
-------------------------------------------------
"""
import time
import timeit

__author__ = 'Max_Pengjb'
start = time.time()

# 下面写上代码块

print(timeit.timeit(stmt='list(i**2 for i in normal_list)', setup='normal_list=range(10000)', number=10))
# 0.3437936799875755
print(timeit.repeat(stmt='list(i**2 for i in normal_list)', setup='normal_list=range(10000)', repeat=2, number=10))
# [0.33649995761778984, 0.3394490767789293]
# setup 为复合语句
print(timeit.timeit(stmt='list(i**2 for i in normal_list)', setup='a=10000;normal_list=range(a)', number=10))
# 0.33272367424748817
print(timeit.repeat(stmt='list(i**2 for i in normal_list)', setup='a=10000;normal_list=range(a)', repeat=2, number=10))
# [0.3323106610316342, 0.3356380911962764]




# 生成timer
timer1 = timeit.Timer(stmt='list(i**2 for i in normal_list)', setup='normal_list=range(10000)')
# 调用timeit和repeat时还传number和repeat参数
print(timer1.timeit(number=10))
# 0.34721554568091145
print(timer1.repeat(repeat=2, number=10))
# [0.3391925079630199, 0.34103400077255097]

# setup 为复合语句
timer1 = timeit.Timer(stmt='list(i**2 for i in normal_list)', setup='a=10000;normal_list=range(a)')
print(timer1.timeit(number=10))
# 0.34383463997592467
print(timer1.repeat(repeat=2, number=10))
# [0.34573984832288773, 0.34413273766891006]

# stmt为函数
def func():
    normal_list = range(10000)
    L = [i ** 2 for i in normal_list]


timer1 = timeit.Timer("func()", setup="from __main__ import func")
print(timer1.timeit(number=10))
# 0.1223264363160359
print(timer1.repeat(repeat=2, number=10))


# [0.12266321844246209, 0.1264150395975001]

def func():
    normal_list = range(10000)
    L = [i ** 2 for i in normal_list]


# stmt为函数
print(timeit.timeit("func()", setup="from __main__ import func", number=10))
# 0.12436874684622312
print(timeit.repeat("func()", setup="from __main__ import func", repeat=2, number=10))
# [0.12142133435126468, 0.12079555675148601]


# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
