#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/25 17:31
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块


class A:
    def go(self):
        print("go A go!")

    def stop(self):
        print("stop A stop!")

    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")


class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")

    def stop(self):
        super(C, self).stop()
        print("stop C stop!")


class D(B, C):
    def go(self):
        super(D, self).go()
        print("go D go!")

    def stop(self):
        super(D, self).stop()
        print("stop D stop!")

    def pause(self):
        print("wait D wait!")


class E(B, C):
    pass


a = A()
b = B()
c = C()
d = D()
e = E()
# 说明下列代码的输出结果
a.go()
print('--------')
b.go()
print('--------')
c.go()
print('--------')
d.go()
print('--------')
e.go()
print('--------')
a.stop()
print('--------')
b.stop()
print('--------')
c.stop()
print('--------')
d.stop()
print('--------')
e.stop()
print(D.mro())
a.pause()
b.pause()
c.pause()
d.pause()
e.pause()


class A1:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B1(A1):
    def __init__(self):
        super().__init__()
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        print('newb')
        self.n += 3


class C1(A1):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        print('newc')
        self.n += 4


class D1(B1, C1):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5


d = D1()
d.add(2)
print(d.n)

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
