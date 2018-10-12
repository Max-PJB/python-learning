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

operate = ['+', '-', '*', '/']


def eval_rpn(express_list):
    stack = []
    top = 0
    for operation in express_list:
        if operation in operate:
            if top < 2:
                return False
            m = stack.pop()
            n = stack.pop()
            if operation == '+':
                k = m + n
            elif operation == '-':
                k = m - n
            elif operation == '*':
                k = m * n
            elif operation == '/':
                k = n / m
            else:
                pass
            stack.append(k)
            top -= 1
        else:
            stack.append(int(operation))
            top += 1
    if top > 1:
        return False
    else:
        return stack[0]


inpp = ["4", "2", "/"]
print(eval_rpn(inpp))
