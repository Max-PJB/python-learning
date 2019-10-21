#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/17 15:29
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  1004. 最大连续1的个数 III 显示英文描述
用户通过次数97
用户尝试次数143
通过次数102
提交次数299
题目难度Medium
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。



示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。


提示：

1 <= A.length <= 20000
0 <= K <= A.length
A[i] 为 0 或 1
-------------------------------------------------
"""
import time
from typing import List
import queue

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
"""
想象有条这样的贪吃蛇：它的肚子的容量为K，每吃掉一块食物（1代表食物），肚子的容量不变大也不变小，每吃掉一块石头（0代表石头，肚子的容量变小），不管是吃掉食物还是石头，身长都会增加1。
每当贪吃蛇无法再吃掉任何东西的时候，就无法再进食了，它必须等待他的肚子容量增加了才能继续吃，每排出来一块石头（0代表石头），肚子的容量又恢复了一格。
只要肚子不空，那么就一直吃，直到没得吃了为止。
因此我们可以定义贪吃蛇的头部为：j,尾部为i,肚子的容量为left,最大长度为res
"""
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        que = queue.Queue()
        dp = 0
        res = 0
        for i in range(len(A)):
            if A[i] == 1:
                dp = dp + 1
            elif A[i] == 0:
                if que.qsize() < K:
                    print("<K")
                    que.put(i)
                    dp = dp + 1
                else:
                    print("get()")
                    que.put(i)
                    j = que.get()
                    dp = i - j
            res = max(res, dp)
        return res


A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
K = 0
r = Solution().longestOnes(A, K)
print(r)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
