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

# 别人的数据库设计文件
# https://macrozheng.github.io/mall-learning/#/database/mall_database_overview
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
             "picUrl": "https://img12.360buyimg.com/cms/jfs/t1/18904/30/10423/567680/5c87148dE406015ca/a4b15b221755ccf1.jpg",
             "picUrl2": "", "picUrl3": "",
             "created": 1523970510000, "updated": 1523970512000, "salePrice": 1.00,
             "productName": "支付测试商品 IPhone X 全面屏 全面绽放", "subTitle": "此仅为支付测试商品 拍下不会发货",
             "productImageBig": "https://img12.360buyimg.com/cms/jfs/t1/18904/30/10423/567680/5c87148dE406015ca/a4b15b221755ccf1.jpg"}]},
        {"id": 8, "name": "活动版块", "type": 1, "sortOrder": 1, "position": 0, "limitNum": 4, "status": 1, "remark": "",
         "created": 1523790300000, "updated": 1523790300000, "panelContents": [
            {"id": 25, "panelId": 8, "type": 0, "productId": 150642571432835, "sortOrder": 1,
             "fullUrl": "https://www.smartisan.com/jianguo3-accessories",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092059359158.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1523790463000, "updated": 1524151234000, "salePrice": 1.00,
             "productName": "捐赠商品", "subTitle": "您的捐赠将用于本站维护 给您带来更好的体验",
             "productImageBig": "https://resource.smartisan.com/resource/6/610400xinpinpeijian.jpg"},
            {"id": 26, "panelId": 8, "type": 0, "productId": 150635087972564, "sortOrder": 2,
             "fullUrl": "https://www.smartisan.com/service/#/tradein",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092100205673.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1523790480000, "updated": 1524151248000, "salePrice": 1.00,
             "productName": "支付测试商品 IPhone X 全面屏 全面绽放", "subTitle": "此仅为支付测试商品 拍下不会发货",
             "productImageBig": "https://resource.smartisan.com/resource/6/610400yijiuhuanxin.jpg"},
            {"id": 27, "panelId": 8, "type": 0, "productId": 150642571432835, "sortOrder": 3,
             "fullUrl": "https://www.smartisan.com/category?id=69",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092101076456.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1523790504000, "updated": 1524151261000, "salePrice": 1.00,
             "productName": "捐赠商品", "subTitle": "您的捐赠将用于本站维护 给您带来更好的体验",
             "productImageBig": "https://resource.smartisan.com/resource/4/489673079577637073.png"},
            {"id": 28, "panelId": 8, "type": 0, "productId": 150635087972564, "sortOrder": 4,
             "fullUrl": "https://www.smartisan.com/",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092100205673.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1523790538000, "updated": 1524151273000, "salePrice": 1.00,
             "productName": "支付测试商品 IPhone X 全面屏 全面绽放", "subTitle": "此仅为支付测试商品 拍下不会发货",
             "productImageBig": "https://resource.smartisan.com/resource/fe6ab43348a43152b4001b4454d206ac.jpg"}]},

        {"id": 1, "name": "热门商品", "type": 2, "sortOrder": 2, "position": 0, "limitNum": 3, "status": 1, "remark": "",
         "created": 1524066553000, "updated": 1523790316000, "panelContents": [
            {"id": 22, "panelId": 1, "type": 0, "productId": 150642571432848321, "sortOrder": 1, "fullUrl": None,
             "picUrl": "https://api.ai2hit.com/static/upload/201911092052302994.png", "picUrl2": None, "picUrl3": None,
             "created": 1508682391000, "updated": 1508682391000, "salePrice": 1.00,
             "productName": "仁医师马油护手霜50ml", "subTitle": "防止肌肤干燥、保持双手滋润亮白的肌肤深层滋养马油乳木果护手霜",
             "productImageBig": "https://api.ai2hit.com/static/upload/201911092052302994.png"},
            {"id": 23, "panelId": 1, "type": 0, "productId": 150642571432835, "sortOrder": 2, "fullUrl": "",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092053116217.png", "picUrl2": None, "picUrl3": None,
             "created": 1508682400000, "updated": 1523969975000, "salePrice": 1.00, "productName": "仁医师马油酵素洗面霜100ml",
             "subTitle": "清洁毛孔 保湿不紧绷 添加酵素精华的马油酵素洗面霜",
             "productImageBig": "https://api.ai2hit.com/static/upload/201911092053116217.png"}]},

        {"id": 2, "name": "官方精选", "type": 3, "sortOrder": 3, "position": 0, "limitNum": 8, "status": 1, "remark": "",
         "created": None, "updated": 1524108059000, "panelContents": [
            {"id": 29, "panelId": 2, "type": 2, "productId": 15064257143284811, "sortOrder": 0, "fullUrl": "",
             "picUrl": "https://img11.360buyimg.com/n1/jfs/t26305/153/1540992424/242754/d3070cc9/5bed227aNba46b4d2.jpg",
             "picUrl2": None,
             "picUrl3": None, "created": 1523794475000, "updated": 1524195687000, "salePrice": 1999.00,
             "productName": "五谷扁粮饭", "subTitle": "生态五谷扁粮，家庭营养主食",
             "productImageBig": "https://img11.360buyimg.com/n1/jfs/t26305/153/1540992424/242754/d3070cc9/5bed227aNba46b4d2.jpg"},
            {"id": 8, "panelId": 2, "type": 0, "productId": 150642571432836333, "sortOrder": 1, "fullUrl": "",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092039474228.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1506330228000, "updated": 1524151406000, "salePrice": 49.00,
             "productName": "溯源码完美盏燕窝", "subTitle": "正规溯源码天然白燕盏印，尼孕纯净雨林，优等干燕窝",
             "productImageBig": "https://api.ai2hit.com/static/upload/201911092039474228.jpg"},
            {"id": 9, "panelId": 2, "type": 0, "productId": 150642571432836222, "sortOrder": 2, "fullUrl": "",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092038424695.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1506330275000, "updated": 1524192497000, "salePrice": 79.00,
             "productName": "仁师傅酵素梅", "subTitle": "採用特選大顆成熟的梅子，以低糖、低鹽，烘乾而成，淡淡梅香微甜不膩",
             "productImageBig": "https://api.ai2hit.com/static/upload/201911092038424695.jpg"},
            {"id": 14, "panelId": 2, "type": 0, "productId": 150642571432836123, "sortOrder": 3, "fullUrl": "",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092037487244.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1508681641000, "updated": 1524192509000, "salePrice": 29.00,
             "productName": "仁师傅旗鱼松（金枪鱼）", "subTitle": "严选上等新鲜黑旗鱼胸腹部位，含有丰富鱼肉纤维口感香酥带嚼勁，色泽金黄、入口即化",
             "productImageBig": "https://api.ai2hit.com/static/upload/201911092037487244.jpg"},
            {"id": 15, "panelId": 2, "type": 0, "productId": 150642571432840, "sortOrder": 4, "fullUrl": "",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092036038028.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1508681692000, "updated": 1524192523000, "salePrice": 89.00,
             "productName": "仁师傅眷村风味牛肉面", "subTitle": "细火慢炖汤头清新浓郁，令人回味无穷",
             "productImageBig": "https://api.ai2hit.com/static/upload/201911092036038028.jpg"},
            {"id": 16, "panelId": 2, "type": 0, "productId": 150642571432841, "sortOrder": 5, "fullUrl": "",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092033162363.png", "picUrl2": None,
             "picUrl3": None, "created": 1508681751000, "updated": 1524192542000, "salePrice": 49.00,
             "productName": "草本营养餐", "subTitle": "改变膳食结构，回归自然养生",
             "productImageBig": "https://api.ai2hit.com/static/upload/201911092033162363.png"},
            {"id": 17, "panelId": 2, "type": 0, "productId": 150642571432842444, "sortOrder": 6, "fullUrl": "",
             "picUrl": "https://api.ai2hit.com/static/upload/201911092040318000.jpg", "picUrl2": None,
             "picUrl3": None, "created": 1508681821000, "updated": 1524192557000, "salePrice": 79.00,
             "productName": "上等文山三七", "subTitle": "有机好三七，来自举世公认的最好的三七产地文山",
             "productImageBig": "https://api.ai2hit.com/static/upload/201911092040318000.jpg"}]}
    ]})


