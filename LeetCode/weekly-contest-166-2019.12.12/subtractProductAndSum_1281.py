#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/12 16:58
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       整数的各位积和之差 Subtract the Product and Sum of Digits of an Integer
    https://leetcode-cn.com/contest/weekly-contest-166/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sums = 0
        while n:
            n, r = divmod(n, 10)
            product *= r
            sums += r
        return product - sums


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
