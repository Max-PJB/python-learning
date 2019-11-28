#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/27 11:23
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
from functools import wraps
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()

"""
首先解释一下 @ 语法
@funcA
def funcB()

其实就相当于  funcB = funcA(funcB)

@funcA(arg1)
def funcB()

那就是相当于 funcB = funcA(arg1)(funcB)
"""


# 下面写上代码块
def my_decorator1(func):
    def wrapper(*args, **kwargs):
        print("my_decorator11111,before")
        r = func(*args, **kwargs)
        print("my_decorator11111,after")
        return r

    return wrapper


def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print("my_decorator22222,before")
        r = func(*args, **kwargs)
        print("my_decorator22222,after")
        return r

    return wrapper


def my_decorator3(func):
    def wrapper(*args, **kwargs):
        print("my_decorator3333,before")
        r = func(*args, **kwargs)
        print("my_decorator33333,after")
        return r

    return wrapper


@my_decorator1
@my_decorator2
@my_decorator3
def my_func(x, y):
    print(x + y)
    return x + y


# 多个装饰器执行的顺序是 进入的时候 1->2->3  return退出的时候 ->3->2->1,类似进入一个圆到圆心，然后又出来
# my_func(1, 3)
# my_func(1, 3)


# 高阶，带参数的装饰器
def my_decorator4(myarg1, myarg2):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("my_decorator44444,before")
            print(myarg1)
            r = func(*args, **kwargs)
            print("my_decorator44444,after")
            print(myarg2)
            return r

        return inner_wrapper

    return wrapper


@my_decorator4("haha", "hehe")
def my_func2(x, y):
    print(x + y)
    return x + y


r = my_func2(4, 5)
print(r)

#  @wrapper 作用  @wraps：避免被装饰函数自身的信息丢失
#  上面的my_func1，my_func2 我们打印一下信息看看。
print(my_func.__name__, my_func2.__name__)  # wrapper inner_wrapper 导致函数本身的信息丢失


# 因为当使用装饰器装饰一个函数时，函数本身就已经是一个新的函数；即函数名称或属性产生了变化。
# 所以在python的functools模块中提供了wraps装饰函数来确保原函数在使用装饰器时不改变自身的函数名及应有属性。
# 所以在装饰器的编写中建议加入wraps确保被装饰的函数不会因装饰器带来异常情况。


# 使用  @wraps 后
def my_decorator5(myarg1, myarg2):
    def out_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            print("my_decorator44444,before")
            print(myarg1)
            r = func(*args, **kwargs)
            print("my_decorator44444,after")
            print(myarg2)
            return r

        return inner_wrapper

    return out_wrapper


@my_decorator5("haha", "hehe")
def my_func3(x, y):
    print(x + y)
    return x + y


my_func3(6, 7)
print(my_func3.__name__)


# 基于类实现的装饰器
# 装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。
# 在Python中一般callable对象都是函数，但也有例外。只要某个对象重载了__call__()方法，
# 那么这个对象就是callable的。重载__call__魔法方法一般会改变对象的内部行为，让一个类对象拥有了被调用的行为。
# ————————————————
# 原文链接：https://blog.csdn.net/luoz_java/article/details/90339876

class Test():
    def __call__(self):
        print('call me!')


t = Test()
t()  # call me


# 装饰器要求接受一个callable对象，并返回一个callable对象（不太严谨，详见后文）。
# 那么用类来实现也是也可以的。我们可以让类的构造函数__init__()接受一个函数，然后重载__call__()并返回一个函数，
# 也可以达到装饰器函数的效果。
class logging(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('[DEBUG]: enter function {func}()'.format(
            func=self.func.__name__))
        return self.func(*args, **kwargs)


@logging
def say(something):
    print('say {}'.format(something))


say('love you.')


# [DEBUG]: enter function say()
# say love you.

# 带参数的类装饰器
class logging2(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):  # 接受函数
        def wrapper(*args, **kwargs):
            print('[{level}]: enter function {func}()'.format(
                level=self.level,
                func=func.__name__))
            func(*args, **kwargs)

        return wrapper  # 返回函数


@logging2(level='INFO')
def say2(something):
    print('say {}'.format(something))


say2('love you.')
print(say.__name__)  # wrapper

# 上面中间写上代码块

end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
