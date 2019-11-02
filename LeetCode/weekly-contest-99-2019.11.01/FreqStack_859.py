#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/1 15:10
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class FreqStack:

    def __init__(self):
        # 一个字典，保存一个数字对应的当前频率
        self.num_fre_dict = {}
        # 当前最大的频率
        self.current_max_fre = 0
        # fre_stack 二维数组，fre_stack[i] = [a,b,c,d] 表示 数字 a b c d 频率为 i 时 ，他们的进栈顺序
        self.fre_stack = [[] for _ in range(10000)]

    def push(self, x: int) -> None:
        # 已经存在，那么频率就要加1了
        x_fre = self.num_fre_dict.get(x, 0) + 1
        self.num_fre_dict[x] = x_fre
        self.fre_stack[x_fre].append(x)
        # 修改 当前最大的频率，为 pop 做准备
        self.current_max_fre = max(self.current_max_fre, x_fre)
        # print("push", x, self.current_max_fre, self.fre_stack)

    def pop(self) -> int:
        # print(self.current_max_fre, self.fre_stack)
        top = self.fre_stack[self.current_max_fre].pop()
        # 这个数字对应的 频率 减少 1
        self.num_fre_dict[top] -= 1
        # 抛出去后，如果这个频率的框中为空，那最大频率就减1
        if not self.fre_stack[self.current_max_fre]:
            self.current_max_fre -= 1
        # print("pop", top, self.current_max_fre, self.fre_stack)
        return top


# ["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
# [[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
fq = FreqStack()
fq.push(4)
fq.push(0)
fq.push(9)
fq.push(3)
fq.push(4)
fq.push(2)
print(fq.pop())
fq.push(6)
print(fq.pop())
fq.push(1)
print(fq.pop())
fq.push(1)
print(fq.pop())
fq.push(4)
print(fq.pop())
print(fq.pop())
print(fq.pop())
print(fq.pop())
print(fq.pop())
print(fq.pop())

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
