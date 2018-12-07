#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/6 19:21
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  857. 雇佣 K 名工人的最低成本

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Hard

有 N 名工人。 第 i 名工人的工作质量为 quality[i] ，其最低期望工资为 wage[i] 。

现在我们想雇佣 K 名工人组成一个工资组。在雇佣 一组 K 名工人时，我们必须按照下述规则向他们支付工资：

    对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。
    工资组中的每名工人至少应当得到他们的最低期望工资。

返回组成一个满足上述条件的工资组至少需要多少钱。



示例 1：

输入： quality = [10,20,5], wage = [70,50,30], K = 2
输出： 105.00000
解释： 我们向 0 号工人支付 70，向 2 号工人支付 35。

示例 2：

输入： quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
输出： 30.66667
解释： 我们向 0 号工人支付 4，向 2 号和 3 号分别支付 13.33333。



提示：

    1 <= K <= N <= 10000，其中 N = quality.length = wage.length
    1 <= quality[i] <= 10000
    1 <= wage[i] <= 10000
    与正确答案误差在 10^-5 之内的答案将被视为正确的。
-------------------------------------------------
"""
import time
import bisect

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        n = len(quality)
        rate = list(map(lambda x, y, z: (y / x, z, x), quality, wage, range(n)))
        rate.sort()
        print(rate)
        r = 10 ** 9
        rr = []
        start = K - 1
        smallest = []
        for i in range(K - 1):
            smallest.append(rate[i][2])
        smallest.sort()
        # print(smallest)
        while start < n:
            ls = smallest[:K - 1:]
            cur = rate[start][2]
            print("r============", rate[start][0], rate[start][2], ls,
                  sum(ls))
            all_sum = rate[start][0] * sum(ls) + rate[start][0] * rate[start][2]
            ls.append(cur)
            rr.append(ls)
            print("all_sum", all_sum)
            r = all_sum if all_sum < r else r
            bisect.insort_right(smallest, cur)
            print("sm", smallest, rate[start][2])
            start += 1
        print(rr)
        return round(r, 5)


# quality = [10, 20, 5]
# wage = [70, 50, 30]
# K = 2
# quality = [3,1,10,10,1]
# wage = [4,8,2,2,7]
# K = 3
quality = [3, 1, 10, 10, 1]
wage = [4, 8, 2, 2, 7]
K = 3
res = Solution().mincostToHireWorkers(quality, wage, K)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
