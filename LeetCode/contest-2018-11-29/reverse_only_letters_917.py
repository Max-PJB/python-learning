#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/29 16:22
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  917. 仅仅反转字母

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Easy

给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。



示例 1：

输入："ab-cd"
输出："dc-ba"

示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"



提示：

    S.length <= 100
    33 <= S[i].ASCIIcode <= 122
    S 中不包含 \ or "
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        j = len(S) - 1
        i = 0
        while i < j:
            if S[i].isalpha() and S[j].isalpha():
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
            elif not S[i].isalpha():
                i += 1
            else:
                j -= 1
        return "".join(S)


S_in = "a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
res = Solution().reverseOnlyLetters(S_in)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
