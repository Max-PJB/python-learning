#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/23 16:19
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :     1048. 最长字符串链 显示英文描述
用户通过次数105
用户尝试次数226
通过次数108
提交次数834
题目难度Medium
给出一个单词列表，其中每个单词都由小写英文字母组成。

如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac" 的前身。

词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。

从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。


示例：

输入：["a","b","ba","bca","bda","bdca"]
输出：4
解释：最长单词链之一为 "a","ba","bda","bdca"。


提示：

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] 仅由小写英文字母组成。
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
    def longestStrChain(self, words: List[str]) -> int:
        d = {}
        words.sort(key=len)
        for word in words:
            if word not in d:
                d[word]=1
                for i in range(len(word)):
                    if word[:i]+word[i+1:] in d:
                        d[word]+=d[word[:i]+word[i+1:]]
                        break

        return max(d.values())
        """
        # 判断 b 是不是 a 的父字符
        def isFather(a, b):
            i, j = 0, 0
            while j < len(b) and i < len(a):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    break
            while j < len(b) and i < len(a):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    return False
            return i == len(a)

        # 长度最多16，把他分成17组，0组就一直是空吧，不考虑
        wl = [[] for _ in range(18)]  # wl[i] = [] 表示 单词长度是 i 的 单词组成的数组 按长度分组,17 也要加，为空代表没有更大的了
        for word in words:
            wl[len(word)].append(word)
        words.sort(key=lambda x: len(x), reverse=True)
        print(wl)
        print(words)
        dp = {}
        for word in words:
            word_length = len(word)
            # 查找当前字段的长度 + 1，就是看有没有比他长度多一个字母的，没有的话，那他就是一个字符串链的最后一个字符了
            if not wl[word_length + 1]:  # 不存在 +1 长度的字符，最后一个，那就是以他开头的话字符串链最大是 1
                dp[word] = 1
            else:
                # 存在长度比他大 1 的字符，那遍历这些字符，看看是不是他的父链，是的话塞入 fater_words 列表中
                father_words = []
                for longer_word in wl[word_length + 1]:
                    if isFather(word, longer_word):
                        father_words.append(longer_word)
                dp[word] = max(map(lambda father_word: dp[father_word] + 1, father_words), default=1)

        return max(dp.values())


aa = ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj", "ksqvsq",
      "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]
res = Solution().longestStrChain(aa)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))

