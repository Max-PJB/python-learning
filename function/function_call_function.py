#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/22 19:38
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'


def x(f):
    def y():
        print(1)

    return y


def f():
    print(2)


x(f)
x(f())
x(f())()