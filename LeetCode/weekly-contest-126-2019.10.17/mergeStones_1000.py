#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/17 16:07
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 1000. 合并石头的最低成本 显示英文描述
用户通过次数8
用户尝试次数69
通过次数8
提交次数160
题目难度Hard
有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。

每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。

找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。



示例 1：

输入：stones = [3,2,4,1], K = 2
输出：20
解释：
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。
示例 2：

输入：stones = [3,2,4,1], K = 3
输出：-1
解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
示例 3：

输入：stones = [3,5,1,2,6], K = 3
输出：25
解释：
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。


提示：

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()

"""
首先我们定义dp(i,j,k)表示把数组的i到j这个子数组分成k个部分，每个部分合成为1个块的最小成本
显然我们要求的是dp(1,n,1)

可以这样想 一个i到j的数组 合成一份 一定是先分成k份 再把这k份合起来，也就是加上从i到j的和sum(i,j),而分成k份有很多种分法 显然我们要求最小的那种分法
也就是：
dp(i,j,1)=min{dp(i,j,k)}+sum(i,j)

而要分成k分 就从i到j之间找一个t 把i到t分成k-1份 再把t+1到j合成一份,递归计算两边要合并的值为多少，再加起来
所以我们考虑每个t 看哪一个t使得两边合并的成本再加起来是最小的 就取这个t
也就是：
dp(i,j,k)=min{dp(i,t,k-1)+dp(t+1,j,1)|t from i to j-1}

合并一下用递推表达式表示就是：
dp(i,j,k)=min{dp(i,t,k-1)+dp(t+1,j,1)|t from i to j-1}
dp(i,j,1)=dp(i,j,k)+sum(i,j)

初始条件是
dp(i,i,1)=0 只有一个的时候是不需要合并的
dp(i,i+k-1,1)=sum(i,i+k-1) 这个很显然
注意如果一开始的n-1一定是要可以整除k-1 不然分不了 其他情况都可以分出来 这个可以自己模拟下就知道了

"""


# 下面写上代码块
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        length = len(stones)
        if length == 1:
            return 0
        x, y = divmod(length, K)
        z = x + y
        while x != 0:
            x, y = divmod(z, K)
            z = x + y
        if y != 1:
            return -1
        global res
        res = 0
        # TODO 上面有解析，能不能自己撸一下代码
        return res


stones = [3, 2, 4, 1]
K = 4
res = Solution().mergeStones(stones, K)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
