#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/10 21:33
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 843. 猜猜这个单词

    用户通过次数 2
    用户尝试次数 12
    通过次数 2
    提交次数 32
    题目难度 Hard

这个问题是 LeetCode 平台新增的交互式问题 。

我们给出了一个由一些独特的单词组成的单词列表，每个单词都是 6 个字母长，并且这个列表中的一个单词将被选作秘密。

你可以调用 master.guess(word) 来猜单词。你所猜的单词应当是存在于原列表并且由 6 个小写字母组成的类型字符串。

此函数将会返回一个整型数字，表示你的猜测与秘密单词的准确匹配（值和位置同时匹配）的数目。此外，如果你的猜测不在给定的单词列表中，它将返回 -1。

对于每个测试用例，你有 10 次机会来猜出这个单词。当所有调用都结束时，如果您对 master.guess 的调用不超过 10 次，并且至少有一次猜到秘密，那么您将通过该测试用例。

除了下面示例给出的测试用例外，还会有 5 个额外的测试用例，每个单词列表中将会有 100 个单词。这些测试用例中的每个单词的字母都是从 'a' 到 'z' 中随机选取的，并且保证给定单词列表中的每个单词都是唯一的。

示例 1:
输入: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

解释:

master.guess("aaaaaa") 返回 -1, 因为 "aaaaaa" 不在 wordlist 中.
master.guess("acckzz") 返回 6, 因为 "acckzz" 就是秘密，6个字母完全匹配。
master.guess("ccbazz") 返回 3, 因为 "ccbazz" 有 3 个匹配项。
master.guess("eiowzz") 返回 2, 因为 "eiowzz" 有 2 个匹配项。
master.guess("abcczz") 返回 4, 因为 "abcczz" 有 4 个匹配项。

我们调用了 5 次master.guess，其中一次猜到了秘密，所以我们通过了这个测试用例。

提示：任何试图绕过评判的解决方案都将导致比赛资格被取消。
-------------------------------------------------
"""
import time
import random

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master(object):
    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        # sec = "hbaczn"
        sec = "ccoyyo"
        cnt = 0
        for i, j in zip(word, sec):
            if i == j:
                cnt += 1
        if cnt == 0:
            return -1
        else:
            return cnt


class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        挺有意思的一道题，不知道该怎么形容做法。
        既然所有字符串都是随机生成，所以你肯定要盲猜一下，
        第一次先随机选一个字符串然后利用接口函数得出当前字符串和正确字符串的接近个数num,
        然后筛选wordlist列表里与字符串匹配个数为num的字符串，
        通过十次循环，最终得出要猜的字符串。
        """

        # 判断一个单词和另一个单词是否只有 k 个字母一样
        def judge_different(a, b, k):
            """
            :param a:str
            :param b: str
            :param k: int
            :return: bool
            """
            # return sum([a == b for a, b in zip(aa, bb)])
            cnt = 0
            for i, j in zip(a, b):
                if i == j:
                    cnt += 1
            if cnt == k:
                return True
            else:
                return False

        cnt = 0
        times = 0
        while cnt != 6:
            test = wordlist[random.randint(0,len(wordlist)-1)]
            cnt = master.guess(test)
            if cnt == -1:
                cnt = 0
            wordlist = list(filter(lambda x: judge_different(x, test, cnt), wordlist))
            times += 1
        return cnt, times

        # 下面是我做的，有点慢，可以通过筛选来做嘛
        # print(judge_different("hbaczn", "hbaczn", 1))
        # fail_list = []
        # test = wordlist[0]
        # res = master.guess(test)
        # times = 1
        # while res != 6:
        #     times += 1
        #     res = 0 if res == -1 else res
        #     fail_list.append((test, res))
        #     for word in wordlist:
        #         flag = 1
        #         for fail in fail_list:
        #             print(word, fail[0], fail[1], judge_different(word, fail[0], fail[1]))
        #             if not judge_different(word, fail[0], fail[1]):
        #                 flag = 0
        #                 break
        #         if flag:
        #             test = word
        #             res = master.guess(test)
        #             print("1111111111", res, test)
        #             break
        # return res, times


