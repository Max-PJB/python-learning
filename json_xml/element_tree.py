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
import xml.etree.ElementTree as ET
__author__ = 'Max_Pengjb'


"""
ElementTree

xml.etree.ElementTree模块是一个轻量级的DOM(文件对象模型)，具有方便友好的API。代码可用性好，速度快，消耗内存少。
ElementTree模块大致可以三部分：ElementTree类，Element类以及一些操作 XML 的函数。

教程中所使用的data.xml文件的内容如下：

    <collection shelf="New Arrivals">
        <movie title="Enemy Behind">
           <type>War, Thriller</type>
           <description>Talk about a US-Japan war</description>
        </movie>
        <movie title="Transformers">
           <type>Anime, Science Fiction</type>
           <description>A schientific fiction</description>
        </movie>
        <movie title="Trigun">
           <type>Anime, Action</type>
           <description>Vash the Stampede!</description>
        </movie>
        <movie title="Ishtar">
           <type>Comedy</type>
           <description>Viewable boredom</description>
        </movie>
    </collection>

解析

xml.etree.ElementTree提供了两个函数：parse和fromstring，用于从文件和字符串解析XML数据，比如：

    import xml.etree.ElementTree as ET
    doc = ET.parse("data.xml") #从文件解析XML数据
    root = doc.getroot() #获取根元素
    data = "<a>hello</a>"
    el = ET.fromstring(data) #从字符串解析XML数据

parse函数返回一个ElementTree对象，fromstring返回一个Element对象。

Element对象代表一个XML元素，它的功能接下来会介绍。

ElementTree对象代表一个XML文档，它提供了函数getroot来获取一个文档的根元素，正如上面的例子中展示的那样。
查找元素

Element对象和ElementTree对象都提供了用于在子元素查找元素的函数：

    find(name)：用于在直接子元素中查找一个名为name的元素。
    findall(name)：用于在直接子元素中查找所有名为name的元素，它的返回值可以看做一个元素都是Element对象的tuple对象，，可以对它进行迭代操作或者索引[]操作。
    iter(name = None)：用于在当前元素下的所有子元素中查找名为name的元素，如果不指定name，则返回所有子元素。它返回一个迭代器对象。

比如：

    import xml.etree.ElementTree as ET
    doc = ET.parse("data.xml") #从文件解析XML数据
    root = doc.getroot() #获取根元素
    for s in root.findall("movie"): #选择所有名为moive的元素
            print(s.find("description").text) #打印出movie元素下description元素的文本

得到结果是：
Talk about a US-Japan war
A schientific fiction
Vash the Stampede!
Viewable boredom
获取元素的文本与属性值

Element有一个属性text，这个属性用于获取直接在这个元素的开始、结束标志之间的文本，如果没有文本，则返回空字符串：

    import xml.etree.ElementTree as ET
    data = "<a>TextA<b>TextB</b></a>"
    ele = ET.fromstring(data)
    print(ele.text)
    print(ele.find("b").text)

得到的结果是：
TextA
TextB

如果要获取一个元素的某个属性，可以使用get(name)函数，它会寻找当前元素上名为name的属性，如果找到就返回这个属性的值，没找到则返回空字符串。比如：

    import xml.etree.ElementTree as ET
    doc = ET.parse("data.xml") #从文件解析XML数据
    root = doc.getroot() #获取根元素
    for s in root.findall("movie"): #选择所有名为moive的元素
            de = s.find("description") #获取description元素
            print("%s: %s" % (s.get("title"),de.text)) #获取tile属性，与description元素的文本值格式化输出

得到的结果：
Enemy Behind: Talk about a US-Japan war
Transformers: A schientific fiction
Trigun: Vash the Stampede!
Ishtar: Viewable boredom

打印出了电影的名字与简介。
"""
data = '''
    <collection shelf="New Arrivals">
        <movie title="Enemy Behind">
           <type>War, Thriller</type>
           <description>Talk about a US-Japan war</description>
        </movie>
        <movie title="Transformers">
           <type>Anime, Science Fiction</type>
           <description>A schientific fiction</description>
        </movie>
        <movie title="Trigun">
           <type>Anime, Action</type>
           <description>Vash the Stampede!</description>
        </movie>
        <movie title="Ishtar">
           <type>Comedy</type>
           <description>Viewable boredom</description>
        </movie>
    </collection>
'''
root = ET.fromstring(data)
for s in root.findall("movie"):
        de = s.find("description")
        print("%s: %s" % (s.get("title"), de.text))
