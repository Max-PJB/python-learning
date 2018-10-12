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
import time

__author__ = 'Max_Pengjb'
start = time.time()
# 下面写上代码块
"""
生成器 (Generator)
生成器是一类特殊的迭代器，它是一种更为高级、更为优雅的迭代器。
在Python中有两种类型的生成器：生成器函数以及生成器表达式。
生成器函数
生成器函数与一个普通函数很像，但是当它要返回一个值时，用的不是return，而是yield。只要函数中使用了yield关键字，他就变成了一个生成器函数：
    def Fun1():
        yield 1
        yield 2
上面例子中的Fun1就是一个生成器函数，它使用了两条yield语句。
如果熟悉return语句的含义，就会对上面的函数感到奇怪：函数每次执行都会在执行完yield 1之后返回，下面的yield 2有什么意义呢？
这正是yield与return语句不同的地方。一般的函数在调用时会立刻执行函数体，直到遇到return语句返回一个值（当然也可以不返回任何值，此处只讨论有返回值的情况）。
而生成器函数不同，他会返回一个生成器，并不立刻执行函数，只有当对生成器进行next操作时，才会真正开始执行函数，我们称这种特性为延迟计算（Lazy Evaluation）
并且，每一次进行next操作，函数会从上一个yield语句（或者函数第一条语句）执行到下一个yield语句（或者函数结尾），然后返回yield的值（或者引发StopIteration异常）：
    def Fun1():
        print("yield 1") #语句1
        yield 1 #语句2
        print("yield 2") #语句3
        yield 2 #语句4
    g = Fun1() #获得一个生成器
    print("before next")
    print(next(g))
    print(next(g))
上面的结果是：
before next
yield 1
1
yield 2
2
可以看到直到程序运行到print(next(g))时，Fun1函数才真正开始执行，第一条next使函数从语句1运行到了语句2，第二条next使函数从语句3运行到了语句4，就像函数发生了暂停，下一次调用时就从暂停的位置继续运行。
生成器函数强大的地方在于，它不仅能保存执行流程，执行过程中的局部变量也是能保存的：
    def Fun1():
        n = 0
        yield n
        n += 1
        yield n
        n += 1
        yield n
    g = Fun1()
    for s in g: #生成器也是一个迭代器，所以也可以使用for语句
        print(s)
得到的结果是：
0
1
2
每次yield语句之后局部变量n的值都会保存下来，下次next时能够继续使用上一次的n值。
有了这些特性，我们就可以更加优雅的创建迭代器了：
    def Fun1(max):
        start = 0
        while start < max:
            yield start
            start += 1
    g = Fun1(3) #得到一个能返回0-2的生成器
    for s in g:
        print(s)
得到的结果：
0
1
2
通常，我们将这种能够中断执行，之后又能从断点以上一次的状态继续执行的函数叫做协程（Coroutine）。
列表生成式
要介绍生成器表达式，首先需要了解一下列表生成式。
列表生成式是一种创建列表的方式，当我们要创建一个满足特定条件的列表时，使用它就非常方便。
比如我们要创建一个包含0到10的平方的列表，传统的做法是：
    data = []
    for x in range(11):
        data.append(x * x)
而使用列表生成式，就可以一行语句创建：
    data =[x*x for x in range(11)]
方括号里的左边部分是一个表达式x*x，代表列表元素怎么计算得来，右边是用for来表示的范围。
如果要进行条件筛选，可以在for后面带上if语句：
    data =[x*x for x in range(11) if x % 2 == 0]
    #生成包含0-10中偶数的平方的列表
不仅如此，for语句还能嵌套：
    data = [x*y for x in range(11) if x %2 == 0 for y in range(11)]
    #列表中的元素是第一个for代表的[0,2,4,6,8,10]与第二个for代表的[0,1,2.....,9,10]中每个元素分别相乘的结果，共6*11=66项
生成器表达式
生成器表达式与列表生成式语法基本一样，只是把方括号[]换成圆括号()：
    data = (x*x for x in range(11))
此时data是一个生成器，还没有包含0-10的平方项的元素。只有使用next函数调用时，才会一项一项的返回元素：
    data = (x*x for x in range(11))
    print(next(data))
    print(next(data))
    print(next(data))

得到的结果：
0
1
4
可见，它也满足延迟计算的特点。
与使用列表生成式马上创建一个包含指定元素的列表的方法相比，使用生成器表达式更节省内存空间，尤其当我们只是需要遍历一个满足特殊要求的序列时：
    data = [x*x for x in range(100000)] #一下子需要生成100000个元素，内存占用很大
    data2 = (x*x for x in range(100000)) #只创建一个生成器，每次只保存当前x的值，需要时就计算下一个值，节省内存空间
编程要求
根据提示，在右侧编辑器补充代码，实现myrange的功能。
myrange函数接受三个参数start，stop，step，就如同Python内置的函数range一样，start代表起始值，stop代表结束值（不包括），step代表步长。返回值是一个包含这一范围内的元素的迭代器。
测试说明
每组测试有4个数据输入，代表start，stop，step，n，其中start，stop，step为任意整数，n大于等于0。4个输入的数据由测试代码读取，不需要学员处理。
测试代码会将前三个数据作为参数调用myrange函数，然后使用for来打印返回的迭代器中最多n个值。
测试输入：1 2 1 5
输出：
1
测试输入：0 7 1 3
输出：
0
1
2
这一组数据虽然会生成一个有7个数据的迭代器，但由于n是3，所以只输出前3个数据。"""


def myrange(start, stop, step):
    # 补充这个生成器函数的代码，实现要求的功能
    k = start
    if step < 0:
        while k > stop:
            yield k
            k += step
    else:
        while k < stop:
            yield k
            k += step


# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
