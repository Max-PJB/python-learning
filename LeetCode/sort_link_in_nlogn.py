#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/15 13:00
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    148. Sort List--O(nlogn)时间复杂度和常数空间复杂度给链表排序
    排序链表

在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4

示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge_2_link(link1, link2):
            """
            :type link1: ListNode
            :type link2: ListNode
            :rtype: ListNode
            """
            res = ListNode(0)
            pre = res
            while link1 and link2:
                if link1.val < link2.val:
                    pre.next = link1
                    link1 = link1.next
                    pre = pre.next
                else:
                    pre.next = link2
                    link2 = link2.next
                    pre = pre.next
            if link1:
                pre.next = link1
            if link2:
                pre.next = link2
            return res.next
            # 上面中间写上代码块

        def sort_list(link):
            if not link or not link.next:
                return link
            fast = slow = link
            cur = None
            while fast and fast.next:
                cur = slow
                slow = slow.next
                fast = fast.next.next
            cur.next = None
            link_left = sort_list(link)
            link_right = sort_list(slow)
            return merge_2_link(link_left, link_right)

        return sort_list(head)


head1 = ListNode(1)
p = head1
for i in range(7, 2, -1):
    p.next = ListNode(i)
    p = p.next
res = Solution().sortList(head1)
while res:
    print(res.val, "->", end="")
    res = res.next
end = time.time()
print('Running time: %s Seconds' % (end - start))
