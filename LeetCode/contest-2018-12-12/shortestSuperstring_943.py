#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/12 11:50
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 943. 最短超级串

    虚拟 用户通过次数 1
    虚拟 用户尝试次数 5
    虚拟 通过次数 1
    虚拟 提交次数 5
    题目难度 Hard

给定一个字符串数组 A，找到以 A 中每个字符串作为子字符串的最短字符串。

我们可以假设 A 中没有字符串是 A 中另一个字符串的子字符串。



示例 1：

输入：["alex","loves","leetcode"]
输出："alexlovesleetcode"
解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。

示例 2：

输入：["catg","ctaagt","gcta","ttca","atgcatc"]
输出："gctaagttcatgcatc"



提示：

    1 <= A.length <= 12
    1 <= A[i].length <= 20
-------------------------------------------------
"""
import time
import re

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """

        # s1后面连接s2后，会变成什么样，有多少个字符重复
        def max_similar(s1, s2):
            """
            :param s1:str
            :param s2: str
            :return:
            """
            # 保证 s1 长度 < s2 (n<m)
            n = len(s1)
            m = len(s2)
            if n > m:
                n, m = m, n
                s1, s2 = s2, s1
            max_overlap = 0
            over_lap = s1 + s2
            if s1 in s2:
                max_overlap = n
                over_lap = s2
            else:
                for i in range(n + 1):
                    if s1.endswith(s2[:i:]):
                        if max_overlap < i:
                            max_overlap = i
                            over_lap = s1 + s2[i::]
                for i in range(n + 1):
                    if s2.endswith(s1[:i:]):
                        if max_overlap < i:
                            max_overlap = i
                            over_lap = s2 + s1[i::]

            return max_overlap, over_lap

        A.sort(key=lambda x:len(x))
        n = len(A)
        while n != 1:
            p, q = -1, -1
            new_str = ""
            max_len = -1
            for i in range(n):
                for j in range(i + 1, n):
                    over_lap_len, overlap = max_similar(A[i], A[j])
                    if over_lap_len > max_len:
                        p, q = i, j
                        new_str = overlap
                        max_len = over_lap_len
            n -= 1
            A[p] = new_str
            A.pop(q)
            A.sort(key=lambda x: len(x))
            print(A)
        # print(A)
        return A[0]


a_in = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
a_in2 = ["ift","efd","dnete","tef","fdn"]
res = Solution().shortestSuperstring(a_in2)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))