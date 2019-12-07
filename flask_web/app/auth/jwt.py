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

import jwt
import datetime, time
from config.default import Config


class JWT:
    @staticmethod
    def encode_auth_token(username):
        """
        生成认证Token
        :param username: User
        :return: string
        """
        try:
            payload = {
                # 有效期，在exp之后的时间，token无效   jwt.ExpiredSignatureError
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=Config.EXP_SECONDS),
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
            ).decode(encoding="utf-8")
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
                return '无效Token'
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'
