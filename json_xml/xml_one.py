# !/usr/bin/env python
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
import xml.sax
__author__ = 'Max_Pengjb'

"""
SAX库

SAX是一种基于事件驱动的API，使用SAX解析XML时主要分两个部分：解析器和事件处理器。
解析器

解析器负责读取XML文档，并向事件处理器发送事件，比如元素开始跟元素结束事件。
SAX提供了两个函数：parse和parseString。前者用于从文件中解析XML数据，后者用于从字符串中解析XML数据。

两个函数的声明如下：

    xml.sax.parse( xmlfile, contenthandler)
    xml.sax.parseString(xmlstring, contenthandler)

parse函数的第一个参数是XML文件的路径，比如:

    xml.sax.parse("test.xml",contenthandler)

parseString函数的第一个参数是含有XML数据的字符串，比如：

    data = "<data>Hello</data>"
    xml.sax.parseString(data,contenthandler)

而它们的第二个参数则是接下来要介绍的事件处理器。
事件处理器

事件处理器则负责对事件作出响应，对传递的XML数据进行处理。
一个事件处理器必须是ContentHandler类型的子类，通过重写父类的以下函数来响应解析器的事件请求：

    characters(content)函数，它会在以下时机被调用：
        如果从一行开始，遇到标签之前，存在字符，则content的值为这些字符串。
        如果从一个标签，遇到下一个标签之前，存在字符，则content的值为这些字符串。
        如果从一个标签，遇到行结束符（换行符）之前，存在字符，则content的值为这些字符串。
        标签可以是开始标签，也可以是结束标签。

    startDocument()函数，它在文档启动的时候调用。
    endDocument()函数，它在解析器到达文档结尾时调用。
    startElement(name, attrs)函数，它在遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。
    endElement(name)函数，它在遇到XML结束标签时调用。

假设有如下文件test.xml：

    <data>文字1
    文字2<ele1>元素1数据</ele1>文字3
    文字4<ele2>元素2数据</ele2>文字5
    </data>

当运行以下代码时：

    import xml.sax
    class Handler(xml.sax.ContentHandler):
        def startDocument(self):
            print("文档开始")
        def endDocument(self):
            print("文档结束")
        def startElement(self,name,attrs):
            print("开始标签：" , name)
        def endElement(self,name):
            print("结束标签：" , name)
        def characters(self,content):
            print("数据：" ,content)
    if __name__ == '__main__':
        xml.sax.parse("test.xml",Handler())

会得到以下结果：
文档开始
开始标签： data
数据： 文字1
数据：<换行>
数据： 文字2
开始标签： ele1
数据： 元素1数据
结束标签： ele1
数据： 文字3
数据：<换行>
数据： 文字4
开始标签： ele2
数据： 元素2数据
结束标签： ele2
数据： 文字5
数据：<换行>
结束标签： data
文档结束
注意：结果中的<换行>其实是换行字符\n，为了方便阅读才改成<换行>。

将其与test.xml中数据的结构对比一下，就可以明白每个函数调用的时机了。
"""


class Handler(xml.sax.ContentHandler):
    def startDocument(self):
        print("文档开始")

    def endDocument(self):
        print("文档结束")

    def startElement(self, name, attrs):
        print("开始标签：", name)

    def endElement(self, name):
        print("结束标签：", name)

    def characters(self, content):
        print("数据：", content)


test_xml = '''  
<data>文字1
文字2<ele1>元素1数据</ele1>文字3
文字4<ele2>元素2数据</ele2>文字5
</data>'''
xml.sax.parseString(test_xml, Handler())
