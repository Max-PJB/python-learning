#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/13 21:39
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 存在重复元素

给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true

示例 2:

输入: [1,2,3,4]
输出: false

示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def contain_duplicate(nums):
    return not len(nums) == len(set(nums))


def contain_duplicate2(nums):
    num_dict = {}
    for i in nums:
        if i not in num_dict.keys():
            num_dict[i] = 1
        else:
            return True
    return False


n_in = [1,1,1,3,3,4,3,2,4,2]
print(contain_duplicate2(n_in))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



