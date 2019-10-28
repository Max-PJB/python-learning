#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/28 15:15
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       966. 元音拼写检查器
    提示：

    1 <= wordlist.length <= 5000
    1 <= queries.length <= 5000
    1 <= wordlist[i].length <= 7
    1 <= queries[i].length <= 7
    wordlist 和 queries 中的所有字符串仅由英文字母组成。

-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        思路与算法
        我们分析了算法需要考虑的 3 种情况: 当查询完全匹配时，当查询存在大小写不同的单词匹配时，当查询与出现元音错误的单词匹配时。
        在所有 3 种情况下，我们都可以使用哈希表来查询答案。
        对于第一种情况（完全匹配），我们使用集合存放单词以有效地测试查询单词是否在该组中。
        对于第二种情况（大小写不同），我们使用一个哈希表，该哈希表将单词从其小写形式转换为原始单词（大小写正确的形式）。
        对于第三种情况（元音错误），我们使用一个哈希表，将单词从其小写形式（忽略元音的情况下）转换为原始单词。
        """
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return list(map(solve, queries))


"""        
我写的，错了，但是思路是对的，只是太想一顿操作解决了。没有别人写的思路清晰
# 先搞一个单词的字典嘛，这种东西要速度肯定是要字典来搞的
        from collections import defaultdict
        word_dict = defaultdict(list)
        for word in wordlist:
            word_dict[word.lower()] = word_dict.get(word.lower(), []) + [word]

        # print(word_dict)
        # print(queries)
        res = []
        for query in queries:
            # 如果字典中有这个单词的小写的键，说明一定存在
            if query.lower() in word_dict:
                # 看这个单词本身在不在，不在的话就取第一个
                if query in word_dict[query.lower()]:
                    res.append(query)
                else:
                    res.append(word_dict[query.lower()][0])
            # 如果没有这个单词的键，那就要考虑变换元音了
            else:
                #  这个时候就要找元音了，找到了后搞个 笛卡尔积 有放回的排列
                vowels = ['a', 'e', 'i', 'o', 'u']
                # query 这个单词中含有元音的字符在单词中的位置
                vowel_index = [index for index, ch in enumerate(query.lower()) if ch in vowels]
                # 有元音字符
                if len(vowel_index) > 0:
                    import itertools
                    flag = False
                    # 笛卡尔排列，拿出来又放回去
                    product = itertools.product(vowels, repeat=len(vowel_index))
                    for permutation in product:
                        tmp = list(query)
                        for index, permu in zip(vowel_index, permutation):
                            tmp[index] = permu
                        new_word = "".join(tmp)
                        # print(query,new_word)
                        if new_word in word_dict:
                            res.append(word_dict[new_word][0])
                            flag = True
                            break
                    if not flag:
                        res.append("")
                # 没有元音字符，那就是字典中没有答案
                else:
                    res.append("")

        return res"""

wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
rrr = Solution().spellchecker(["ae", "aa"], ["UU"])
# rrr = Solution().spellchecker(wordlist, queries)
print(rrr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