@app.route("/goods/navList")
def nav_list():
    return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572182342706, "result": [
        {"id": 67, "panelId": 0, "type": "健康检测", "productId": None, "sortOrder": 1,
         "fullUrl": "http://xmall.exrick.cn/#/goods?cid=1184", "picUrl": "健康检测", "picUrl2": None, "picUrl3": None,
         "created": 1569839447000, "updated": 1569839447000, "salePrice": None, "productName": None, "subTitle": None,
         "productImageBig": "健康检测"},
        {"id": 58, "panelId": 0, "type": "健康食品", "productId": None, "sortOrder": 2,
         "fullUrl": "http://xmall.exrick.cn/#/thanks", "picUrl": "健康食品", "picUrl2": None,
         "picUrl3": None, "created": 1532695807000, "updated": 1532701518000,
         "salePrice": None, "productName": None, "subTitle": None,
         "productImageBig": "健康食品"},
        {"id": 59, "panelId": 0, "type": "健康用品", "productId": None, "sortOrder": 3,
         "fullUrl": "http://xmadmin.exrick.cn",
         "picUrl": "健康用品", "picUrl2": None, "picUrl3": None, "created": 1532701544000, "updated": 1532701614000,
         "salePrice": None, "productName": None, "subTitle": None, "productImageBig": "健康用品"},
        {"id": 68, "panelId": 0, "type": "体育用品", "productId": None, "sortOrder": 4, "fullUrl": "http://xpay.exrick.cn",
         "picUrl": "体育用品", "picUrl2": None, "picUrl3": None, "created": 1569839494000, "updated": 1569839494000,
         "salePrice": None, "productName": None, "subTitle": None, "productImageBig": "体育用品"},
        {"id": 61, "panelId": 0, "type": "健康服务", "productId": None, "sortOrder": 5,
         "fullUrl": "https://github.com/Exrick/x-boot", "picUrl": "健康服务", "picUrl2": None, "picUrl3": None,
         "created": 1532701581000, "updated": 1541324408000, "salePrice": None, "productName": None, "subTitle": None,
         "productImageBig": "健康服务"}
    ]})


