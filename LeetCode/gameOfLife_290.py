#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/5/26 18:54
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


# https://leetcode-cn.com/problems/game-of-life/solution/xiong-mao-shua-ti-python3-bao-xue-bao-hui-cvzhong-/
# 下面写上代码块
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word_char = {}
        char_word = {}
        words = str.split()
        if len(pattern) != len(words):
            return False
        for p, word in zip(pattern, words):
            if word in word_char:
                if p != word_char[word]:
                    return False
            else:
                if p in char_word:
                    return False
                else:
                    char_word[p] = word
                    word_char[word] = p
        return True


pattern = "abba"
str = "dog cat cat dog"
rr = Solution().wordPattern(pattern, str)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
