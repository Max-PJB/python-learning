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
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
#
# # Create a new chat bot named Charlie
# chinese_bot = ChatBot('Charlie',
#                       storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
#                       logic_adapters=[
#                           'chatterbot.logic.BestMatch'
#                       ],
#                       database_uri='mongodb://localhost:27017/chatterbot-database'
#                       )
#
# trainer = ListTrainer(chinese_bot)
#
# trainer.train([
#     "为中文自然语言处理领域发展贡献语料",
#     "贡献中文语料，请联系",
#     "语料库将会不断扩充",
#     "一期目标",
#     "个百万级中文语料",
#     "个千万级中文语料",
#     "二期目标",
#     "个百万级中文语料 ",
#     "个千万级中文语料",
#     "个亿级中文语料",
#     "为什么需要这个项目",
#     "中文的信息无处不在，但如果想要获得大量的中文语料，却是不太容易，有时甚至非常困难。在2019年初这个时点上",
#     "普通的从业者、研究人员或学生，并没有一个比较好的渠道获得极大量的中文语料。笔者想要训练一个中文的词向量，",
#     "在百度和github上上搜索了好久，收获却很少：要么语料的量级太小，要么数据过于成旧，或需要的处理太复杂。",
#     "不知道你是否也遇到了这样的问题？",
#     "我们这个项目，就是为了解决这一问题贡献微薄之力。",
# ])

# Get a response to the input text 'I would like to book a flight.'
# response = chinese_bot.get_response('I would like to book a flight.')

# print(response)

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origin": "*"}})


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return "haha"


@app.route("/member/checkLogin")
def check_login():
    print("haha")
    return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572179265312,
                    "result": {"id": None, "username": None, "phone": None, "email": None, "sex": None, "address": None,
                               "file": None, "description": None, "points": None, "balance": None, "state": 0,
                               "token": None,
                               "message": "用户登录已过期"}})


