#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/15 16:30
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :     1217. 玩筹码 显示英文描述
用户通过次数670
用户尝试次数749
通过次数681
提交次数1186
题目难度Easy
数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。

你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：

将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
将第 i 个筹码向左或者右移动 1 个单位，代价为 1。
最开始的时候，同一位置上也可能放着两个或者更多的筹码。

返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。



示例 1：

输入：chips = [1,2,3]
输出：1
解释：第二个筹码移动到位置三的代价是 1，第一个筹码移动到位置三的代价是 0，总代价为 1。
示例 2：

输入：chips = [2,2,2,3,3]
输出：2
解释：第四和第五个筹码移动到位置二的代价都是 1，所以最小总代价为 2。


提示：

1 <= chips.length <= 100
1 <= chips[i] <= 10^9
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        # 其实就是统计奇数和偶数的个数，个数少的那个就是了
        odd_num = 0
        even_num = 0
        for chip in chips:
            # 判断是不是奇数，用位运算更吊
            # if chip & 1:
            #     odd_num += 1
            if chip % 2 == 0:
                even_num += 1
            else:
                odd_num += 1
        res = odd_num if odd_num < even_num else even_num
        return res


chips = [2,2,2,3,3]
rr = Solution().minCostToMoveChips(chips)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
