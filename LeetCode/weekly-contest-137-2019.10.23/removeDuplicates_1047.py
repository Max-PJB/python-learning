#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/23 14:18
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :     1047. 删除字符串中的所有相邻重复项 显示英文描述
用户通过次数398
用户尝试次数455
通过次数400
提交次数964
题目难度Easy
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。



示例：

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。


提示：

1 <= S.length <= 20000
S 仅由小写英文字母组成。
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) == 1:
            return S
        res = []
        i = 0
        while i < len(S):
            if res and S[i] == res[-1]:
                tmp = res.pop()
                while i < len(S) and S[i] == tmp:
                    i += 1
            else:
                res.append(S[i])
                i += 1

        return "".join(res)


a = "aaaaaacccc"
res = Solution().removeDuplicates(a)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
