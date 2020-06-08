#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/6/7 14:15
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


# 下面写上代码块
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def one_trans(a, b):
            if len(a) != len(b):
                return False
            cnt = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    cnt += 1
            if cnt == 1:
                return True
            else:
                return False

        wordList.append(beginWord)
        wordList = list(set(wordList))
        n = len(wordList)
        from collections import defaultdict
        dp = defaultdict(list)
        for i in range(n):
            word = wordList[i]
            for j in range(i + 1, n):
                word2 = wordList[j]
                if one_trans(word, word2):
                    dp[word].append(word2)
                    dp[word2].append(word)
        visited = {beginWord}
        cur_queue = [[beginWord]]
        res = []
        print(dp)
        flag = False
        while not flag and cur_queue:
            tmp_que = []
            while cur_queue:
                print(cur_queue)
                path = cur_queue.pop()
                print('->', path)
                last_node = path[-1]
                visited.add(last_node)
                print(last_node, ':', dp[last_node])
                if dp[last_node]:
                    for word in dp[last_node]:
                        if word == endWord:
                            res.append(path + [word])
                            flag = True
                        elif word not in visited:
                            tmp_que.append(path + [word])
            cur_queue = tmp_que
        return res


beginWord = "red"
endWord = "tax"
wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
rr = Solution().findLadders(beginWord, endWord, wordList)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
