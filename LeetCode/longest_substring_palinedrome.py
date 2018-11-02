#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/10/24 13:04
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。

示例 2：

输入: "cbbd"
输出: "bb"
Manacher's algorithm 很厉害的啊
https://www.felix021.com/blog/read.php?2040
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def isbacktofirst(ss):
    n = len(ss)
    if n <= 0:
        return False
    mid = int(len(ss) / 2)
    i = 0
    while i <= mid:
        if ss[i] != ss[n - 1 - i]:
            return False
        else:
            i += 1
    return True


# 暴力破解法
def longestbacktofirst(s):
    n = len(s)
    print("n=", n)
    for i in range(n, 0, -1):
        j = 0
        print("i=", i)
        while j <= n - i and i + j <= n:
            ss = s[j:j + i:]
            print("i=", i, "j=", j, "ss=", ss)
            if isbacktofirst(ss):
                return ss
            j += 1
    return ""


# 自己想的稍微快一点的方法，以每一个点为基点来看看
def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s
    listdrome = []
    for i in range(n):
        if i+1 < n:
            if s[i] == s[i+1]:
                listdrome.insert(0, [i, i+1])
            if i-1 >= 0 and s[i-1] == s[i+1]:
                listdrome.append([i-1, i+1])
    res = []
    while listdrome:
        res = listdrome.pop(0)
        i, j = res[0], res[1]
        if i - 1 >= 0 and j + 1 < n and s[i-1] == s[j+1]:
            listdrome.append([i-1, j+1])
    if not res:
        return s[-1]
    else:
        return s[res[0]:res[1]+1:]


ssss = "abadd"

print(isbacktofirst(ssss))
print(longestbacktofirst(ssss))
print(longestPalindrome(ssss))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))

"""
Manacher's ALGORITHM: O(n)时间求字符串的最长回文子串 
https://www.felix021.com/blog/read.php?2040

这个 Manacher's algorithm 很厉害的啊
"""