#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/23 22:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

a = {"count": 3,
 "infos":
     [
         {"name": "赵昊", "age": 15, "height": 1.83, "sex": "男性"},
         {"name": "龙傲天", "age": 16, "height": 2.00, "sex": "男性"},
         {"name": "玛丽苏", "age": 15, "height": 1.78, "sex": "女性"}
     ]
 }
for i in range(len(a["infos"])):
    a["infos"][i]["age"] += 1
    print(a["infos"][i]["age"])

a["infos"].append({"name": "赵昊", "age": 15, "height": 1.83, "sex": "男性"})
print(a)