# /goods/allGoods?page=1&size=20&sort=&priceGt=&priceLte=
# 这里要做一个分页，接受参数，然后返回分页后的结果
@app.route("/goods/allGoods")
def all_goods():
    # 如果带了 type 分类信息，就返回不同的分类给他
    print(request.args)

    if request.args.get("type") in ["健康服务"]:
        return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572505215697,
                        "result": {"total": 1, "data": [
                            {"productId": 150642571432849, "salePrice": 9.90, "productName": "健身培训",
                             "subTitle": "有减脂、增肌、塑形等普通课程；也有拳击、拉伸、体态调整等特色课程",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092059359158.jpg"},
                            {"productId": 150642571432847, "salePrice": 249.00, "productName": "网球培训",
                             "subTitle": "有优秀运动员退役资深教练，也有国际知名顶级专业教练",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092100205673.jpg"},
                            {"productId": 15064257143284712, "salePrice": 249.00, "productName": "康养体验营",
                             "subTitle": "5天康养基地活动，食疗+理疗+心疗，面向三高人群",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092101076456.jpg"},
                            {"productId": 15064257143284721, "salePrice": 249.00, "productName": "网球培训",
                             "subTitle": "有优秀运动员退役资深教练，也有国际知名顶级专业教练",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092100205673.jpg"}
                        ]}})
    elif request.args.get("type") in ["健康食品"]:
        return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572505215697,
                        "result": {"total": 1, "data": [
                            {"productId": 15064257143284811, "salePrice": 199.00, "productName": "五谷扁粮饭",
                             "subTitle": "生态五谷扁粮，家庭营养主食",
                             "productImageBig": "https://img11.360buyimg.com/n1/jfs/t26305/153/1540992424/242754/d3070cc9/5bed227aNba46b4d2.jpg"},
                            {"productId": 1506425714328461, "salePrice": 149.00,
                             "productName": "草本营养餐", "subTitle": "改变膳食结构，回归自然养生",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092033162363.png"},
                            {"productId": 1506425714328452, "salePrice": 199.00, "productName": "仁师傅眷村风味牛肉面",
                             "subTitle": "细火慢炖汤头清新浓郁，令人回味无穷",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092036038028.jpg"},
                            {"productId": 150642571432836123, "salePrice": 149.00, "productName": "仁师傅旗鱼松（金枪鱼）",
                             "subTitle": "严选上等新鲜黑旗鱼胸腹部位，含有丰富鱼肉纤维口感香酥带嚼勁，色泽金黄、入口即化",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092037487244.jpg"},
                            {"productId": 150642571432836222, "salePrice": 149.00, "productName": "仁师傅酵素梅",
                             "subTitle": "採用特選大顆成熟的梅子，以低糖、低鹽，烘乾而成，淡淡梅香微甜不膩",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092038424695.jpg"},
                            {"productId": 150642571432836333, "salePrice": 149.00, "productName": "溯源码完美盏燕窝",
                             "subTitle": "正规溯源码天然白燕盏印，尼孕纯净雨林，优等干燕窝",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092039474228.jpg"},
                            {"productId": 150642571432842444, "salePrice": 149.00, "productName": "上等文山三七",
                             "subTitle": "有机好三七，来自举世公认的最好的三七产地文山",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092040318000.jpg"}]}})
    elif request.args.get("type") in ["健康检测"]:
        return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572505215697,
                        "result": {"total": 1, "data": [
                            {"productId": 150642571432848, "salePrice": 199.00, "productName": "个性化体检套餐",
                             "subTitle": "为用户精准了解当前的健康状态",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092045038833.png"},
                            {"productId": 1506425714328462, "salePrice": 149.00,
                             "productName": "女士易感基因检测", "subTitle": "女士肿瘤+慢病全套检测（24项）",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092047188630.jpg"},
                            {"productId": 1506425714328453, "salePrice": 199.00, "productName": "男士易感基因检测",
                             "subTitle": "男士肿瘤+慢病全套检测（21项）",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092048181028.jpg"},
                            {"productId": 150642571432836, "salePrice": 149.00, "productName": "儿童基因检测",
                             "subTitle": "儿童优势+成长发育全套检测（14项）",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092048548320.jpg"}]}})
    elif request.args.get("type") in ["健康用品"]:
        return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572505215697,
                        "result": {"total": 1, "data": [
                            {"productId": 150642571432848321, "salePrice": 199.00, "productName": "仁医师马油护手霜50ml",
                             "subTitle": "防止肌肤干燥、保持双手滋润亮白的肌肤深层滋养马油乳木果护手霜",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092052302994.png"},
                            {"productId": 1506425714328463, "salePrice": 149.00,
                             "productName": "仁医师马油酵素洗面霜100ml", "subTitle": "清洁毛孔 保湿不紧绷 添加酵素精华的马油酵素洗面霜",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092053116217.png"}]}})
    elif request.args.get("type") in ["体育用品"]:
        return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572505215697,
                        "result": {"total": 1, "data": [
                            {"productId": 150642571432848000, "salePrice": 199.00, "productName": "Nike耐克女运动休闲防风保暖双面穿棉衣",
                             "subTitle": "连帽短款高端保暖运动外套，耐磨防风，2018冬款",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092054355828.jpg"},
                            {"productId": 1506425714328464, "salePrice": 149.00,
                             "productName": "Nike耐克男运动防风羽绒服", "subTitle": "优质保暖AIR JORDAN运动防风羽绒服，耐磨 透气",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092055115444.jpg"},
                            {"productId": 1506425714328465, "salePrice": 149.00,
                             "productName": "ASICS亚瑟士男GEL-RESOLUTION 7专业网球鞋", "subTitle": "孟菲尔斯19年新款，蓄能减震，防滑耐磨透气，包裹性佳",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092055536961.jpg"},
                            {"productId": 1506425714328466, "salePrice": 149.00,
                             "productName": "HEAD海德网球拍", "subTitle": "兹维列夫GRAVITY系列专业网球拍 2019新款",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092056298796.jpg"},
                            {"productId": 1506425714328467, "salePrice": 149.00,
                             "productName": "HEAD海德 健身球瑜伽球", "subTitle": "防爆瑜伽球是瑜伽、减肥、运动、健身的不二之选",
                             "productImageBig": "https://api.ai2hit.com/static/upload/201911092057167625.jpg"}]}})
    else:
        if request.args.get("page") == "1":
            return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572446419191,
                            "result": {"total": 32, "data": [
                                {"productId": 150642571432849, "salePrice": 9.90, "productName": "健身培训",
                                 "subTitle": "有减脂、增肌、塑形等普通课程；也有拳击、拉伸、体态调整等特色课程",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092059359158.jpg"},
                                {"productId": 150642571432847, "salePrice": 249.00, "productName": "网球培训",
                                 "subTitle": "有优秀运动员退役资深教练，也有国际知名顶级专业教练",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092100205673.jpg"},
                                {"productId": 15064257143284712, "salePrice": 249.00, "productName": "康养体验营",
                                 "subTitle": "5天康养基地活动，食疗+理疗+心疗，面向三高人群",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092101076456.jpg"},
                                {"productId": 15064257143284721, "salePrice": 249.00, "productName": "网球培训",
                                 "subTitle": "有优秀运动员退役资深教练，也有国际知名顶级专业教练",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092100205673.jpg"},
                                {"productId": 15064257143284811, "salePrice": 199.00, "productName": "五谷扁粮饭",
                                 "subTitle": "生态五谷扁粮，家庭营养主食",
                                 "productImageBig": "https://img11.360buyimg.com/n1/jfs/t26305/153/1540992424/242754/d3070cc9/5bed227aNba46b4d2.jpg"},
                                {"productId": 1506425714328461, "salePrice": 149.00,
                                 "productName": "草本营养餐", "subTitle": "改变膳食结构，回归自然养生",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092033162363.png"},
                                {"productId": 1506425714328452, "salePrice": 199.00, "productName": "仁师傅眷村风味牛肉面",
                                 "subTitle": "细火慢炖汤头清新浓郁，令人回味无穷",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092036038028.jpg"},
                                {"productId": 150642571432836123, "salePrice": 149.00, "productName": "仁师傅旗鱼松（金枪鱼）",
                                 "subTitle": "严选上等新鲜黑旗鱼胸腹部位，含有丰富鱼肉纤维口感香酥带嚼勁，色泽金黄、入口即化",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092037487244.jpg"},
                                {"productId": 150642571432836222, "salePrice": 149.00, "productName": "仁师傅酵素梅",
                                 "subTitle": "採用特選大顆成熟的梅子，以低糖、低鹽，烘乾而成，淡淡梅香微甜不膩",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092038424695.jpg"},
                                {"productId": 150642571432836333, "salePrice": 149.00, "productName": "溯源码完美盏燕窝",
                                 "subTitle": "正规溯源码天然白燕盏印，尼孕纯净雨林，优等干燕窝",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092039474228.jpg"},
                                {"productId": 150642571432842444, "salePrice": 149.00, "productName": "上等文山三七",
                                 "subTitle": "有机好三七，来自举世公认的最好的三七产地文山",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092040318000.jpg"},
                                {"productId": 150642571432848, "salePrice": 199.00, "productName": "个性化体检套餐",
                                 "subTitle": "为用户精准了解当前的健康状态",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092045038833.png"},
                                {"productId": 1506425714328462, "salePrice": 149.00,
                                 "productName": "女士易感基因检测", "subTitle": "女士肿瘤+慢病全套检测（24项）",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092047188630.jpg"},
                                {"productId": 1506425714328453, "salePrice": 199.00, "productName": "男士易感基因检测",
                                 "subTitle": "男士肿瘤+慢病全套检测（21项）",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092048181028.jpg"},
                                {"productId": 150642571432836, "salePrice": 149.00, "productName": "儿童基因检测",
                                 "subTitle": "儿童优势+成长发育全套检测（14项）",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092048548320.jpg"},
                                {"productId": 150642571432848321, "salePrice": 199.00, "productName": "仁医师马油护手霜50ml",
                                 "subTitle": "防止肌肤干燥、保持双手滋润亮白的肌肤深层滋养马油乳木果护手霜",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092052302994.png"},
                                {"productId": 1506425714328463, "salePrice": 149.00,
                                 "productName": "仁医师马油酵素洗面霜100ml", "subTitle": "清洁毛孔 保湿不紧绷 添加酵素精华的马油酵素洗面霜",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092053116217.png"},
                                {"productId": 150642571432848000, "salePrice": 199.00,
                                 "productName": "Nike耐克女运动休闲防风保暖双面穿棉衣",
                                 "subTitle": "连帽短款高端保暖运动外套，耐磨防风，2018冬款",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092054355828.jpg"},
                                {"productId": 1506425714328464, "salePrice": 149.00,
                                 "productName": "Nike耐克男运动防风羽绒服", "subTitle": "优质保暖AIR JORDAN运动防风羽绒服，耐磨 透气",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092055115444.jpg"},
                                {"productId": 1506425714328465, "salePrice": 149.00,
                                 "productName": "ASICS亚瑟士男GEL-RESOLUTION 7专业网球鞋",
                                 "subTitle": "孟菲尔斯19年新款，蓄能减震，防滑耐磨透气，包裹性佳",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092055536961.jpg"},
                            ]}})
        else:
            return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572446419191,
                            "result": {"total": 32, "data": [
                                {"productId": 1506425714328466, "salePrice": 149.00,
                                 "productName": "HEAD海德网球拍", "subTitle": "兹维列夫GRAVITY系列专业网球拍 2019新款",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092056298796.jpg"},
                                {"productId": 1506425714328467, "salePrice": 149.00,
                                 "productName": "HEAD海德 健身球瑜伽球", "subTitle": "防爆瑜伽球是瑜伽、减肥、运动、健身的不二之选",
                                 "productImageBig": "https://api.ai2hit.com/static/upload/201911092057167625.jpg"}
                            ]}})


# 进入具体某个商品的详情，需要传入参数 productId
@app.route("/goods/productDetail")
def product_detail():
    print(request.args)
    if request.args.get("productId"):
        print(request.args.get("productId"))
        return jsonify({"success": True, "message": "success", "code": 200, "timestamp": 1572522173985,
                        "result": {"productId": 15064257143284811, "salePrice": 199.00, "productName": "五谷扁粮饭",
                                   "subTitle": "生态五谷扁粮，家庭营养主食", "limitNum": 100,
                                   "productImageBig": "https://img11.360buyimg.com/n1/jfs/t29275/174/260500715/288384/ccdb0c1c/5bed227aN9fcd6992.jpg",
                                   # "detail": "<img src=\"https://resource.smartisan.com/resource/27a054301d8e10c40461443928dccd77.jpg\" style=\"width:1220px;height:7451px;\" alt=\"\" />",
                                   "detail": '<div style="text-align:center;font-size:0px">'
                                             '<img width="100%" src="https://img30.360buyimg.com/popWaterMark/jfs/t1/66160/4/13847/151006/5db25173Ef8c12d57/455a9dd4e7c66995.jpg"/>'
                                             '<img width="100%" src="https://img30.360buyimg.com/popWaterMark/jfs/t1/71656/21/13781/173276/5db25173Edb7c11cf/63993d025efac6e6.jpg"/>'
                                             '<img width="100%" src="https://img30.360buyimg.com/popWaterMark/jfs/t1/76168/20/13837/166820/5db25173E33beaafe/dd094af1f0f89e28.jpg"/>'
                                             '<img width="100%" src="https://img30.360buyimg.com/popWaterMark/jfs/t1/60433/1/13831/162338/5db25173E4a4d9066/673b1aee941e8c5e.jpg"/>'
                                             '<img width="100%" src="https://img30.360buyimg.com/popWaterMark/jfs/t1/51643/23/14353/203101/5db25173E05cd57e8/857dbe3ead4455d2.jpg"/>'
                                             '<img width="100%" src="https://img30.360buyimg.com/popWaterMark/jfs/t1/93455/40/707/173321/5db25173E91df8864/d725b6b9766c45f0.jpg"/>'
                                             '<img width="100%" src="https://img30.360buyimg.com/popWaterMark/jfs/t1/90564/18/702/175043/5db25174E0cb766de/198e26573b9eedab.jpg"/>'
                                             '<img width="100%" src="https://img30.360buyimg.com/popWaterMark/jfs/t1/73925/40/13790/176899/5db25174E9a59044d/f30aeb5a07bae98b.jpg"/>'
                                             '<img width="100%" src="https://img30.360buyimg.com/popWaterMark/jfs/t1/75815/22/13793/186011/5db25174E0ee49db4/16b0157511ea07e8.jpg"/>'
                                             '<img width="100%" src="https://img30.360buyimg.com/popWaterMark/jfs/t1/56225/10/14223/195771/5db25174Ef6c2aea0/55ea4269e7054324.jpg"/>'
                                             '</div>',

                                   "productImageSmall": [
                                       "https://img11.360buyimg.com/n1/jfs/t29275/174/260500715/288384/ccdb0c1c/5bed227aN9fcd6992.jpg",
                                       "https://img11.360buyimg.com/n7/jfs/t26305/153/1540992424/242754/d3070cc9/5bed227aNba46b4d2.jpg",
                                       "https://img11.360buyimg.com/n1/jfs/t26215/237/1792888488/253540/f2ec4823/5bed227aNd1423b3e.jpg"
                                   ]}})


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
