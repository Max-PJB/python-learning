#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/3 20:41
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
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


# 双指针嘛，这个我知道的
def remove_nth_fomr_end(head, n):
    tail = head
    previous = head
    prior = head
    i = 1
    while i < n and tail.next:
        tail = tail.next
        i += 1
    if i == n:
        while tail.next:
            prior = previous
            previous = previous.next
            tail = tail.next
    print(id(head), id(prior), id(previous), id(tail))
    if head is previous:
        head = previous.next
    else:
        prior.next = previous.next
    return head


head_in = ListNode(1)
p = head_in
for x in range(2, 8):
    p.next = ListNode(x)
    p = p.next
print("初始链表：")
p = head_in
if head_in:
    print(head_in.val, end="")
while head_in.next:
    print("->", head_in.next.val, end='')
    head_in = head_in.next
print("")
n_in = 7
res = remove_nth_fomr_end(p, n_in)
print("删除倒数第{}个后链表:".format(n_in))
head_in = res
if head_in:
    print(head_in.val, end="")
while head_in.next:
    print("->", head_in.next.val, end='')
    head_in = head_in.next
print("")
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
