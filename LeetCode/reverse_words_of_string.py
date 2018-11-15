#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/13 20:22
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def reverse_words(s):
    print(" ".join(map(lambda x: x[::-1], s.split())))
    pass


s_in = "Let's take LeetCode contest"
reverse_words(s_in)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