sec = "hbaczn"
words = ["gaxckt", "trlccr", "jxwhkz", "ycbfps", "peayuf", "yiejjw", "ldzccp", "nqsjoa", "qrjasy", "pcldos", "acrtag",
         "buyeia", "ubmtpj", "drtclz", "zqderp", "snywek", "caoztp", "ibpghw", "evtkhl", "bhpfla", "ymqhxk", "qkvipb",
         "tvmued", "rvbass", "axeasm", "qolsjg", "roswcb", "vdjgxx", "bugbyv", "zipjpc", "tamszl", "osdifo", "dvxlxm",
         "iwmyfb", "wmnwhe", "hslnop", "nkrfwn", "puvgve", "rqsqpq", "jwoswl", "tittgf", "evqsqe", "aishiv", "pmwovj",
         "sorbte", "hbaczn", "coifed", "hrctvp", "vkytbw", "dizcxz", "arabol", "uywurk", "ppywdo", "resfls", "tmoliy",
         "etriev", "oanvlx", "wcsnzy", "loufkw", "onnwcy", "novblw", "mtxgwe", "rgrdbt", "ckolob", "kxnflb", "phonmg",
         "egcdab", "cykndr", "lkzobv", "ifwmwp", "jqmbib", "mypnvf", "lnrgnj", "clijwa", "kiioqr", "syzebr", "rqsmhg",
         "sczjmz", "hsdjfp", "mjcgvm", "ajotcx", "olgnfv", "mjyjxj", "wzgbmg", "lpcnbj", "yjjlwn", "blrogv", "bdplzs",
         "oxblph", "twejel", "rupapy", "euwrrz", "apiqzu", "ydcroj", "ldvzgq", "zailgu", "xgqpsr", "wxdyho", "alrplq",
         "brklfk"]
sec2 = "ccoyyo"
words2 = ["wichbx", "oahwep", "tpulot", "eqznzs", "vvmplb", "eywinm", "dqefpt", "kmjmxr", "ihkovg", "trbzyb", "xqulhc",
          "bcsbfw", "rwzslk", "abpjhw", "mpubps", "viyzbc", "kodlta", "ckfzjh", "phuepp", "rokoro", "nxcwmo", "awvqlr",
          "uooeon", "hhfuzz", "sajxgr", "oxgaix", "fnugyu", "lkxwru", "mhtrvb", "xxonmg", "tqxlbr", "euxtzg", "tjwvad",
          "uslult", "rtjosi", "hsygda", "vyuica", "mbnagm", "uinqur", "pikenp", "szgupv", "qpxmsw", "vunxdn", "jahhfn",
          "kmbeok", "biywow", "yvgwho", "hwzodo", "loffxk", "xavzqd", "vwzpfe", "uairjw", "itufkt", "kaklud", "jjinfa",
          "kqbttl", "zocgux", "ucwjig", "meesxb", "uysfyc", "kdfvtw", "vizxrv", "rpbdjh", "wynohw", "lhqxvx", "kaadty",
          "dxxwut", "vjtskm", "yrdswc", "byzjxm", "jeomdc", "saevda", "himevi", "ydltnu", "wrrpoc", "khuopg", "ooxarg",
          "vcvfry", "thaawc", "bssybb", "ccoyyo", "ajcwbj", "arwfnl", "nafmtm", "xoaumd", "vbejda", "kaefne", "swcrkh",
          "reeyhj", "vmcwaf", "chxitv", "qkwjna", "vklpkp", "xfnayl", "ktgmfn", "xrmzzm", "fgtuki", "zcffuv", "srxuus",
          "pydgmq"]
res = Solution().findSecretWord(words2, Master())
print(res)

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
