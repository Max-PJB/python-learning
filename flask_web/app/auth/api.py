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

# from flask_wtf import csrf

__author__ = 'Max_Pengjb'

from flask import request, g
from app.models.User import User, Permission
from app import jsonReturn
from app.auth.jwt import JWT
from flask_mongoengine.wtf import model_form

PostForm = model_form(User)


def init_api(app):
    @app.route('/register', methods=['POST'])
    def register():
        """
        用户注册
        :return: json
        """
        # form = PostForm(request.form)
        # 跨域就出现问题，我真的是服了这个 flask_mongoengine， bug是真的多
        #  解决前后端分离 'csrf_token': ['The CSRF token is missing.'] 问题
        # TODO 不用 form 传数据，省掉这些麻烦把，直接 json ，然后还可以用 mongo 的 fromjson 的 orm
        # form.csrf_token.data = csrf.generate_csrf()
        # if form.validate():
        #     print(form)
        # else:
        #     print(form.errors)
        #     return jsonReturn.falseReturn('', form.errors)
        # username = request.form.get('username')
        # password = request.form.get('password')
        req_json = request.json
        username = req_json.get('username')
        password = req_json.get('password')
        if not username or not password:
            return jsonReturn.falseReturn('', '用户名和密码不能为空')
        if User.objects(username=username).first():
            return jsonReturn.falseReturn('', '用户名已存在')
        user = User.register(username, password)
        # 这里User的password做了特别处理，需要加密保存，单独写了方法新建用户
        # password 是通过@property 和 @property.setter 来定义的，真正的 password 是 _password
        print(user.to_mongo())
        if user.id:
            returnUser = {
                'id': str(user.id),
                'username': user.username
            }
            g.username = username
            return jsonReturn.trueReturn(returnUser, "用户注册成功")
        else:
            return jsonReturn.falseReturn('', '用户注册失败')

    @app.route('/login', methods=['POST'])
    def login():
        """
        用户登录
        :return: json
        """
        username = request.json.get('username')
        password = request.json.get('password')
        # if not username or not password:
        if not username or not password:
            return jsonReturn.falseReturn('', '用户名和密码不能为空')
        else:
            userInfo = User.objects(username=username).first()
            if userInfo is None:
                return jsonReturn.falseReturn('', '找不到用户')
            else:
                if userInfo.check_password(password):
                    # 这里放入 g 的原因：
                    # 1.  登录之前默认的是一个临时用户，@app.before_request 为他设置了一个 g.username='__casual_user' + str(uuid_id)
                    # 2.  @app.after_request 会在 header 中添加 Authorization->token，
                    # 3.  生成token需要的username通过获取 g.username 来生成token的，所以这里需要将临时用户更新为登录后的用户
                    g.username = userInfo.username
                    # print(token,type(token))  # decode() 方法以指定的编码格式解码 bytes 对象。
                    token = JWT.encode_auth_token(userInfo.username)
                    # print(token)
                    # TODO 显示的在返回的结果中也传token，为了我测试的时候用，后面需要取消，统一在headers中通过Authorization来拿
                    return jsonReturn.trueReturn(token, '登录成功')
                else:
                    return jsonReturn.falseReturn('', '密码不正确')

    @app.route('/user', methods=['GET'])
    def get():
        """
        获取用户信息
        :return: json
        """
        return jsonReturn.trueReturn(g.username, '获取用户信息')

    # 访问地址的管理
    @app.route('/admin/add_permission', methods=['POST'])
    def add_permission():
        """
        访问地址的管理
        :return: json
        """
        url = request.args.get('url')
        name = request.args.get('name')
        description = request.args.get('description')
        if not url:
            return jsonReturn.trueReturn('', 'url访问路径是必须的')
        if Permission.objects(url=url).first():
            return jsonReturn.falseReturn(url, '失败：该路径权限已经存在')
        new_permission = Permission(url=url, name=name, description=description)
        new_permission.save()
        return jsonReturn.trueReturn(new_permission, '增加地址成功')

    @app.route('/admin/del_permission', methods=['POST'])
    def del_permission():
        """
        获取用户信息
        :return: json
        """
        url = request.args.get('url')
        target_permission = Permission.objects(url=url).first()
        if target_permission:
            r = target_permission.delete()
            return jsonReturn.trueReturn(r, '删除路径权限')
        else:
            return jsonReturn.falseReturn('', '目标路径权限不存在')

    # 角色的管理
    @app.route('/admin/add_role', methods=['POST'])
    def add_role():
        """
        获取用户信息
        :return: json
        """
        url = request.args.get('url')
        request.args.get('name')
        request.args.get('description')
        if not url:
            return
        new_permission = Permission(url='/login', name='登录', description='谁都能访问')
        new_permission.save()
        return jsonReturn.trueReturn(g.username, '获取用户信息')

    @app.route('/admin/del_role', methods=['POST'])
    def del_role():
        """
        获取用户信息
        :return: json
        """
        return jsonReturn.trueReturn(g.username, '获取用户信息')

    # 角色权限管理
    @app.route('/admin/add_permission_to_role', methods=['POST'])
    def add_permission_to_role():
        """
        获取用户信息
        :return: json
        """
        return jsonReturn.trueReturn(g.username, '获取用户信息')

    @app.route('/admin/del_permission_from_role', methods=['POST'])
    def del_permission_from_role():
        """
        获取用户信息
        :return: json
        """
        return jsonReturn.trueReturn(g.username, '获取用户信息')

    # 用户管理
    @app.route('/admin/add_user', methods=['POST'])
    def add_user():
        """
        获取用户信息
        :return: json
        """
        return jsonReturn.trueReturn(g.username, '获取用户信息')

    @app.route('/admin/del_user', methods=['POST'])
    def del_user():
        """
        获取用户信息
        :return: json
        """
        return jsonReturn.trueReturn(g.username, '获取用户信息')

    # 用户->角色管理
    @app.route('/admin/add_role_to_user', methods=['POST'])
    def add_role_to_user():
        """
        获取用户信息
        :return: json
        """
        return jsonReturn.trueReturn(g.username, '获取用户信息')

    @app.route('/admin/del_role_from_user', methods=['POST'])
    def del_role_from_user():
        """
        获取用户信息
        :return: json
        """
        return jsonReturn.trueReturn(g.username, '获取用户信息')
