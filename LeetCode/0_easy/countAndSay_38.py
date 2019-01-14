#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/1/14 16:10
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       38. 报数
    报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。



示例 1:

输入: 1
输出: "1"

示例 2:

输入: 4
输出: "1211"
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def next_1(ss):
            """
            :param ss:str
            :return:
            """
            ls = ss[0]
            cnt = 0
            r = ""
            for i in ss:
                if i != ls:
                    r += str(cnt) + ls
                    ls = i
                    cnt = 1
                else:
                    cnt += 1
            r += str(cnt) + ls
            return r

        j = 1
        rr = "1"
        while j < n:
            rr = next_1(rr)
            j += 1
        return rr


res = Solution().countAndSay(8)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
