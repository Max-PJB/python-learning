#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/5/31 13:30
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
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
        to_from_dict = defaultdict(list)
        from_to_dict = defaultdict(list)
        for f, t in connections:
            to_from_dict[t].append(f)
            from_to_dict[f].append(t)
        arrives = {0}
        res = 0
        stack = [0]
        while stack:
            node = stack.pop(0)
            # 直接可以到的
            cans1 = set(to_from_dict[node])
            for can in cans1 - arrives:
                stack.append(can)
            arrives.update(cans1)
            # 改变方向可以到的
            cans2 = set(from_to_dict[node])
            for can in cans2 - arrives:
                stack.append(can)
                res += 1
            arrives.update(cans2)
        return res


n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
rr = Solution().minReorder(n, connections)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
