#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/6 13:47
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  856. 括号的分数

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Medium

给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

    () 得 1 分。
    AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
    (A) 得 2 * A 分，其中 A 是平衡括号字符串。



示例 1：

输入： "()"
输出： 1

示例 2：

输入： "(())"
输出： 2

示例 3：

输入： "()()"
输出： 2

示例 4：

输入： "(()(()))"
输出： 6



提示：

    S 是平衡括号字符串，且只含有 ( 和 ) 。
    2 <= S.length <= 50
-------------------------------------------------
"""
import time
import re

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """

        def jie_kai(sss):
            """
            :param sss: List[str]
            :return: int
            """
            if len(sss) == 2:
                return 1
            stack = []
            ls = []
            do_next = []
            for i in sss:
                ls.append(i)
                if i == "(":
                    stack.append(i)
                else:
                    # i == ")"
                    stack.pop()
                if not stack:
                    do_next.append(ls)
                    ls = []
            jie_guo = 0
            if len(do_next) == 1:
                jie_guo += jie_kai(2 * do_next[0][1:len(do_next[0]) - 1:])
            else:
                for mei_ge in do_next:
                    jie_guo += jie_kai(mei_ge)
            return jie_guo

        return jie_kai(S)

    # 感受一下高手的力量
    def scoreOfParentheses2(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                score = 0
                while True:
                    t = stack.pop()
                    if t == '(':
                        if score == 0:
                            stack.append(1)
                        else:
                            stack.append(score * 2)
                        break
                    else:
                        score += t
                    if not stack:
                        return score
        return sum(stack)


s = "(()(()))"
res = Solution().scoreOfParentheses(s)
print(s)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
