#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 12:26
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   旋转链表

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        q = head
        cnt = 1
        while cnt <= k and q.next:
            q = q.next
            cnt += 1
            print(p.val, q.val, "->", end="")
            print(cnt)
        if cnt <= k:
            k = k % cnt
            p = head
            q = head
            cnt = 1
            while cnt <= k and q.next:
                q = q.next
                cnt += 1
                print(p.val, q.val, "->", end="")
                print(cnt)
            while q.next:
                q = q.next
                p = p.next
        else:
            while q.next:
                q = q.next
                p = p.next
        q.next = head
        head = p.next
        p.next = None
        return head


head1 = ListNode(1)
p = head1
for i in range(2, 6):
    p.next = ListNode(i)
    p = p.next
k_in = 9
res = Solution().rotateRight(head1, k_in)
while res:
    print(res.val, "->", end="")
    res = res.next
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
