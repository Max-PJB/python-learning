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
json库

json库是Python内置的一个用于操作JSON数据的库，提供了几个函数用于解析与生成（或者说反序列化与序列化）JSON格式的数据。
解析JSON数据

json库提供了一个函数loads用于从Python的字符串中解析JSON数据。
使用它的方法很简单，只需将含有JSON数据的字符串当做参数传递给它，它的返回值就是由Python中的基础数据类型组成的对象：

    import json
    data = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
    text = json.loads(data)
    print(text)

得到的结果是：
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

JSON的对象类型转换成了Python的dict类型。

JSON各种数据类型在解析后对应的Python基础数据类型如下表：
JSON 	Python
object(对象) 	dict
array(数组) 	list
string(字符串) 	unicode
number (int) 	int, long
number (real) 	float
true 	True
false 	False
null 	None

JSON数据类型转化成Python数据类型后就可以按照Python的方式来使用了：

    import json
    data = '[1,2,3]';
    text = json.loads(data)
    text.append(4) #调用list的append函数
    print(text)

得到的结果是：
[1, 2, 3, 4]

如果需要以不同的字符编码来解析，可以指定 encoding参数，比如：

    import json
    data = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
    text = json.loads(data,encoding = "utf-8")
    print(text)

上面的代码以utf-8的字符编码解析data字符串的数据。

注意：如果字符编码指定错误，有可能会导致解析失败引发异常。

json库的另一个函数load也是用于解析JSON数据的，它与loads函数唯一不同的地方在于，它是从文件中解析，比如：

    import json
    data = open("test.txt","r",encoding = "utf-8")
    text = json.load(data) #将文件对象传递给load函数
    print(text)
    fp.close()

这样test.txt文件内的内容就会被当做JSON格式的数据来解析。

注意：load函数没有可选参数encoding，只要文件对象使用了正确的字符编码打开文件，load函数就可以正确的解析数据。
生成JSON数据

与解析的那两个函数相对应，json库也提供了两个函数：dumps和dump来将由Python基础数据类型组成的对象转化成JSON数据，使用方法也类似：

    import json
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
    json = json.dumps(data) #转化成JSON格式的字符串
    print(json)

得到的结果是：
[{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}]
注意，这是一个字符串。

同样，在转化的时候也有一个Python基础数据类型到JSON数据类型的对应表格：
Python 	JSON
dict 	object
list, tuple 	array
str, unicode 	string
int, long, float 	number
True 	true
False 	false
None 	null

注意：dumps没有可选参数encoding，当要转化的对象含有中文等非ASCII字符时，建议指定可选参数ensure_ascii为False，否则非ASCII的字符将会被显示成\uXXXX的形式：

    data = {"name":"小明"}
    print(json.dumps(data)) #ensure_ascii默认值为True
    print(json.dumps(data,ensure_ascii= False)) #指定ensure_ascii为False

上面的代码的结果：
{"name": "\u5c0f\u660e"}
{"name": "小明"}

使用dump函数直接输出到文件也很简单，只需多传递一个文件对象作为参数：

    import json
    fp = open("test.txt","w")
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
    json.dump(data,fp) #转化成JSON格式的字符串后输出到文件
    fp.close()

test.txt文件的内容：
[{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}]

dump函数同样也没有可选参数encoding，如果有数据中有中文字符等非ASCII字符时，建议指定可选参数ensure_ascii为False。
"""