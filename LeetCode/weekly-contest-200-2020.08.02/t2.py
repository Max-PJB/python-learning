#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/19 10:27
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
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        from collections import defaultdict
        edges_dict = defaultdict(list)
        for i, j in edges:
            edges_dict[i].append(j)
            edges_dict[j].append(i)
        visited = set()
        from collections import Counter
        res = [0 for _ in range(n)]

        def bfs(k):
            visited.add(k)
            next_nodes = edges_dict[k]
            t = Counter(labels[k])
            for nod in next_nodes:
                if nod not in visited:
                    t += bfs(nod)
            res[k] = t[labels[k]]
            return t
        bfs(0)
        return res


n = 4
edges = [[0, 2], [1, 2], [0, 3]]
labels = "aeed"
rr = Solution().countSubTrees(n, edges, labels)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
