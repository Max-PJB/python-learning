#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/8 13:57
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


# 下面写上代码块
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ab_eq = []
        ab_ne = []
        for a, equ, _, b in equations:
            print(a, equ, b)
            if equ == '=':
                ab_eq.append([a, b])
            else:
                ab_ne.append([a, b])
        buckets = []
        visited = set()

        def find_buc_ind(x):
            for i, buc in enumerate(buckets):
                if x in buc:
                    return i

        for a, b in ab_eq:
            if a not in visited:
                buckets.append({a})
                visited.add(a)
            if b not in visited:
                buckets.append({b})
                visited.add(b)
            buc_a_ind = find_buc_ind(a)
            buc_b_ind = find_buc_ind(b)
            if buc_a_ind != buc_b_ind:
                buckets[buc_a_ind].update(buckets[buc_b_ind])
                buckets.pop(buc_b_ind)
        print(buckets)
        for a, b in ab_ne:
            if a not in visited:
                buckets.append({a})
            if b not in visited:
                buckets.append({b})
            buc_a_ind = find_buc_ind(a)
            buc_b_ind = find_buc_ind(b)
            if buc_a_ind == buc_b_ind:
                return False
        return True


inin = ["c==c","b==d","x!=z"]
rr = Solution().equationsPossible(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
