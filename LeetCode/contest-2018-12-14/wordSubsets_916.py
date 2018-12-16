#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/14 14:27
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  916. 单词子集

    虚拟 用户通过次数 39
    虚拟 用户尝试次数 76
    虚拟 通过次数 39
    虚拟 提交次数 76
    题目难度 Medium

我们给出两个单词数组 A 和 B。每个单词都是一串小写字母。

现在，如果 b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称单词 b 是单词 a 的子集。 例如，“wrr” 是 “warrior” 的子集，但不是 “world” 的子集。

如果对 B 中的每一个单词 b，b 都是 a 的子集，那么我们称 A 中的单词 a 是通用的。

你可以按任意顺序以列表形式返回 A 中所有的通用单词。



示例 1：

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
输出：["facebook","google","leetcode"]

示例 2：

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
输出：["apple","google","leetcode"]

示例 3：

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
输出：["facebook","google"]

示例 4：

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
输出：["google","leetcode"]

示例 5：

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
输出：["facebook","leetcode"]



提示：

    1 <= A.length, B.length <= 10000
    1 <= A[i].length, B[i].length <= 10
    A[i] 和 B[i] 只由小写字母组成。
    A[i] 中所有的单词都是独一无二的，也就是说不存在 i != j 使得 A[i] == A[j]。
-------------------------------------------------
"""
import time
import collections

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        A_dic = collections.defaultdict(collections.Counter)
        for i in A:
            A_dic[i] = collections.Counter(i)
        # print(A_dic)
        B_dic = collections.defaultdict(int)
        for b in B:
            b_count = collections.Counter(b)
            for k, v in b_count.items():
                if B_dic[k] < v:
                    B_dic[k] = v
        # print(B_dic)
        ans = []
        for word, chars in A_dic.items():
            flag = 1
            for k, v in B_dic.items():
                if chars[k] < v:
                    flag = 0
                    break
            if flag:
                ans.append(word)
        return ans


A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["ec", "oc","ceo"]
res = Solution().wordSubsets(A, B)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
