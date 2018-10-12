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

SYMBOLS = {'{': '}', '[': ']', '(': ')', '<': '>'}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.keys(), SYMBOLS.values()


def is_valid(s):
    stack = []
    top = 0
    for w in s:
        if w in SYMBOLS_L:
            stack.append(w)
            top += 1
        else:
            if top > 0:
                top -= 1
            else:
                return False
            m = stack.pop()
            if w != SYMBOLS[m]:
                return False
    if top > 0:
        return False
    else:
        return True


print(is_valid("{{{{{{{[]{}()"))
