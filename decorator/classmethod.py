#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/31 18:48
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    装饰器 @classmethod
                     工厂模式的一个方法
                    class method可以用来为一个类创建一些预处理的实例.
                    类方法只能找类变量，不能访问实例变量，
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'


class Dog(object):
    name = "Jerry"

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(cls):
        print("%s is eating %s" % (cls.name, "food"))

    def talk(self):
        print("%s is talking" % self.name)


# 类方法只能找类变量，不能访问实例变量，
# 所以这里的name是jerry而不是实例化的tom
d = Dog("Tom")
d.eat()
Dog.eat()
