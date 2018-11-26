#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/23 14:06
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  括号生成

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
-------------------------------------------------
"""
import time
import copy

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def possible(tmp, x, y):
            """
            :param tmp: str
            :param x: int
            :param y: int
            :return: None
            """
            if x == 0 and y >= 1:
                tmp += ")" * y
                res.append(tmp)
            if x == y:
                tmp += "("
                possible(tmp, x - 1, y)
            elif 0 < x < y:
                possible(tmp + "(", x - 1, y)
                possible(tmp + ")", x, y - 1)

        possible("", n, n)
        return res
        # 高手写的
        # ans = []
        # def dfs(l, r, path):
        #     if l:
        #         dfs(l-1, r, path + '(')
        #     if r > l:
        #         dfs(l, r-1, path + ')')
        #     if not r:
        #         ans.append(path)
        # dfs(n-1, n , '(')
        # return ans


n = 3
res = Solution().generateParenthesis(n)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
