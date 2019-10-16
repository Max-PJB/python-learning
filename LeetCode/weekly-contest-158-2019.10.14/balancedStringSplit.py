#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/14 8:58
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :      5222. 分割平衡字符串 显示英文描述
用户通过次数986
用户尝试次数1042
通过次数1002
提交次数1414
题目难度Easy
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量。



示例 1：

输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
示例 2：

输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。
示例 3：

输入：s = "LLLLRRRR"
输出：1
解释：s 只能保持原样 "LLLLRRRR".


提示：

1 <= s.length <= 1000
s[i] = 'L' 或 'R'
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

import queue


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = queue.LifoQueue(1000)
        count = 0
        bottom = None

        for c in s:
            if stack.empty():
                    stack.put(c)
                    bottom = c
            else:
                if c == bottom:
                    stack.put(c)
                else:
                    stack.get()
                    if stack.empty():
                        count += 1
                        bottom = None
        return count


A_in = "LLLLRRRR"
res = Solution().balancedStringSplit(A_in)
print(res)
