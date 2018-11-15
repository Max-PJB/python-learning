#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 10:49
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  反转链表

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
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
    # 迭代
    def reverse_link_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head and head.next:
            q = head.next
            head.next = pre
            pre = head
            head = q
        if head:
            head.next = pre
        # while head:
        #     print(head.val)
        #     head = head.next
        return head


head = ListNode(1)
p = head
for i in range(2,6):
    p.next = ListNode(i)
    p = p.next
p = head
while p.next:
    print(p.val,"->",end="")
    p = p.next
print(p.val)
p = Solution().reverse_link_list(head)
# while p.next:
#     print(p.val,"->",end="")
#     p = p.next
# print(p.val)


# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



