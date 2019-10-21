#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/17 10:26
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   1002. 查找常用字符 显示英文描述
用户通过次数301
用户尝试次数324
通过次数303
提交次数480
题目难度Easy
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。



示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]


提示：

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母
-------------------------------------------------
"""
import time
from functools import reduce
from typing import List
import collections

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = collections.Counter(A[0])
        for i in range(1, len(A)):
            tmp = {}
            for word in A[i]:
                if tmp.setdefault(word, 0) < res.setdefault(word, 0):
                    tmp[word] = tmp.setdefault(word, 0) + 1
            res = tmp
        return sorted(reduce(lambda x, y: x + y[0] * y[1], res.items(), ""))


print("a" * 0)
aa = ["cool","lock","cook"]
print("cool".count("o"))
r = Solution().commonChars(aa)
print(r)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
