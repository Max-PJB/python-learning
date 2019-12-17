#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/17 15:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       868. 二进制间距 Binary Gap
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
    def binaryGap(self, N: int) -> int:
        res = []
        i = 0
        while N:
            N, r = divmod(N, 2)
            if r:
                res.append(i)
            i += 1
        if len(res) < 2:
            return 0
        else:
            return max(map(lambda x, y: y - x, res[:-1], res[1:]))


inin = 222
r = Solution().binaryGap(inin)
print(r)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
