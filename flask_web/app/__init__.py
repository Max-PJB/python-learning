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
import random
import string
import time
import uuid

from flask import Flask, request, g
from flask_cors import CORS

from app import jsonReturn
from app.auth.jwt import JWT
from app.models.User import User, Role, Permission
from config import load_config

__author__ = 'Max_Pengjb'


def create_app():
    # 初始化 App
    config = load_config()
    app = Flask(__name__)
    app.config.from_object(config)
    # CORS(app)
    CORS(app, resources	={r"/*": {"expose_headers": ["Authorization"]}})

    # Alternatively, you can specify CORS options on a resource and origin level of granularity by passing a dictionary as the resources option, mapping paths to a set of options. See the full list of options in the documentation.
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from app.models import db
    db.init_app(app)

    from app.auth.api import init_api
    init_api(app)

    @app.before_first_request
    def create_admin_casual_user():
        admin = User.objects(username='admin').first()
        if not admin:
            permission_admin = Permission(url='*', name='超级权限', description='超级管理员的权限，哪里都能访问')
            permission_admin.save()
            super_admin = Role(name='超级管理员', description='超级管理员，哪里都能访问哦')
            super_admin.permissions.append(permission_admin)
            super_admin.save()
            admin = User(username='admin')
            admin.password = 'admin'
            admin.roles.append(super_admin)
            admin.save()

            # permission_casual = Permission(url='/login', name='登录', description='谁都能访问')
            # permission_casual.save()
            # permission_casual_reg = Permission(url='/register', name='注册', description='谁都能访问')
            # permission_casual_reg.save()
            # permission_casual_role = Role(name='everyone', description='临时用户')
            # permission_casual_role.permissions.append(permission_casual)
            # permission_casual_role.permissions.append(permission_casual_reg)
            # permission_casual_role.save()

    @app.before_request
    def auth_jwt():
        # 在每一个请求的时候判断token，然后根据请求的 path 判断有没有权限来控制放行
        token = request.headers.get('Authorization')
        # print(token)
        if token:
            payload = JWT.decode_auth_token(token)
            # payload 的返回值如果是字符串，那就是错误的token，过期或者无效token，正确的话会返回一个dict对象
            if not isinstance(payload, str):
                # 从数据库中找一个username和token解析的username一致的用户出来,
                user = User.objects(username=payload['data']['username']).first()
                # TODO 这里判断 user 存在不存在，实际应该用 redis 来做,token 存的肯定是登录过的用户啊，没有登录不会在token里面
                if user is None:
                    return jsonReturn.falseReturn('', '错误的token')
                username = user.username
                # 设置一个该次访问的全局 username，用于response 检查是否登录，登录了的话就更新 token
                g.username = username
                # 鉴权 rbac
                # TODO 这里需要改成 redis 取 permissions 后，设置为redis 直接存 user->permissions
                permissions = set(config.allow_urls)
                for role in user.roles:
                    # print(role)
                    for permission in role.permissions:
                        # print(permission.url)
                        permissions.add(permission.url)
                        # print(user.username, user.roles, permissions)
                # print(request.path)
                if request.path not in permissions and '*' not in permissions:
                    return jsonReturn.falseReturn(request.path, '没有访问权限')
            else:
                # 返回 token 过期，或者 token 无效
                # print(payload)
                return jsonReturn.falseReturn('', payload)
        else:
            # TODO token不存在只有一种情况： 系统临时用户，权限只有config['allow_urls']里的
            # 生成唯一id
            # uuid_id = uuid.uuid5(uuid.NAMESPACE_DNS, str(time.time()) + "".join(
            #     random.choice(string.ascii_letters + string.digits) for _ in range(16)))
            # 不在可匿名访问的目录中，就返回错误
            if request.path not in config.allow_urls:
                return jsonReturn.falseReturn(request.path, '需要登录')

    # 请求结束后干的事
    @app.after_request
    def after_request(response):
        # 在每一个请求结束的时候根据 request 中的 user 信息，存在 username 就说明是登录的用户，更新并返回 token
        if 'username' in g:
            token = JWT.encode_auth_token(g.username)
            # print("token:", token)
            print(g.username, JWT.decode_auth_token(token))
            response.headers.add('Authorization', token)
            # 加上这一段，不然前台 axios 拿到的 response 中没有 Authorization,也可以如上 CORS 中设置
            # response.headers.add('Access-Control-Expose-Headers', 'Authorization')
        return response

    return app
