#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/30 18:43
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  920. 播放列表的数量

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Hard

你的音乐播放器里有 N 首不同的歌，在旅途中，你的旅伴想要听 L 首歌（不一定不同，即，允许歌曲重复）。请你为她按如下规则创建一个播放列表：

    每首歌至少播放一次。
    一首歌只有在其他 K 首歌播放完之后才能再次播放。

返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回它模 10^9 + 7 的结果。



示例 1：

输入：N = 3, L = 3, K = 1
输出：6
解释：有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2, 1].

示例 2：

输入：N = 2, L = 3, K = 0
输出：6
解释：有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2]

示例 3：

输入：N = 2, L = 3, K = 1
输出：2
解释：有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2]



提示：

    0 <= K < N <= L <= 100
-------------------------------------------------
"""
import time
import itertools
import math

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    """
    # # 写了5个小时，写不出来，不忍心删掉，留着纪念吧！~~
    # def numMusicPlaylists(self, N, L, K):
    #
    #     # 排列
    #     def permute(total, x):
    #         if total < x or total < 0:
    #             return False
    #         sis = 1
    #         for xx in range(x):
    #             sis *= (total - xx)
    #         return sis
    #
    #     # 组合
    #     def combine(total, x):
    #         if total < x:
    #             return False
    #         return math.factorial(total) // math.factorial(x) // math.factorial(total - x)
    #
    #     if N == L or N == K+1:
    #         return int(permute(N, N) % (math.pow(10, 9) + 7))
    #     res = 1
    #     # 从 N 首歌中挑出 K+1 首的情况，放在前 K+1 首歌的情况，属于组合
    #     # qingkuang1 = len(list(itertools.permutations(range(N), K + 1)))
    #     qingkuang1 = permute(N, K + 1)
    #     print("从N=", N, "个数中挑出 K+1=", K + 1, " 个数的放在前 K+1 首歌的情况", qingkuang1)
    #     res *= qingkuang1
    #     # 后面还需要挑选 L-K-1 首歌，但是其中还有 N-K-1 首歌一次都没有播放过
    #     ls = 0
    #     for i in range(N - K):
    #         # qk = (N - K - i) ** (L - K - 1) * len(list(itertools.combinations(range(N - K - 1), i)))
    #         qk = math.pow((N - K - i)*(K+1), L - K - 1) * combine(N - K - 1, i)
    #         print(i, "情况", qk)
    #         ls += qk * math.pow(-1, i)
    #     res *= ls
    #     return int(res % (math.pow(10, 9) + 7))
    """

    # 大神的动态规划思路，牛逼啊.注意，顺序是从前往后，不是从后往前。从后往前就要出错
    # F(N,L,K) = F(N - 1, L - 1, K) * N + F(N, L - 1, K) * (N - K)
    #
    # F(N - 1, L - 1, K)
    # If only N - 1 in the L - 1 first songs.
    # We need to put the rest one at the end of music list.
    # Any song can be this last song, so there are N possible combinations.
    #
    # F(N, L - 1, K)
    # If already N in the L - 1 first songs.
    # We can put any song at the end of music list,
    # but it should be different from K last song.
    # We have N - K choices.
    #
    # Time Complexity:
    # O((L-K)(N-K))
    def numMusicPlaylists2(self, N, L, K):
        dp = [[0 for i in range(L + 1)] for j in range(N + 1)]
        for i in range(K + 1, N + 1):
            for j in range(i, L + 1):
                if i == j or i == K + 1:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - K)
        return dp[N][L] % (10 ** 9 + 7)


res2 = Solution().numMusicPlaylists2(25, 28, 5)
print(res2)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
