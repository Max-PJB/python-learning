#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 12:02
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
-------------------------------------------------
"""
import time
from functools import reduce
__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return reduce(merge_two_list, lists, None)


def merge_two_list(l1, l2):
    p = l1
    q = l2
    pre = ListNode(0)
    head = pre
    while p and q:
        if p.val < q.val:
            pre.next = p
            p = p.next
            pre = pre.next
        else:
            pre.next = q
            q = q.next
            pre = pre.next
    if p:
        pre.next = p
    if q:
        pre.next = q
    return head.next


head1 = ListNode(1)
head2 = ListNode(1)
head3 = ListNode(2)
p = head1
for i in range(4, 6):
    p.next = ListNode(i)
    p = p.next
p = head2
for i in range(3, 5):
    p.next = ListNode(i)
    p = p.next
p = head3
for i in range(6, 7):
    p.next = ListNode(i)
    p = p.next
lists = [head1, head2, head3]
res = Solution().mergeKLists(lists)
while res:
    print(res.val,"->",end="")
    res = res.next
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
