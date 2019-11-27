#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/25 22:09
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import jwt, datetime, time
from flask import jsonify
from flask_web.config.default import Config
from flask_web.app.models.User import User
from .. import commonReturn


class JWT:
    @staticmethod
    def encode_auth_token(username):
        """
        生成认证Token
        :param username: string
        :return: string
        """
        try:
            payload = {
                # 有效期，在exp之后的时间，token无效   jwt.ExpiredSignatureError
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
                # 发布者，可有可无，表示是谁给出这个token，针对不同的 application 可以设置不同的 iss
                # If the issuer claim is incorrect, jwt.InvalidIssuerError will be raised.
                'iss': 'ken',
                'iat': datetime.datetime.utcnow(),
                'data': {
                    'username': username,
                    'login_time': int(time.time())
                }
            }
            return jwt.encode(
                payload,
                Config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
            # payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'), leeway=datetime.timedelta(seconds=10))
            payload = jwt.decode(auth_token, Config.SECRET_KEY, algorithms=['HS256'])
            if 'data' in payload and 'username' in payload['data']:
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    @staticmethod
    def authenticate(username, password):
        """
        用户登录，登录成功返回token，写将登录时间写入数据库；登录失败返回失败原因
        :param username:
        :param password:
        :return: json
        """
        userInfo = User.objects(username=username).first()
        if userInfo is None:
            return jsonify(commonReturn.falseReturn('', '找不到用户'))
        else:
            if userInfo.check_password(password):
                token = JWT.encode_auth_token(userInfo.id)
                return token
            else:
                return jsonify(commonReturn.falseReturn('', '密码不正确'))

    @staticmethod
    def identify(request):
        """
        用户鉴权
        :return: list
        """
        token = request.headers.get('Authorization')
        print(token)
        if token:
            payload = JWT.decode_auth_token(token)
            if not isinstance(payload, str):
                # 从数据库中找一个username和token解析的username一致的用户出来
                user = User.objects(username=payload['data']['username']).first()
                if user is None:
                    result = commonReturn.falseReturn('', '找不到该用户信息')
                else:
                    result = commonReturn.trueReturn(user.username, '请求成功')
            else:
                result = commonReturn.falseReturn('', payload)
        else:
            result = commonReturn.falseReturn('', '没有提供认证token')
        return result
