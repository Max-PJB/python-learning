#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/26 19:53
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 890. 查找和替换模式

    虚拟 用户通过次数 27
    虚拟 用户尝试次数 30
    虚拟 通过次数 27
    虚拟 提交次数 30
    题目难度 Medium

你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。

如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。

（回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）

返回 words 中与给定模式匹配的单词列表。

你可以按任何顺序返回答案。



示例：

输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
输出：["mee","aqq"]
解释：
"mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
"ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
因为 a 和 b 映射到同一个字母。



提示：

    1 <= words.length <= 50
    1 <= pattern.length = words[i].length <= 20
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        def word_to_pattern(word):
            """
            :param word: Str
            :return: List[int]
            """
            if not word:
                return False
            ls = []
            tmp = {word[0]: 0}
            for i in word:
                if i in tmp.keys():
                    ls.append(tmp[i])
                else:
                    k = max(ls) + 1
                    ls.append(k)
                    tmp[i] = k
            return ls

        pat = word_to_pattern(pattern)
        res = []
        for j in words:
            if word_to_pattern(j) == pat:
                res.append(j)
        return res


# 别人的方法
class Solution2(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        def P(words):
            dict = {}
            for w in words:
                dict[w] = dict.get(w, len(dict))
            return "".join([str(dict[w]) for w in words])

        return [word for word in words if P(word) == P(pattern)]


words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
res = Solution().findAndReplacePattern(words, pattern)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
