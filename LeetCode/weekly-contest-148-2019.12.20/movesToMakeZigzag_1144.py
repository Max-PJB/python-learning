#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/20 14:45
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1144. 递减元素使数组呈锯齿状 Decrease Elements To Make Array Zigzag
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root:TreeNode 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        dp_even = 0
        dp_odd = 0
        # TODO 把这个月工资先结了吧
        pass


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
