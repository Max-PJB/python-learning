#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/22 15:44
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

"""
内置模块

Python中常见的内置模块如下：

    os模块：（文件和目录）用于提供系统级别的操作。
    sys模块：用于提供对解释器相关的操作。
    json模块：处理JSON字符串。
    logging: 用于便捷记录日志且线程安全的模块。
    time&datetime模块：时间相关的操作，时间有三种表示方式。
    hashlib模块：用于加密相关操作，代替了md5模块，主要是提供SHA1，SHA224，SHA256，SHA384，SHA512，MD5算法。
    random模块：提供随机数。
    
Python3 内置函数
注意：有些函数与 Python2.x 变化不大，会直接跳转到 Python2.x 教程下的内置函数说明，大家要注意下哈。
内置函数		
abs()	dict()	help()	min()	setattr()
all()	dir()	hex()	next()	slice()
any()	divmod()	id()	object()	sorted()
ascii()	enumerate()	input()	oct()	staticmethod()
bin()	eval()	int()	open()	str()
bool()	exec()	isinstance()	ord()	sum()
bytearray()	filter()	issubclass()	pow()	super()
bytes()	float()	iter()	print()	tuple()
callable()	format()	len()	property()	type()
chr()	frozenset()	list()	range()	vars()
classmethod()	getattr()	locals()	repr()	zip()
compile()	globals()	map()	reversed()	__import__()
complex()	hasattr()	max()	round()	 
delattr()	hash()	memoryview()	set()	
"""
# abs()：返回数值的绝对值
print(abs(-1))
# divmod()：返回两个数值的商和余数
print(divmod(7, 2))
print(divmod(7, 2)[0])
print(divmod(7, 2)[1])
# max()：返回元素中的最大值
print(max(2, 6, 1, 7))
# min()：返回元素中的最小值
print(min(2, 6, 1, 7))
# sum()：返回传入元素之和,
"""
注意这里sum()的用法，他只接收2个参数，第一个参数可以都是 list，元组 等迭代器。
以下是 sum() 方法的语法:

sum(iterable[, start])

参数

    iterable -- 可迭代对象，如：列表、元组、集合。
    start -- 指定相加的参数，如果没有设置这个值，默认为0。

"""
print(sum([2, 6, 1, 7], 3))
print(sum((2, 6, 1, 7)))

# all()：判断可迭代对象的每个元素是否都为True值,只要有一个为假就判断False
# 例如：
print(all([1, 2, 3]))  # 列表中每个元素逻辑值均为True，返回True
# True
print(all([0, 1, 2]))  # 列表中0的逻辑值为False，返回False
# False
print(all(()))  # 空元组
# True

# any()：判断可迭代对象的元素是否有为True值的元素，只要有一个真的就判断 True
# 例如：
print(any([0, 1, 2]))  # 列表元素有一个为True，则返回True
# True
print(any([0, 0]))  # 列表元素全部为False，则返回False
# False
print(any([]))  # 空列表
# False
