#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/25 21:53
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time

from flask_wtf import csrf

__author__ = 'Max_Pengjb'

from flask import jsonify, request
from flask_web.app.models.User import User
from .. import commonReturn
from .jwt import JWT
from flask_mongoengine.wtf import model_form

PostForm = model_form(User)


def init_api(app):
    @app.route('/register', methods=['POST'])
    def register():
        """
        用户注册
        :return: json
        """
        form = PostForm(request.form)
        # 跨域就出现问题，我真的是服了这个 flask_mongoengine， bug是真的多
        #  解决前后端分离 'csrf_token': ['The CSRF token is missing.'] 问题
        form.csrf_token.data = csrf.generate_csrf()
        if form.validate():
            print(form)
        else:
            print(form.errors)
            print("nonono", form.username.data, form.passwd.data)
        username = request.form.get('username')
        password = request.form.get('password')
        # user = User(name=username,  passwd=User.set_passwd(User, passwd))
        user = User(username=username)
        # 这里要分开写，不然会报错，因为 password 是通过@property 和 @property.setter 来定义的
        user.password = password
        user.save()
        print(user.to_mongo())
        if user.id:
            returnUser = {
                'id': str(user.id),
                'username': user.username
            }
            return jsonify(commonReturn.trueReturn(returnUser, "用户注册成功"))
        else:
            return jsonify(commonReturn.falseReturn('', '用户注册失败'))

    @app.route('/login', methods=['POST'])
    def login():
        """
        用户登录
        :return: json
        """
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return jsonify(commonReturn.falseReturn('', '用户名和密码不能为空'))
        else:
            userInfo = User.objects(username=username).first()
            if userInfo is None:
                return jsonify(commonReturn.falseReturn('', '找不到用户'))
            else:
                if userInfo.check_password(password):
                    token = JWT.encode_auth_token(userInfo.username)
                    # print(token,type(token))  # decode() 方法以指定的编码格式解码 bytes 对象。
                    return jsonify(commonReturn.trueReturn(token.decode(encoding="utf-8"), '登录成功'))
                else:
                    return jsonify(commonReturn.falseReturn('', '密码不正确'))

    @app.route('/user', methods=['GET'])
    def get():
        """
        获取用户信息
        :return: json
        """
        for i in dir(request):
            print(i, "->", getattr(request, i))

        result = JWT.identify(request)
        return jsonify(result)
