#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/3 22:06
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def is_valid(s):
    bracket_left = ["(", "{", "["]
    bracket_right = [")", "}", "]"]
    stack = []
    if not s:
        return True
    for i in s:
        if i in bracket_left:
            stack.append(i)
        elif i in bracket_right and stack:
            out = stack.pop()
            if bracket_left.index(out) != bracket_right.index(i):
                return False
        else:
            return False
    if stack:
        return False
    return True


ss = "([][]{})"
print(is_valid(ss))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
