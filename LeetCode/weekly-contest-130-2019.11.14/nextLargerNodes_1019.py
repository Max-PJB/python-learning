#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/15 19:55
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1019. 链表中的下一个更大节点 Next Greater Node In Linked List
    https://leetcode-cn.com/problems/next-greater-node-in-linked-list/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        stack = []
        res = []
        i = 0
        p = head
        while p:
            res.append(0)
            while stack and p.val > stack[-1][0]:
                res[stack.pop()[1]] = p.val
            stack.append((p.val, i))
            p = p.next
            i += 1
        return res


inin = ListNode(2)
inin.next = ListNode(1)
inin.next.next = ListNode(5)
rr = Solution().nextLargerNodes(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