@app.route("/goods/home")
def home():
    # 轮播图：2240 x 1108
    return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572182342709, "result": [
        {"id": 7, "name": "轮播图", "type": 0, "sortOrder": 0, "position": 0, "limitNum": 5, "status": 1, "remark": "",
         "created": 1523766787000, "updated": 1523766787000, "panelContents": [
            {"id": 70, "panelId": 7, "type": 0, "productId": 150635087972564, "sortOrder": 1, "fullUrl": "",
             "picUrl": "https://api.ai2hit.com/static/upload/201910302141432598.png",
             "picUrl2": "",
             "picUrl3": "", "created": 1569839898000,
             "updated": 1569843454000, "salePrice": 1.00, "productName": "支付测试商品 IPhone X 全面屏 全面绽放",
             "subTitle": "此仅为支付测试商品 拍下不会发货", "productImageBig": "https://i.loli.net/2019/09/30/CAZ6QrXPBoh5aIT.png"},
            {"id": 33, "panelId": 7, "type": 0, "productId": 150642571432835, "sortOrder": 2, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/4921019f885a28b0c1f8161646dfc395.png?x-oss-process=image/format,jpg/quality,Q_100",
             "picUrl2": "",
             "picUrl3": "", "created": 1523970502000,
             "updated": 1524192439000, "salePrice": 1.00, "productName": "捐赠商品", "subTitle": "您的捐赠将用于本站维护 给您带来更好的体验",
             "productImageBig": "https://i.loli.net/2018/11/04/5bdeba4028e90.png"},
            {"id": 34, "panelId": 7, "type": 0, "productId": 150635087972564, "sortOrder": 3, "fullUrl": None,
             "picUrl": "https://api.ai2hit.com/static/upload/201910302157356025.jpg", "picUrl2": "", "picUrl3": "",
             "created": 1523970510000, "updated": 1523970512000, "salePrice": 1.00,
             "productName": "支付测试商品 IPhone X 全面屏 全面绽放", "subTitle": "此仅为支付测试商品 拍下不会发货",
             "productImageBig": "https://s1.ax1x.com/2018/05/19/Ccdiid.png"}]},
        {"id": 8, "name": "活动版块", "type": 1, "sortOrder": 1, "position": 0, "limitNum": 4, "status": 1, "remark": "",
         "created": 1523790300000, "updated": 1523790300000, "panelContents": [
            {"id": 25, "panelId": 8, "type": 0, "productId": 150642571432835, "sortOrder": 1,
             "fullUrl": "https://www.smartisan.com/jianguo3-accessories",
             "picUrl": "https://resource.smartisan.com/resource/6/610400xinpinpeijian.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1523790463000, "updated": 1524151234000, "salePrice": 1.00,
             "productName": "捐赠商品", "subTitle": "您的捐赠将用于本站维护 给您带来更好的体验",
             "productImageBig": "https://resource.smartisan.com/resource/6/610400xinpinpeijian.jpg"},
            {"id": 26, "panelId": 8, "type": 0, "productId": 150635087972564, "sortOrder": 2,
             "fullUrl": "https://www.smartisan.com/service/#/tradein",
             "picUrl": "https://resource.smartisan.com/resource/6/610400yijiuhuanxin.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1523790480000, "updated": 1524151248000, "salePrice": 1.00,
             "productName": "支付测试商品 IPhone X 全面屏 全面绽放", "subTitle": "此仅为支付测试商品 拍下不会发货",
             "productImageBig": "https://resource.smartisan.com/resource/6/610400yijiuhuanxin.jpg"},
            {"id": 27, "panelId": 8, "type": 0, "productId": 150642571432835, "sortOrder": 3,
             "fullUrl": "https://www.smartisan.com/category?id=69",
             "picUrl": "https://resource.smartisan.com/resource/4/489673079577637073.png", "picUrl2": None,
             "picUrl3": None, "created": 1523790504000, "updated": 1524151261000, "salePrice": 1.00,
             "productName": "捐赠商品", "subTitle": "您的捐赠将用于本站维护 给您带来更好的体验",
             "productImageBig": "https://resource.smartisan.com/resource/4/489673079577637073.png"},
            {"id": 28, "panelId": 8, "type": 0, "productId": 150635087972564, "sortOrder": 4,
             "fullUrl": "https://www.smartisan.com/",
             "picUrl": "https://resource.smartisan.com/resource/fe6ab43348a43152b4001b4454d206ac.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1523790538000, "updated": 1524151273000, "salePrice": 1.00,
             "productName": "支付测试商品 IPhone X 全面屏 全面绽放", "subTitle": "此仅为支付测试商品 拍下不会发货",
             "productImageBig": "https://resource.smartisan.com/resource/fe6ab43348a43152b4001b4454d206ac.jpg"}]},
        {"id": 1, "name": "热门商品", "type": 2, "sortOrder": 2, "position": 0, "limitNum": 3, "status": 1, "remark": "",
         "created": 1524066553000, "updated": 1523790316000, "panelContents": [
            {"id": 22, "panelId": 1, "type": 0, "productId": 150635087972564, "sortOrder": 1, "fullUrl": None,
             "picUrl": "https://i.loli.net/2018/07/13/5b48a7f468bf2.png", "picUrl2": None, "picUrl3": None,
             "created": 1508682391000, "updated": 1508682391000, "salePrice": 1.00,
             "productName": "支付测试商品 IPhone X 全面屏 全面绽放", "subTitle": "此仅为支付测试商品 拍下不会发货",
             "productImageBig": "https://i.loli.net/2018/07/13/5b48a7f468bf2.png"},
            {"id": 23, "panelId": 1, "type": 0, "productId": 150642571432835, "sortOrder": 2, "fullUrl": "",
             "picUrl": "https://i.loli.net/2018/07/13/5b48a7f46be51.png", "picUrl2": None, "picUrl3": None,
             "created": 1508682400000, "updated": 1523969975000, "salePrice": 1.00, "productName": "捐赠商品",
             "subTitle": "您的捐赠将用于本站维护 给您带来更好的体验",
             "productImageBig": "https://i.loli.net/2018/07/13/5b48a7f46be51.png"}]},
        {"id": 2, "name": "官方精选", "type": 3, "sortOrder": 3, "position": 0, "limitNum": 8, "status": 1, "remark": "",
         "created": None, "updated": 1524108059000, "panelContents": [
            {"id": 29, "panelId": 2, "type": 2, "productId": 150642571432843, "sortOrder": 0, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/1/1220858shoujilouceng.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1523794475000, "updated": 1524195687000, "salePrice": 1999.00,
             "productName": "坚果 3", "subTitle": "漂亮得不像实力派",
             "productImageBig": "https://resource.smartisan.com/resource/1/1220858shoujilouceng.jpg"},
            {"id": 8, "panelId": 2, "type": 0, "productId": 150642571432837, "sortOrder": 1, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/3a7522290397a9444d7355298248f197.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1506330228000, "updated": 1524151406000, "salePrice": 49.00,
             "productName": "坚果 3 前屏钢化玻璃保护膜", "subTitle": "超强透光率、耐刮花、防指纹",
             "productImageBig": "https://resource.smartisan.com/resource/3a7522290397a9444d7355298248f197.jpg"},
            {"id": 9, "panelId": 2, "type": 0, "productId": 150642571432838, "sortOrder": 2, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/63ea40e5c64db1c6b1d480c48fe01272.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1506330275000, "updated": 1524192497000, "salePrice": 79.00,
             "productName": "坚果 3 绒布国旗保护套", "subTitle": "质感精良、完美贴合、周到防护",
             "productImageBig": "https://resource.smartisan.com/resource/63ea40e5c64db1c6b1d480c48fe01272.jpg"},
            {"id": 14, "panelId": 2, "type": 0, "productId": 150642571432839, "sortOrder": 3, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/5e4b1feddb13639550849f12f6b2e202.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1508681641000, "updated": 1524192509000, "salePrice": 29.00,
             "productName": "坚果 3 TPU 软胶透明保护套", "subTitle": "轻薄透明、完美贴合、TPU 环保材质",
             "productImageBig": "https://resource.smartisan.com/resource/5e4b1feddb13639550849f12f6b2e202.jpg"},
            {"id": 15, "panelId": 2, "type": 0, "productId": 150642571432840, "sortOrder": 4, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/10525c4b21f039fc8ccb42cd1586f5cd.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1508681692000, "updated": 1524192523000, "salePrice": 89.00,
             "productName": "Smartisan 半入耳式耳机", "subTitle": "经典配色、专业调音、高品质麦克风",
             "productImageBig": "https://resource.smartisan.com/resource/10525c4b21f039fc8ccb42cd1586f5cd.jpg"},
            {"id": 16, "panelId": 2, "type": 0, "productId": 150642571432841, "sortOrder": 5, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/b899d9b82c4bc2710492a26af021d484.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1508681751000, "updated": 1524192542000, "salePrice": 49.00,
             "productName": "坚果 3 TPU 软胶保护套", "subTitle": "TPU 环保材质、完美贴合、周到防护",
             "productImageBig": "https://resource.smartisan.com/resource/b899d9b82c4bc2710492a26af021d484.jpg"},
            {"id": 17, "panelId": 2, "type": 0, "productId": 150642571432842, "sortOrder": 6, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/abb6986430536cd9365352b434f3c568.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1508681821000, "updated": 1524192557000, "salePrice": 79.00,
             "productName": "坚果 3 \"足迹\"背贴 乐高创始人出生", "subTitle": "1891 年 4 月 7 日",
             "productImageBig": "https://resource.smartisan.com/resource/abb6986430536cd9365352b434f3c568.jpg"}]},
        {"id": 10, "name": "品牌周边", "type": 3, "sortOrder": 4, "position": 0, "limitNum": 7, "status": 1, "remark": None,
         "created": 1524066632000, "updated": 1524066635000, "panelContents": [
            {"id": 40, "panelId": 10, "type": 3, "productId": None, "sortOrder": 0,
             "fullUrl": "http://xmall.exrick.cn/#/goods?cid=1184",
             "picUrl": "https://resource.smartisan.com/resource/z/zhoubianshangpin1220858web.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1524067373000, "updated": 1524194159000, "salePrice": None,
             "productName": None, "subTitle": None,
             "productImageBig": "https://resource.smartisan.com/resource/z/zhoubianshangpin1220858web.jpg"},
            {"id": 41, "panelId": 10, "type": 0, "productId": 150642571432845, "sortOrder": 1, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/2f9a0f5f3dedf0ed813622003f1b287b.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1524067376000, "updated": 1524155076000, "salePrice": 199.00,
             "productName": "Smartisan 帆布鞋", "subTitle": "一双踏实、舒适的帆布鞋",
             "productImageBig": "https://resource.smartisan.com/resource/2f9a0f5f3dedf0ed813622003f1b287b.jpg"},
            {"id": 42, "panelId": 10, "type": 0, "productId": 150642571432836, "sortOrder": 2, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/2b05dbca9f5a4d0c1270123f42fb834c.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1524067380000, "updated": 1524155101000, "salePrice": 149.00,
             "productName": "Smartisan T恤 伍迪·艾伦出生", "subTitle": "一件内外兼修的舒适T恤",
             "productImageBig": "https://resource.smartisan.com/resource/2b05dbca9f5a4d0c1270123f42fb834c.jpg"},
            {"id": 43, "panelId": 10, "type": 0, "productId": 150642571432846, "sortOrder": 3, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/804edf579887b3e1fae4e20a379be5b5.png", "picUrl2": None,
             "picUrl3": None, "created": 1524067384000, "updated": 1524155117000, "salePrice": 149.00,
             "productName": "Smartisan T恤 任天堂发售“红白机”", "subTitle": "100% 美国 SUPIMA 棉、舒适拉绒质地",
             "productImageBig": "https://resource.smartisan.com/resource/804edf579887b3e1fae4e20a379be5b5.png"},
            {"id": 44, "panelId": 10, "type": 0, "productId": 150642571432848, "sortOrder": 4, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/a1c53b5f12dd7ef790cadec0eaeaf466.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1524067390000, "updated": 1524192952000, "salePrice": 199.00,
             "productName": "Smartisan 牛津纺衬衫", "subTitle": "一件无拘无束的舒适衬衫",
             "productImageBig": "https://resource.smartisan.com/resource/a1c53b5f12dd7ef790cadec0eaeaf466.jpg"},
            {"id": 45, "panelId": 10, "type": 0, "productId": 150642571432847, "sortOrder": 5, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/daa975651d6d700c0f886718c520ee19.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1524067395000, "updated": 1524192896000, "salePrice": 249.00,
             "productName": "Smartisan Polo衫 经典款", "subTitle": "一件表里如一的舒适 POLO 衫",
             "productImageBig": "https://resource.smartisan.com/resource/daa975651d6d700c0f886718c520ee19.jpg"},
            {"id": 46, "panelId": 10, "type": 0, "productId": 150642571432849, "sortOrder": 6, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/3973d009d182d8023bea6250b9a3959e.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1524067400000, "updated": 1524192903000, "salePrice": 9.90,
             "productName": "Smartisan 明信片", "subTitle": "优质卡纸、包装精致、色彩饱满",
             "productImageBig": "https://resource.smartisan.com/resource/3973d009d182d8023bea6250b9a3959e.jpg"}]},
        {"id": 3, "name": "品牌精选", "type": 3, "sortOrder": 5, "position": 0, "limitNum": 7, "status": 1, "remark": "",
         "created": 1524066559000, "updated": 1523962455000, "panelContents": [
            {"id": 30, "panelId": 3, "type": 2, "productId": 150642571432850, "sortOrder": 0, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/a/acillouceng1220856.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1523794518000, "updated": 1524194283000, "salePrice": 199.00,
             "productName": "ACIL E1 颈挂式蓝牙耳机", "subTitle": "无感佩戴，一切变得简单",
             "productImageBig": "https://resource.smartisan.com/resource/a/acillouceng1220856.jpg"},
            {"id": 2, "panelId": 3, "type": 0, "productId": 150642571432851, "sortOrder": 1, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/7ac3af5a92ad791c2b38bfe1e38ee334.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1506096182000, "updated": 1524155020000, "salePrice": 2699.00,
             "productName": "优点智能 E1 推拉式智能指纹密码锁", "subTitle": "推拉一下，轻松开关",
             "productImageBig": "https://resource.smartisan.com/resource/7ac3af5a92ad791c2b38bfe1e38ee334.jpg"},
            {"id": 7, "panelId": 3, "type": 0, "productId": 816448, "sortOrder": 2, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/41cb562a47d4831e199ed7e2057f3b61.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1506178691000, "updated": 1524154469000, "salePrice": 2799.00,
             "productName": "极米无屏电视 CC", "subTitle": "720P 高清分辨率、JBL 音响、两万毫安续航力",
             "productImageBig": "https://resource.smartisan.com/resource/41cb562a47d4831e199ed7e2057f3b61.jpg"},
            {"id": 18, "panelId": 3, "type": 0, "productId": 847276, "sortOrder": 3, "fullUrl": None,
             "picUrl": "https://resource.smartisan.com/resource/99c548bfc9848a8c95f4e4f7f2bc1095.png", "picUrl2": None,
             "picUrl3": None, "created": 1508682172000, "updated": 1508682172000, "salePrice": 1499.00,
             "productName": "FIIL Diva Pro 全场景无线降噪耳机", "subTitle": "智能语音交互、高清无损本地存储播放",
             "productImageBig": "https://resource.smartisan.com/resource/99c548bfc9848a8c95f4e4f7f2bc1095.png"},
            {"id": 19, "panelId": 3, "type": 0, "productId": 150642571432844, "sortOrder": 4, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/71432ad30288fb860a4389881069b874.png", "picUrl2": None,
             "picUrl3": None, "created": 1508682215000, "updated": 1524194738000, "salePrice": 2999.00,
             "productName": "畅呼吸智能空气净化器超级除甲醛版", "subTitle": "购新空净 赠价值 699 元活性炭滤芯",
             "productImageBig": "https://resource.smartisan.com/resource/71432ad30288fb860a4389881069b874.png"},
            {"id": 20, "panelId": 3, "type": 0, "productId": 847276, "sortOrder": 5, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/804b82e4c05516e822667a23ee311f7c.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1508682294000, "updated": 1524154503000, "salePrice": 1499.00,
             "productName": "FIIL Diva Pro 全场景无线降噪耳机", "subTitle": "智能语音交互、高清无损本地存储播放",
             "productImageBig": "https://resource.smartisan.com/resource/804b82e4c05516e822667a23ee311f7c.jpg"},
            {"id": 21, "panelId": 3, "type": 0, "productId": 150642571432852, "sortOrder": 6, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/367d93db1d58f9f3505bc0ec18efaa44.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1508682328000, "updated": 1524155051000, "salePrice": 499.00,
             "productName": "FIIL Driifter 脖挂蓝牙耳机", "subTitle": "全天佩戴 抬手就听 HEAC稳连技术",
             "productImageBig": "https://resource.smartisan.com/resource/367d93db1d58f9f3505bc0ec18efaa44.jpg"}]},
        {"id": 9, "name": "活动版块2", "type": 1, "sortOrder": 7, "position": 0, "limitNum": 4, "status": 1, "remark": "",
         "created": None, "updated": 1524110267000, "panelContents": [
            {"id": 65, "panelId": 9, "type": 0, "productId": 150635087972564, "sortOrder": 1, "fullUrl": "",
             "picUrl": "https://resource.smartisan.com/resource/f82c9e2774ce0e391a17f1b20c1e0c90.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1554871004000, "updated": 1554871004000, "salePrice": 1.00,
             "productName": "支付测试商品 IPhone X 全面屏 全面绽放", "subTitle": "此仅为支付测试商品 拍下不会发货",
             "productImageBig": "https://resource.smartisan.com/resource/f82c9e2774ce0e391a17f1b20c1e0c90.jpg"},
            {"id": 37, "panelId": 9, "type": 0, "productId": 150642571432835, "sortOrder": 2,
             "fullUrl": "https://www.smartisan.com/os/#/4-x",
             "picUrl": "https://resource.smartisan.com/resource/5ea6f0905535d7b11258e9a0f9b1abeb.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1524066711000, "updated": 1524196999000, "salePrice": 1.00,
             "productName": "捐赠商品", "subTitle": "您的捐赠将用于本站维护 给您带来更好的体验",
             "productImageBig": "https://resource.smartisan.com/resource/5ea6f0905535d7b11258e9a0f9b1abeb.jpg"},
            {"id": 38, "panelId": 9, "type": 0, "productId": 150635087972564, "sortOrder": 3,
             "fullUrl": "https://www.smartisan.com/pr/#/video/changhuxi-jinghuaqi",
             "picUrl": "https://resource.smartisan.com/resource/c245ada282824a4a15e68bec80502ad4.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1524066718000, "updated": 1524197011000, "salePrice": 1.00,
             "productName": "支付测试商品 IPhone X 全面屏 全面绽放", "subTitle": "此仅为支付测试商品 拍下不会发货",
             "productImageBig": "https://resource.smartisan.com/resource/c245ada282824a4a15e68bec80502ad4.jpg"},
            {"id": 39, "panelId": 9, "type": 0, "productId": 150642571432835, "sortOrder": 4,
             "fullUrl": "https://www.smartisan.com/pr/#/video/onestep-introduction",
             "picUrl": "https://resource.smartisan.com/resource/m/minibanner_03.jpg", "picUrl2": None, "picUrl3": None,
             "created": 1524066722000, "updated": 1524197021000, "salePrice": 1.00, "productName": "捐赠商品",
             "subTitle": "您的捐赠将用于本站维护 给您带来更好的体验",
             "productImageBig": "https://resource.smartisan.com/resource/m/minibanner_03.jpg"}]}]})


