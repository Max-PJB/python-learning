#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/21 19:40
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""
__author__ = 'Max_Pengjb'

"""
类似__xxx__这种格式的变量是特殊变量，允许被直接引用，但是会被用作特殊用途，比如__author__、__name__就是属于特殊变量。hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己编程定义的变量一般不会用这种变量名。

类似_xxx和__xxx这种格式的函数和变量就是非公开的（private），不应该被直接引用。

补充：_xxx的函数和变量变量是protected，我们直接从外部访问不会产生异常。__xxx的函数和变量是private，我们直接从外部访问会报异常，我们要注意前缀符合的区别。

我们要注意用词的区别，我们说的是private函数和变量是“不应该”被直接引用，而不是“不能”被直接引用，这是因为在Python种并没有一种方法可以真正完全限制访问private函数或变量。但是我们为了养成良好的编程习惯，是不应该引用private函数或变量的。

private函数的作用是隐藏函数的内部逻辑，让函数有更好的封装性。
"""


# 例如：

def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


"""
我们在上述程序块里公开了greeting()函数，greeting()函数需要使用_private_1()和_private_2()函数，读者并不需要知道greeting()函数中的内部实现细节。所以我们可以将内部逻辑用private函数隐藏起来。这是一种十分常用的代码封装的方法。

小结：为了让程序的封装性更好，我们一般都限定函数的使用范围，一般我们把外部需要使用的函数定义为public函数，而把只在内部使用，而外部不需要引用的函数定义成private函数。
"""
