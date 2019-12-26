#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/26 15:27
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1295. 统计位数为偶数的数字  Find Numbers with Even Number of Digits
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
    def findNumbers(self, nums: List[int]) -> int:
        return sum(map(lambda x: 0 if len(str(x)) % 2 else 1, nums))


nums = [12, 345, 2, 6, 7896]
rr = Solution().findNumbers(nums)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
