#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/26 17:38
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1298. 你能从盒子里获得的最大糖果数  Maximum Candies You Can Get from Boxes
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
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:

        visited = []
        res = 0
        flag = True
        while flag:
            flag = False
            for box in initialBoxes:
                # 这个盒子打开的,搜刮这个盒子
                if status[box]:
                    flag = True
                    visited.append(box)
                    res += candies[box]
                    initialBoxes.remove(box)
                    for cbox in containedBoxes[box]:
                        if cbox not in visited:
                            initialBoxes.append(cbox)
                    for key_index in keys[box]:
                        status[key_index] = 1
        return res


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
