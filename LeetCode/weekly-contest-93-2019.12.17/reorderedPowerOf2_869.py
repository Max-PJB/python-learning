#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/17 16:04
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       869. 重新排序得到 2 的幂 Reordered Power of 2
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
    def reorderedPowerOf2(self, N: int) -> bool:
        i = 0
        n = pow(2, i)
        T = pow(10, 9)
        r = []
        while n < T:
            r.append(n)
            i += 1
            n = pow(2, i)
        base = list(map(lambda x: sorted(str(x)), r))
        if sorted(str(N)) in base:
            return True
        else:
            return False


inin = 1
rr = Solution().reorderedPowerOf2(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
