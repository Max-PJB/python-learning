#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/25 21:07
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
from flask import Flask
from flask_cors import CORS

from flask_web.config import load_config

__author__ = 'Max_Pengjb'


def create_app():
    # 初始化 App
    config = load_config()
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)
    # Alternatively, you can specify CORS options on a resource and origin level of granularity by passing a dictionary as the resources option, mapping paths to a set of options. See the full list of options in the documentation.
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.before_request
    def auth_jwt():
        pass


    # 请求结束后干的事
    # @app.after_request
    # def after_request(response):
    #     response.headers.add('Access-Control-Allow-Origin', '*')
    #     # if request.method == 'OPTIONS':
    #     #     response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
    #     #     headers = request.headers.get('Access-Control-Request-Headers')
    #     #     if headers:
    #     #         response.headers['Access-Control-Allow-Headers'] = headers
    #     return response

    from flask_web.app.models import db
    db.init_app(app)

    from flask_web.app.auth.api import init_api
    init_api(app)

    return app
