#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/5 20:47
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import functools


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(D, C, A):
    pass


@functools.singledispatch
def myfunc(arg):
    print("11111111")
    print('default myfunc({})'.format(arg.__class__.__name__))


@myfunc.register(A)
def myfunc_A(arg):
    print("AAAAAAAAA")
    print('myfunc_A({})'.format(arg.__class__.__name__))


@myfunc.register(B)
def myfunc_B(arg):
    print("BBBBBBBBBB")
    print('myfunc_B({})'.format(arg.__class__.__name__))


@myfunc.register(C)
def myfunc_C(arg):
    print("CCCCCC")
    print('myfunc_C({})'.format(arg.__class__.__name__))


myfunc(A())
myfunc(B())
myfunc(C())
myfunc(D())
myfunc(E())
