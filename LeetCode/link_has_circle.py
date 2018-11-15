#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 12:58
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   环形链表

给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？
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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p = head
        while p.next:
            if p.next == head:
                return True
            else:
                q = p.next
                p.next = head
                p = q
        return False


head1 = ListNode(1)
p = head1
for i in range(2, 6):
    p.next = ListNode(i)
    p = p.next
# p.next = head1.next
res = Solution().hasCycle(head1)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