@app.route("/goods/navList")
def nav_list():
    return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572182342706, "result": [
        {"id": 67, "panelId": 0, "type": 1, "productId": None, "sortOrder": 1,
         "fullUrl": "http://xmall.exrick.cn/#/goods?cid=1184", "picUrl": "健康监测", "picUrl2": None, "picUrl3": None,
         "created": 1569839447000, "updated": 1569839447000, "salePrice": None, "productName": None, "subTitle": None,
         "productImageBig": "健康监测"},
        {"id": 58, "panelId": 0, "type": 1, "productId": None, "sortOrder": 2,
         "fullUrl": "http://xmall.exrick.cn/#/thanks", "picUrl": "健康食品", "picUrl2": None,
         "picUrl3": None, "created": 1532695807000, "updated": 1532701518000,
         "salePrice": None, "productName": None, "subTitle": None,
         "productImageBig": "健康食品"},
        {"id": 59, "panelId": 0, "type": 0, "productId": None, "sortOrder": 3, "fullUrl": "http://xmadmin.exrick.cn",
         "picUrl": "健康用品", "picUrl2": None, "picUrl3": None, "created": 1532701544000, "updated": 1532701614000,
         "salePrice": None, "productName": None, "subTitle": None, "productImageBig": "健康用品"},
        {"id": 68, "panelId": 0, "type": 0, "productId": None, "sortOrder": 4, "fullUrl": "http://xpay.exrick.cn",
         "picUrl": "体育用品", "picUrl2": None, "picUrl3": None, "created": 1569839494000, "updated": 1569839494000,
         "salePrice": None, "productName": None, "subTitle": None, "productImageBig": "体育用品"},
        {"id": 61, "panelId": 0, "type": 0, "productId": None, "sortOrder": 5,
         "fullUrl": "https://github.com/Exrick/x-boot", "picUrl": "健康服务", "picUrl2": None, "picUrl3": None,
         "created": 1532701581000, "updated": 1541324408000, "salePrice": None, "productName": None, "subTitle": None,
         "productImageBig": "健康服务"}
    ]})


