#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/25 22:25
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
from flask import jsonify

__author__ = 'Max_Pengjb'


def trueReturn(data, msg, token=None):
    return jsonify({
        "status": True,
        "data": data,
        "msg": msg,
        "token": token
    })


def falseReturn(data, msg, token=None):
    return jsonify({
        "status": False,
        "data": data,
        "msg": msg,
        "token": token
    })
