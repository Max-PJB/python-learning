#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/22 12:37
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""
from collections import Iterator, Iterable

__author__ = 'Max_Pengjb'

"""
1.迭代器的应用场景

1).如果数列的数据规模巨大

2).数列有规律，但是依靠列表推导式描述不出来

2.
数学中有个著名的斐波拉契数列（Fibonacci），数列中第⼀个数0，第⼆个数1，其后的每⼀个数都可由前两个数相加得到：

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

现在我们想要通过for... in ...
循环来遍历迭代斐波那契数列中的前n个数。那么这个斐波那契数列我们就可以⽤迭代器来实现，每次迭代都通过数学计算来⽣成下⼀个数。
"""


class FibIterator(object):
    """
    fib数列迭代器
    """
    def __init__(self, n):
        """"""
        self.num1 = 0
        self.num2 = 1
        self.n = n  # 用来保存迭代的总次数
        self.i = 0  # 用来记录迭代次数

    def __next__(self):
        # 判断是否迭代结束，如果没有到达迭代次数，则返回数据
        if self.i < self.n:
            # 保存要返回的值
            item = self.num1
            # 计算num1, num2的值，方便下次迭代返回
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            # 记录迭代次数
            self.i += 1
            return item
        else:
            # 到达了迭代次数，抛出异常
            raise StopIteration

    def __iter__(self):
        return self

fib = FibIterator(20)
print(next(fib))
li = list(fib)
print(li)
print(fib)
print(isinstance(fib, Iterator))
print(isinstance(fib, Iterable))

# 当输入一个列表时，填入将列表List转换为迭代器的代码
# 填入用next()
# 函数遍历迭代器IterList的代码
List = []
member = input()
for i in member.split(','):
    result = i
    List.append(result)


# 请在此添加代码，将List转换为迭代器的代码
# ********** Begin *********#
class my_iterator(object):
    def __init__(self, obj):
        self.List = obj
        self.i = 0
        self.n = len(self.List)

    def __next__(self):
        if self.i < self.n:
            index = self.i
            self.i += 1
            return self.List[index]
        else:
            raise StopIteration

    def __iter__(self):
        return self

hehe = my_iterator(List)
print(list(hehe))
# ********** End **********#
while True:
    try:
        # 请在此添加代码，用next()函数遍历IterList的代码
        # ********** Begin *********#
        num = next(hehe)
        # ********** End **********#
        result = int(num) * 2
        print(result)
    except StopIteration:
        break