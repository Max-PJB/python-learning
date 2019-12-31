#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/31 12:49
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1299. 将每个元素替换为右侧最大元素 Replace Elements with Greatest Element on Right Side
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
    def replaceElements(self, arr: List[int]) -> List[int]:
        gright = arr[-1]
        res = [-1]
        for i in arr[::-1]:
            gright = max(gright, i)
            res.append(gright)
        return res[::-1][1:]


arr = [17, 18, 5, 4, 6, 1]
rr = Solution().replaceElements(arr)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
