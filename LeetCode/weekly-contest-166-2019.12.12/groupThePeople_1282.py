#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/12 17:05
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       用户分组 Group the People Given the Group Size They Belong To
    https://leetcode-cn.com/contest/weekly-contest-166/problems/group-the-people-given-the-group-size-they-belong-to/
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
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict
        k_dict = defaultdict(list)
        for i, k in enumerate(groupSizes):

            k_dict[k].append(i)
        res = []
        for k, index_list in k_dict.items():
            for j in range(0, len(index_list), k):
                res.append(index_list[j:j + k])
        return res


inin = [3, 3, 3, 3, 3, 1, 3]
rr = Solution().groupThePeople(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
