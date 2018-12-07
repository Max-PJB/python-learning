#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/4 15:07
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   828. 独特字符串

    用户通过次数 0
    用户尝试次数 4
    通过次数 0
    提交次数 12
    题目难度 Hard

如果一个字符在字符串 S 中有且仅有出现一次，那么我们称其为独特字符。

例如，在字符串 S = "LETTER" 中，"L" 和 "R" 可以被称为独特字符。

我们再定义 UNIQ(S) 作为字符串 S 中独特字符的个数。

那么，在 S = "LETTER" 中， UNIQ("LETTER") =  2。

对于给定字符串 S，计算其所有非空子串的独特字符的个数，即 UNIQ(substring)。

如果出现两个或者多个相同的子串，将其认为是不同的两个子串。

考虑到答案可能会非常大，规定返回格式为：结果 mod 10 ^ 9 + 7。

示例 1:

输入: "ABC"
输出: 10
解释: 所有可能的子串为："A","B","C","AB","BC" 和 "ABC"。
     其中，每一个子串都由独特字符构成。
     所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10

示例 2:

输入: "ABA"
输出: 8
解释: 除了子串 UNIQ('ABA') = 1，其余与示例1相同。

说明: 0 <= S.length <= 10000。
-------------------------------------------------
"""
import time
import re

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int

        算法
(答案转换) O(n)

    预处理每个位置 i，左边第一个和自己一样字符的位置 left，右边第一个和自己一样字符的位置 right。
    该位置 i 贡献的答案就是 (i - left) * (right - i)。
    对每个位置进行统计。

时间复杂度

    预处理的时间复杂度为 O(n)

；每个位置常数时间统计，故总时间复杂度为 O(n)。
  # 出现相同子串也被认为是不同子串，则所有的子串都可以用一组下标 [i, j] 完全确定
        # i, j 满足条件，0 ≤ i ≤ j ≤ N-1，N 为 S 的长度。因此共有 N(N-1)(N+4)/6 个子串
        # 若对每个子串遍历求解，则至少是 O(N^3) 的时间复杂度
        #
        # 转换一下思路，每个字符在哪些子串中是独特字符，求出这样的子串数目
        # 对所有字符做这样的运算，并将结果求和即为最终答案

        # 因为是独特字符，所以所有满足要求的子串中仅出现这个字符一次
        # 若字符在整个字符串中出现不止一次，就需要知道每次出现的位置，从而限制可能的子串的最大长度

        # 比如字符 'a'，在 S 中出现的位置有，[...i1...i2...i3...]
        # 则遍历到 i2 处时，所有可能的子串 [i,j]，满足条件 i1 < i ≤ i2 ≤ j < i3
        # 因此这样的子串共有 (i2 - i1)(i3 - i2) 个
        # 考虑边界情况，左侧有 (i1 + 1)(i2 - i1)，右侧有 (in - in-1)(n - in)
        """
        N = len(S)
        words_dict = {chr(i): [] for i in range(65, 91)}
        # print("1111", words_dict)
        for i, s in enumerate(S):
            words_dict[s] = (words_dict[s] + [i])
        # print("2222", words_dict)
        res = 0
        for words in words_dict.values():
            if words:
                words = [-1] + words + [N]
                # print("33333", words)
                for i in range(1, len(words) - 1):
                    left = words[i - 1]
                    right = words[i + 1]
                    res += (words[i] - left) * (right - words[i])
                    # print("i=", i, "left=", left, "right=", right, "res+=", res)
        return res


S_in = "ABC"
res = Solution().uniqueLetterString(S_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
