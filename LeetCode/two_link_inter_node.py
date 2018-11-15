#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 16:46
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  相交链表

编写一个程序，找到两个单链表相交的起始节点。



例如，下面的两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

在节点 c1 开始相交。



注意：

    如果两个链表没有交点，返回 null.
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。


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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 我写的很复杂啊。
        # 网上别人的实现起来就很简单
        # 用 p，q的交换很巧妙的实现了 相差个数的切换，免去了计数和很多variables
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
        return p1


"""        
        if not headA or not headB:
            return None
        cnt_a = 0
        cnt_b = 0
        p = headA
        q = headB
        pp = headA
        qq = headB
        while p:
            p = p.next
            cnt_a += 1
        while q:
            q = q.next
            cnt_b += 1
        if p != q:
            return None
        if cnt_a > cnt_b:
            for _ in range(cnt_a-cnt_b):
                pp = pp.next
        else:
            for _ in range(cnt_b-cnt_a):
                qq = qq.next
        while pp != qq:
            pp = pp.next
            qq = qq.next
        return pp
"""

head1 = ListNode(1)
p = head1
for i in range(2, 6):
    p.next = ListNode(i)
    p = p.next
head2 = ListNode(9)
head2.next = head1.next.next
res = Solution().getIntersectionNode(head1, head2)
print(not res or res.val)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
