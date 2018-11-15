#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 11:22
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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


a = 2 and 3
b = 2 or 3
print(a)
print(b)
head1 = ListNode(1)
head2 = ListNode(1)
p = head1
for i in range(2, 5):
    p.next = ListNode(i)
    p = p.next
p = head2
for i in range(3, 5):
    p.next = ListNode(i)
    p = p.next
res = Solution().mergeTwoLists(head1,head2)
while res:
    print(res.val,"->",end="")
    res = res.next
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



