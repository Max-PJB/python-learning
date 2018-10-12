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

__author__ = 'Max_Pengjb'

"""
with如何工作？

这看起来充满魔法，但不仅仅是魔法，Python对with的处理还很聪明。基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。

紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
"""


class Sample:
    def __enter__(self):
        print("In __enter__()")

    def __init__(self):
        pass

    def __exit__(self, type, value, trace):
        print("In __exit__()")
        print("type:", type)
        print("value:", value)
        print("trace:", trace)

    def do_something(self):
        bar = 1/0
        return bar + 10


with Sample() as sample:
    print("sample:", sample)

"""
    正如你看到的，
    1.__enter__()方法被执行
    2.__enter__()方法返回的值 - 这个例子中是"Foo"，赋值给变量'sample'
    3.执行代码块，打印变量"sample"的值为"Foo"
    4.__exit__()方法被调用with真正强大之处是它可以处理异常。可能你已经注意到Sample类的__exit__方法有三个参数 - val, type和trace。 
    这些参数在异常处理中相当有用。我们来改一下代码，看看具体如何工作的。
"""
# with Sample() as sample:
#     sample.do_something()
sa = Sample()
sa.do_something()