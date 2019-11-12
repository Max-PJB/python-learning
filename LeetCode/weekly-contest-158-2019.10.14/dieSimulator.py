#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/14 10:10
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 5224. 掷骰子模拟 显示英文描述
用户通过次数126
用户尝试次数270
通过次数128
提交次数488
题目难度Medium
有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。

不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。

现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。

假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。



示例 1：

输入：n = 2, rollMax = [1,1,2,2,2,3]
输出：34
解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。
示例 2：

输入：n = 2, rollMax = [1,1,1,1,1,1]
输出：30
示例 3：

输入：n = 3, rollMax = [1,1,1,2,2,3]
输出：181


提示：

1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # todo https://leetcode-cn.com/contest/weekly-contest-158/problems/dice-roll-simulation/
        # 用 dp[i][j][k] 表示第 i 轮掷骰子掷出数字 j 时 j 连续出现 k 次的组合数量。
        dp = [[1 if j == 0 else 0 for j in range(rollMax[i])] for i in range(6)]
        i = 1
        M = 10**9 + 7
        # print(dp, sum(map(sum, dp)))
        while i < n:
            tmp = [[0 for j in range(rollMax[i])] for i in range(6)]
            sum_pre = sum(map(sum, dp))
            for k in range(6):
                for l in range(rollMax[k]):
                    if l == 0:
                        tmp[k][l] = sum_pre - sum(dp[k])
                    else:
                        tmp[k][l] = dp[k][l - 1]
            dp = tmp
            i += 1
        return sum(map(sum, dp)) % M

n = 20
roll = [8,5,10,8,7,2]
res = Solution().dieSimulator(n, roll)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
