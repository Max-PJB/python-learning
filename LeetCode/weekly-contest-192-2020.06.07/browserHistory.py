#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/7 10:49
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()

# TODO 这个题目还没有做完呐
# 下面写上代码块
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = homepage
        self.backs = []
        self.forws = []

    def visit(self, url: str) -> None:
        self.forws = []
        self.backs.append(self.cur)
        self.cur = url

    def back(self, steps: int) -> str:
        if not self.backs:
            return self.cur
        steps = min(len(self.backs), steps)
        i = 0
        while i < steps:
            i += 1
            self.forws.append(self.cur)
            self.cur = self.backs.pop()
        return self.cur

    def forward(self, steps: int) -> str:
        if not self.forws:
            return self.cur
        steps = min(len(self.forws), steps)
        i = 0
        while i < steps:
            i += 1
            self.backs.append(self.cur)
            self.cur = self.forws.pop()
        return self.cur


opers = ["BrowserHistory", "back", "back", "visit", "forward", "visit", "visit", "visit", "back", "visit", "visit",
         "visit", "back", "visit", "visit", "visit", "visit", "back", "visit", "visit", "visit", "visit", "visit",
         "visit", "visit", "back", "forward", "back", "forward", "visit", "back", "visit", "visit"]
params = [["icpbj.com"], [1], [10], ["xbepk.com"], [8], ["kls.com"], ["dlkwxpf.com"], ["pnep.com"], [9], ["rmis.com"],
          ["bxf.com"], ["dz.com"], [2], ["acuqsax.com"], ["dcvo.com"], ["ijbg.com"], ["nlott.com"], [7], ["dd.com"],
          ["vssnq.com"], ["teur.com"], ["pn.com"], ["szi.com"], ["brhldg.com"], ["yulyoqv.com"], [4], [10], [8], [5],
          ["av.com"], [3], ["okr.com"], ["meli.com"]]

obj = BrowserHistory(params[0])
for i in range(1, len(opers)):
    func = getattr(obj, opers[i])
    rr = func(params[i][0])
    print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))

a = [1, 2, 3, 4, 5]
print(a[-4:-1])
