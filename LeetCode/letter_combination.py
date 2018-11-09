#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/3 16:17
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()

NUM_LETTER = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"],
              7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}


# 下面写上代码块
def letter_combination(digits):
    if not digits:
        return []
    else:
        digits = list(map(int, digits))
        di = digits.pop(0)
        return recursive_combination(di, digits)


def recursive_combination(di, dis):
    if not dis:
        return NUM_LETTER[di]
    else:
        di2 = dis.pop(0)
        ls = recursive_combination(di2, dis)
        res = []
        for i in NUM_LETTER[di]:
            ls2 = map(lambda x, y: x + y, [i for _ in ls], ls)
            res.extend(ls2)
        return res


in_num = "7"
print(letter_combination(in_num))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
