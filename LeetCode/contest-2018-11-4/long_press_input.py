#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/4 11:51
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

示例 1：

输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。

示例 2：

输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。

示例 3：

输入：name = "leelee", typed = "lleeelee"
输出：true

示例 4：

输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。


提示：

    name.length <= 1000
    typed.length <= 1000
    name 和 typed 的字符都是小写字母。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def is_longest_pressed_name(name, typed):
    name = retain_one(name)
    typed = retain_one(typed)
    if name[0] == typed[0]:
        ss = list(filter(lambda x: x < 0, map(lambda x, y: y - x, name[1], typed[1])))
        if not ss:
            return True
    return False


def retain_one(ss):
    ss = list(ss)
    res1 = []
    res2 = []
    if ss:
        i = 0
        n = len(ss)
        while i < n:
            count = 1
            m = ss[i]
            while i + 1 < n and ss[i] == ss[i + 1]:
                count += 1
                i += 1
            res1.append(m)
            res2.append(count)
            i += 1
    return [res1, res2]


# name = "alex"
# typed = "aaleex"
# name = "saeed"
# typed = "ssaaedd"
# name = "leelee"
# typed = "lleeelee"
name = "laiden"
typed = "laiden"
print(retain_one(name))
print(retain_one(typed))
print(is_longest_pressed_name(name, typed))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
