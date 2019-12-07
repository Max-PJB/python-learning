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


def trueReturn(data, msg):
    return jsonify({
        "status": "success",
        "code": "200",
        "data": data,
        "msg": msg,
    })


def falseReturn(data, msg):
    return jsonify({
        "status": "failed",
        "code": "500",
        "data": data,
        "msg": msg,
    })
