#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/10/20 16:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807


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


def addTwoNumbers(l1, l2):
    x = l1.val
    y = l2.val
    l3 = ListNode(x + y)
    pp1 = l1.next
    pp2 = l2.next
    pp3 = l3
    print(pp1.val,pp2.val)
    while pp1 and pp2:
        print("run while")
        pp3.next = ListNode(pp1.val + pp2.val)
        pp1 = pp1.next
        pp2 = pp2.next
        pp3 = pp3.next
    if pp1:
        pp3.next = pp1
    else:
        pp3.next = pp2
    pp = l3
    while pp:
        x = int(pp.val / 10)
        pp.val %= 10
        if x:
            if not pp.next:
                pp.next = ListNode(x)
            else:
                pp.next.val += x
        else:
            pass
        pp = pp.next
    return l3


# l1 = ListNode(9)
# l1.next = ListNode(9)
# l1.next.next = ListNode(9)
# l1.next.next.next = ListNode(9)
# l1.next.next.next.next = ListNode(9)
# l2 = ListNode(9)
# l2.next = ListNode(9)
# l2.next.next = ListNode(9)
# l2.next.next.next = ListNode(9)
l1 = ListNode(0)
l2 = ListNode(0)

res = addTwoNumbers(l1, l2)
while res:
    print(res.val)
    res = res.next
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
"""
算法

就像你在纸上计算两个数字的和那样，我们首先从最低有效位也就是列表 l1l1l1 和 l2l2l2 的表头开始相加。由于每位数字都应当处于 0…90 \ldots 90…9 的范围内，我们计算两个数字的和时可能会出现“溢出”。例如，5+7=125 + 7 = 125+7=12。在这种情况下，我们会将当前位的数值设置为 222，并将进位 carry=1carry = 1carry=1 带入下一次迭代。进位 carrycarrycarry 必定是 000 或 111，这是因为两个数字相加（考虑到进位）可能出现的最大和为 9+9+1=199 + 9 + 1 = 199+9+1=19。

伪代码如下：

    将当前结点初始化为返回列表的哑结点。
    将进位 carrycarrycarry 初始化为 000。
    将 ppp 和 qqq 分别初始化为列表 l1l1l1 和 l2l2l2 的头部。
    遍历列表 l1l1l1 和 l2l2l2 直至到达它们的尾端。
        将 xxx 设为结点 ppp 的值。如果 ppp 已经到达 l1l1l1 的末尾，则将其值设置为 000。
        将 yyy 设为结点 qqq 的值。如果 qqq 已经到达 l2l2l2 的末尾，则将其值设置为 000。
        设定 sum=x+y+carrysum = x + y + carrysum=x+y+carry。
        更新进位的值，carry=sum/10carry = sum / 10carry=sum/10。
        创建一个数值为 (sum mod 10)(sum \bmod 10)(summod10) 的新结点，并将其设置为当前结点的下一个结点，然后将当前结点前进到下一个结点。
        同时，将 ppp 和 qqq 前进到下一个结点。
    检查 carry=1carry = 1carry=1 是否成立，如果成立，则向返回列表追加一个含有数字 111 的新结点。
    返回哑结点的下一个结点。

请注意，我们使用哑结点来简化代码。如果没有哑结点，则必须编写额外的条件语句来初始化表头的值。

请特别注意以下情况：
测试用例 	说明
l1=[0,1]l1=[0,1]l1=[0,1]
l2=[0,1,2]l2=[0,1,2]l2=[0,1,2] 	当一个列表比另一个列表长时。
l1=[]l1=[]l1=[]
l2=[0,1]l2=[0,1]l2=[0,1] 	当一个列表为空时，即出现空列表。
l1=[9,9]l1=[9,9]l1=[9,9]
l2=[1]l2=[1]l2=[1] 	求和运算最后可能出现额外的进位，这一点很容易被遗忘

public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode p = l1, q = l2, curr = dummyHead;
    int carry = 0;
    while (p != null || q != null) {
        int x = (p != null) ? p.val : 0;
        int y = (q != null) ? q.val : 0;
        int sum = carry + x + y;
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        if (p != null) p = p.next;
        if (q != null) q = q.next;
    }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return dummyHead.next;
}

复杂度分析

    时间复杂度：O(max⁡(m,n))O(\max(m, n))O(max(m,n))，假设 mmm 和 nnn 分别表示 l1l1l1 和 l2l2l2 的长度，上面的算法最多重复 max⁡(m,n)\max(m, n)max(m,n) 次。

    空间复杂度：O(max⁡(m,n))O(\max(m, n))O(max(m,n))， 新列表的长度最多为 max⁡(m,n)+1\max(m,n) + 1max(m,n)+1。

拓展

如果链表中的数字不是按逆序存储的呢？例如：

(3→4→2)+(4→6→5)=8→0→7 (3 \to 4 \to 2) + (4 \to 6 \to 5) = 8 \to 0 \to 7 (3→4→2)+(4→6→5)=8→0→7
"""