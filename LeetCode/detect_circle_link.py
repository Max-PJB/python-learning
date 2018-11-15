#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 13:11
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   环形链表 II

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

说明：不允许修改给定的链表。

进阶：
你是否可以不用额外空间解决此题？
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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 超时了这个方法
        # ls = []
        # while head and head not in ls:
        #     ls.append(head)
        #     head = head.next
        # if head:
        #     return head
        # else:
        #     return None
        # 用快慢指针方法,快的走两步，慢的走一步
        """
        如下图所示，X,Y,Z分别为链表起始位置，环开始位置和两指针相遇位置，则根据快指针速度为慢指针速度的两倍，可以得出：
slow = a + b + k(b+c) // 其实，只要slow进入到了环，fast速度是slow的两倍，fast肯定可以在slow绕一圈之内超过他的，这里的 k == 0
fast = a + b + n(b+c)
2*slow = fast
2*(a+b) + 2k(b+c) = a + b + n(b+c)
a=(n -2k)*(b+c) - b = (n-2k-1)(b+c) + c
注意到b+c恰好为环的长度，故可以推出，如将此时两指针分别放在起始位置和相遇位置，并以相同速度前进，当一个指针走完距离a时，另一个指针恰好走出 绕环n-1圈加上c的距离。
故两指针会在环开始位置相遇。（换位置后第一次相遇）
相遇位置就是 从起点的刚好走到换的入口，而另一个在Z点出发的事绕了 n-2k-1 圈 再走 c 后到的环的入口
https://blog.csdn.net/Eartha1995/article/details/80990636
        """
        is_circle = None
        if not head:
            return is_circle
        fast = head
        slow = head
        res = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                is_circle = True
                while res != fast:
                    res = res.next
                    fast = fast.next
                break
        print(is_circle)
        return is_circle and res


head1 = ListNode(1)
p = head1
# for i in range(2, 6):
#     p.next = ListNode(i)
#     p = p.next
# p.next = head1.next
res = Solution().detectCycle(head1)
print(not res or res.val)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
