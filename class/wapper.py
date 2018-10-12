#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/25 20:20
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

"""
“包装”是指对一个已经存在的对象进行系定义加工。

实现授权是包装的一个特性。包装一个类型通常是对已存在的类型进行一些自定义定制，这种做法可以新建，修改，或删除原有产品的某些功能，
而其他的保持不变。授权的过程，其实也就是所有的更新功能都交给新类的自定义的某部分功能来处理，但已存在的功能就授权给对象的默认属性。

实现授权的关键点是覆盖__getattr__()
方法，在代码中包含一个对getattr()
内建函数的调用，调用getattr()
得到默认对象的属性，并返回它以便访问或者调用。


用组合的方式完成授权。
"""


class Cpu:  # 定义一个Cpu类
    def __init__(self, cpubrand, cpuprice):  # cpu的属性有品牌、价格等
        self.cpubrand = cpubrand
        self.cpuprice = cpuprice

    def calc(self):
        print("CPU是电脑的大脑，你能进行大量的计算")


class Mainboard:  # 定义一个主板类
    def __init__(self, mbprice, mbsize):  # 主板的属性有价格和型号
        self.mbprice = mbprice
        self.mbsize = mbsize

    def connect(self):
        print("主板类似于人类的脊椎神经，它能够将显卡、声卡等设备联系起来")


class Computer:  # 定义一个电脑类
    def __init__(self, comprice, combrand, cpuprice, cpubrand, mbprice, mbsize):
        self.comprice = comprice
        self.combrand = combrand
        self.cpu = Cpu(cpuprice, cpubrand)
        self.mainboard = Mainboard(mbprice, mbsize)

    def play_game(self):
        print("嘿嘿，我们可以用电脑来玩游戏啊")

    def __getattr__(self, item):                  #这一步是实现授权的方式
        return getattr(self.cpu, item)


com = Computer(6999, "三星", 2345, "intel", 1800, 'B53')
com.calc()

# com.calc()方法的调用方式，
# 首先，他会从com的属性字典去查找calc属性，
# 发现该实例属性中不存在，然后去Computer类的属性字典去查找calc属性，
# 发现也不存在，就触发了__getattr__()方法，
#__getattr__()
#一运行，就会调用getattr(self.cpu, "calc"）方法的运行，得到一个内存地址传给了com.calc，然后运行。
