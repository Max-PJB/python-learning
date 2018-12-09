#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/9 15:12
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  948. 令牌放置

    用户通过次数 49
    用户尝试次数 77
    通过次数 51
    提交次数 247
    题目难度 Medium

你的初始能量为 P，初始分数为 0，只有一包令牌。

令牌的值为 token[i]，每个令牌最多只能使用一次，可能的两种使用方法如下：

    如果你至少有 token[i] 点能量，可以将令牌置为正面朝上，失去 token[i] 点能量，并得到 1 分。
    如果我们至少有 1 分，可以将令牌置为反面朝上，获得 token[i] 点能量，并失去 1 分。

在使用任意数量的令牌后，返回我们可以得到的最大分数。



示例 1：

输入：tokens = [100], P = 50
输出：0

示例 2：

输入：tokens = [100,200], P = 150
输出：1

示例 3：

输入：tokens = [100,200,300,400], P = 200
输出：2



提示：

    tokens.length <= 1000
    0 <= tokens[i] < 10000
    0 <= P < 10000
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        # sum(up) <= P + sum(down) 求 max(up - down)
        # 做错了，不想删除，没有考虑到要求最少有一分
        # if not tokens:
        #     return 0
        # n = len(tokens)
        # tokens.sort()
        # tokens.append(P)
        # up = 0
        # down = n
        # up_energe = 0
        # down_energe = 0
        # while up < down:
        #     if up_energe < down_energe:
        #         print("zzzzz",up)
        #         up_energe += tokens[up]
        #         up += 1
        #     else:
        #         print("yyyyy",down)
        #         down_energe += tokens[down]
        #         down -= 1
        # print(up,up_energe,down,down_energe)
        # if up_energe + tokens[up] > down_energe:
        #     # 表示这个点不能向上翻，向下翻转也没有意思，没有更多的牌了，所以这个点就不管他
        #     up -= 1
        # if up_energe > down_energe:
        #     down -= 1
        # return up + 2 - n + down

        tokens.sort()
        j = len(tokens) - 1
        i = 0
        res = 0
        cur = 0
        while i <= j:
            if P >= tokens[i]:
                cur += 1
                P -= tokens[i]
                res = max(res, cur)
                print(res)
                i += 1
            elif cur > 0:
                P += tokens[j]
                j -= 1
                cur -= 1
            else:
                break
        return res
        # ---------------------
        # 作者：_威行天下_
        # 来源：CSDN
        # 原文：https: // blog.csdn.net / koukehui0292 / article / details / 84495909
        # 版权声明：本文为博主原创文章，转载请附上博文链接！


tokens_in = [71, 55, 82]
P = 54
res = Solution().bagOfTokensScore(tokens_in, P)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
