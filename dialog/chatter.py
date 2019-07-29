#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @   package ：      
    @   Author  :       Max_PengJB
    @   date    :       2019-7-29 18:07
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    
-------------------------------------------------
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chinese_bot = ChatBot('Charlie',
                      storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
                      logic_adapters=[
                          'chatterbot.logic.BestMatch'
                      ],
                      database_uri='mongodb://localhost:27017/chatterbot-database'
                      )

trainer = ListTrainer(chinese_bot)

trainer.train([
    "为中文自然语言处理领域发展贡献语料",
    "贡献中文语料，请联系",
    "语料库将会不断扩充",
    "一期目标",
    "个百万级中文语料",
    "个千万级中文语料",
    "二期目标",
    "个百万级中文语料 ",
    "个千万级中文语料",
    "个亿级中文语料",
    "为什么需要这个项目",
    "中文的信息无处不在，但如果想要获得大量的中文语料，却是不太容易，有时甚至非常困难。在2019年初这个时点上",
    "普通的从业者、研究人员或学生，并没有一个比较好的渠道获得极大量的中文语料。笔者想要训练一个中文的词向量，",
    "在百度和github上上搜索了好久，收获却很少：要么语料的量级太小，要么数据过于成旧，或需要的处理太复杂。",
    "不知道你是否也遇到了这样的问题？",
    "我们这个项目，就是为了解决这一问题贡献微薄之力。",
])

# Get a response to the input text 'I would like to book a flight.'
response = chinese_bot.get_response('I would like to book a flight.')

print(response)

from flask import Flask, request

app = Flask(__name__)


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chinese_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
