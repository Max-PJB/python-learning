#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/19 
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""
__author__ = 'Max_Pengjb'

List = ['Zhang san', 'Li si', 'Wang wu', 'Zhao liu']

# insert()方法，可以在列表任意指定位置插入元素，其基本语法为：
# source_list.insert(index,obj)
List.insert(1, 'insert')
# append()方法向一个列表的尾部追加一个元素，其基本语法如下：
# source_list.append(obj)
List.append("append")
# pop()方法来删除元素，该方法将从源列表删除对应元素，同时返回被删除的元素。其基本语法如下：
# deleted_obj = source_list.pop(index)
List.pop(2)
# remove()方法，可以直接通过元素值来删除对应的元素。其基本语法如下：
# source_list.remove(obj)
List.remove("Wang wu")

print(List)

# tep1：将guests列表末尾的元素删除，并将这个被删除的元素值保存到deleted_guest变量
#
# step2：将deleted_guest插入到step1删除后的guests列表索引位置为2的地方；
#
# step3: 将step2处理后的guests列表索引位置为1的元素删除
#
# 打印输出step1的deleted_guest变量。
#
# 打印输出step3改变后的guests列表；
del_x = List[len(List)-1]
List.pop(len(List)-1)
List.insert(2, del_x)
List.pop(1)
print(del_x)
print(List)

print(max(list(range(10)), key=lambda x: x > 3))

# step1: 根据给定的下限数lower, 上限数upper以及步长step, 利用range函数生成一个列表
# step2: 计算该列表的长度
# step3: 求该列表中的最大元素与最小元素之差
lower = int(input())
upper = int(input())
step = int(input())

List1 = list(range(lower, upper, step))
print(len(List1))
print(max(List1) - min(List1))

# list的切片操作
# list[start:end:step]
# start：切片起始索引位置，省略则从头开始
# end：切片结束索引位置，省略则切至列表末尾
# step：切片步长，可选参数，表示每N个元素取一个，默认为1

a = [1, 2, 3, 4, [5, 5], 6, 7, 8, 9]
print(a[::2])
print(a[-4:-1:])
print(a[:8:])
print(a[::-1])
print(a[1:3:-2])

# 利用切片方法从my_menu列表中每3个元素取1个，组成子序列并打印输出；
# 利用切片方法获取my_menu列表的最后三个元素组成子序列并打印输出。
b = ["pizza", "chicken", "carrot", "apple", "banana"]
print(b[::3])
print(b[-3::])
print(b[-3::-1])
print(b[3::-1])
print(b[:-3:-1])
print(b[:3:-1])
print("sss")
print(a[9:-4:-1])
print(a[-1:-4:-1])
print(a[1:4:-1])
print(a[-1:4:-1])

menu1 = {'fish': 40, 'pork': 30}
menu3 = [1, 2, 3]
print(menu1)
print(list(map(lambda x, y: x, menu1, menu3)))

#字典的遍历方式
dic={"a":1,"b":2,"c":3}
for k in dic:
    print (k,dic[k])
for k,v in dic.items():#dic.iteritems()不再存在
    print (k,v)
#字典的合并方法
#dic.items()的类型是dict.items,不再能相加
#dic3=dic(dic1,**dic2)也不能使用
dic1={1:"a",2:"b",3:"c"}
dic.update(dic1)
print (dic)