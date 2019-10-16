#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/15 21:30
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  1220. 统计元音字母序列的数目 显示英文描述
用户通过次数222
用户尝试次数275
通过次数227
提交次数432
题目难度Hard
给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：

字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
每个元音 'a' 后面都只能跟着 'e'
每个元音 'e' 后面只能跟着 'a' 或者是 'i'
每个元音 'i' 后面 不能 再跟着另一个 'i'
每个元音 'o' 后面只能跟着 'i' 或者是 'u'
每个元音 'u' 后面只能跟着 'a'
由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。



示例 1：

输入：n = 1
输出：5
解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
示例 2：

输入：n = 2
输出：10
解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
示例 3：

输入：n = 5
输出：68


提示：

1 <= n <= 2 * 10^4
-------------------------------------------------
"""
import collections
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        print(MOD)
        pre = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        tmp = {}
        for _ in range(1, n):
            tmp["a"] = pre["e"] % MOD
            tmp["e"] = (pre["a"] + pre["i"]) % MOD
            tmp["i"] = (pre["a"] + pre["u"] + pre["e"] + pre["o"]) % MOD
            tmp["o"] = (pre["i"] + pre["u"]) % MOD
            tmp["u"] = pre["a"] % MOD
            print(pre,tmp)
            pre = tmp.copy()

        return sum(pre.values()) % MOD


n = 144
res = Solution().countVowelPermutation(n)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
