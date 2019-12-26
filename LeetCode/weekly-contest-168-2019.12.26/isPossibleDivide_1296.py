#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/26 15:32
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1296. 划分数组为连续数字的集合 Divide Array in Sets of K Consecutive Numbers
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
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        from collections import Counter
        s = Counter(nums)
        ordered_nums = sorted(s)
        for num in ordered_nums:
            occ = s[num]
            if s[num] > 0:
                for i in range(num + 1, num + k):
                    if s[i] >= occ:
                        s[i] -= occ
                    else:
                        return False
        return True


nums = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
k = 3
rr = Solution().isPossibleDivide(nums, k)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