# /goods/allGoods?page=1&size=20&sort=&priceGt=&priceLte=
# 这里要做一个分页，接受参数，然后返回分页后的结果
@app.route("/goods/allGoods")
def all_goods():
    return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572446419191,
                    "result": {"total": 32, "data": [
                        {"productId": 150642571432852, "salePrice": 499.00, "productName": "FIIL Driifter 脖挂蓝牙耳机",
                         "subTitle": "全天佩戴 抬手就听 HEAC稳连技术",
                         "productImageBig": "https://resource.smartisan.com/resource/367d93db1d58f9f3505bc0ec18efaa44.jpg"},
                        {"productId": 150642571432851, "salePrice": 2699.00, "productName": "优点智能 E1 推拉式智能指纹密码锁",
                         "subTitle": "推拉一下，轻松开关",
                         "productImageBig": "https://resource.smartisan.com/resource/7ac3af5a92ad791c2b38bfe1e38ee334.jpg"},
                        {"productId": 150642571432850, "salePrice": 199.00, "productName": "ACIL E1 颈挂式蓝牙耳机",
                         "subTitle": "无感佩戴，一切变得简单",
                         "productImageBig": "https://resource.smartisan.com/resource/406eddef8808fa5a9be9594d07ef8643.jpg"},
                        {"productId": 150642571432849, "salePrice": 9.90, "productName": "Smartisan 明信片",
                         "subTitle": "优质卡纸、包装精致、色彩饱满",
                         "productImageBig": "https://resource.smartisan.com/resource/3973d009d182d8023bea6250b9a3959e.jpg"},
                        {"productId": 150642571432848, "salePrice": 199.00, "productName": "Smartisan 牛津纺衬衫",
                         "subTitle": "一件无拘无束的舒适衬衫",
                         "productImageBig": "https://resource.smartisan.com/resource/a1c53b5f12dd7ef790cadec0eaeaf466.jpg"},
                        {"productId": 150642571432847, "salePrice": 249.00, "productName": "Smartisan Polo衫 经典款",
                         "subTitle": "一件表里如一的舒适 POLO 衫",
                         "productImageBig": "https://resource.smartisan.com/resource/daa975651d6d700c0f886718c520ee19.jpg"},
                        {"productId": 150642571432846, "salePrice": 149.00, "productName": "Smartisan T恤 任天堂发售“红白机”",
                         "subTitle": "100% 美国 SUPIMA 棉、舒适拉绒质地",
                         "productImageBig": "https://resource.smartisan.com/resource/804edf579887b3e1fae4e20a379be5b5.png"},
                        {"productId": 150642571432845, "salePrice": 199.00, "productName": "Smartisan 帆布鞋",
                         "subTitle": "一双踏实、舒适的帆布鞋",
                         "productImageBig": "https://resource.smartisan.com/resource/2f9a0f5f3dedf0ed813622003f1b287b.jpg"},
                        {"productId": 150642571432844, "salePrice": 2999.00, "productName": "畅呼吸智能空气净化器超级除甲醛版",
                         "subTitle": "购新空净 赠价值 699 元活性炭滤芯",
                         "productImageBig": "https://resource.smartisan.com/resource/71432ad30288fb860a4389881069b874.png"},
                        {"productId": 150642571432843, "salePrice": 1999.00, "productName": "坚果 3",
                         "subTitle": "漂亮得不像实力派",
                         "productImageBig": "https://resource.smartisan.com/resource/718bcecced0df1cd23bbdb9cc1f70b7d.png"},
                        {"productId": 150642571432842, "salePrice": 79.00, "productName": "坚果 3 \"足迹\"背贴 乐高创始人出生",
                         "subTitle": "1891 年 4 月 7 日",
                         "productImageBig": "https://resource.smartisan.com/resource/abb6986430536cd9365352b434f3c568.jpg"},
                        {"productId": 150642571432841, "salePrice": 49.00, "productName": "坚果 3 TPU 软胶保护套",
                         "subTitle": "TPU 环保材质、完美贴合、周到防护",
                         "productImageBig": "https://resource.smartisan.com/resource/b899d9b82c4bc2710492a26af021d484.jpg"},
                        {"productId": 150642571432840, "salePrice": 89.00, "productName": "Smartisan 半入耳式耳机",
                         "subTitle": "经典配色、专业调音、高品质麦克风",
                         "productImageBig": "https://resource.smartisan.com/resource/9c1d958f10a811df841298d50e1ca7c0.jpg"},
                        {"productId": 150642571432839, "salePrice": 29.00, "productName": "坚果 3 TPU 软胶透明保护套",
                         "subTitle": "轻薄透明、完美贴合、TPU 环保材质",
                         "productImageBig": "https://resource.smartisan.com/resource/5e4b1feddb13639550849f12f6b2e202.jpg"},
                        {"productId": 150642571432838, "salePrice": 79.00, "productName": "坚果 3 绒布国旗保护套",
                         "subTitle": "质感精良、完美贴合、周到防护",
                         "productImageBig": "https://resource.smartisan.com/resource/63ea40e5c64db1c6b1d480c48fe01272.jpg"},
                        {"productId": 150642571432837, "salePrice": 49.00, "productName": "坚果 3 前屏钢化玻璃保护膜",
                         "subTitle": "超强透光率、耐刮花、防指纹",
                         "productImageBig": "https://resource.smartisan.com/resource/3a7522290397a9444d7355298248f197.jpg"},
                        {"productId": 150642571432836, "salePrice": 149.00, "productName": "Smartisan T恤 伍迪·艾伦出生",
                         "subTitle": "一件内外兼修的舒适T恤",
                         "productImageBig": "https://resource.smartisan.com/resource/f96f0879768bc317b74e7cf9e3d96884.jpg"},
                        {"productId": 816448, "salePrice": 2799.00, "productName": "极米无屏电视 CC",
                         "subTitle": "720P 高清分辨率、JBL 音响、两万毫安续航力",
                         "productImageBig": "http://image.smartisanos.cn/resource/41cb562a47d4831e199ed7e2057f3b61.jpg"},
                        {"productId": 738388, "salePrice": 39.00, "productName": "Smartisan 原装 Type-C 数据线",
                         "subTitle": "PTC 过温保护、凹形设计、TPE 环保材质",
                         "productImageBig": "http://image.smartisanos.cn/resource/c79a73ffc6f8e782160d978f49f543dc.jpg"},
                        {"productId": 691300, "salePrice": 199.00, "productName": "Smartisan 快充移动电源 10000mAh",
                         "subTitle": "10000mAh 双向快充、轻盈便携、高标准安全保护",
                         "productImageBig": "http://image.smartisanos.cn/resource/0540778097a009364f2dcbb8c5286451.jpg"}]}})


if __name__ == "__main__":
    app.run()
