#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/12/17 19:57
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       871. 最低加油次数
-------------------------------------------------
"""
import time
from typing import List
# list_to_tree 我自己写的一个 list 转 root 的方法
from LeetCode.leetcode_utils.leetcode_list2tree import list_to_tree, TreeNode

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
# 动态规划
# dp[i] 表示加一次油能到达的最远位置
# 1. 考虑，dp[0] = startFuel,初始 dp = [startFuel,0,0,……,0], 0 的个数 == 加油站的个数，最多加这么多次油嘛
# 2. 那么,考虑第一个加油站，如果加油站的位置在 dp[0]的射程以内，那么 dp[1] = dp[0] + station1 , dp[2]=dp[3]=dp[……]=0 ，这不是只能加一次油嘛
# 3. 第二个加油站的时候，如果 这个加油站在 dp[0] 的射程以内，那么 dp[1] = dp[0]+ station2，这个时候再和 前面的 dp[1] 比较一下大小，就是考虑加油站1，2 后加一次油能到的最远地方
#       这个时候，若果加油站在 dp[1] 的射程内，就还有个 dp[2] = dp[1] + station2 ，注意，这一步要在前面算 dp[1] 之前计算，以免 station2 加了两次
# 4. 同理，考虑 第 i 个加油站，加油站在不在 dp[0 - i-1]的射程内，如果在 dp[t] 射程内, t < i ，那么 dp[t+1] = dp[t] + station_i 再已有的 dp[t+1] 比较。 和 3 中一样，t 的循环要从大到小，以免把前一轮的数据弄脏了
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        # i 表示第 i 个加油站（这里 i 从 0 开始的，注意），j 是加油站的 index， oil 是加油站的油量
        for i, (j, oil) in enumerate(stations):
            # 这里要从最大的往小的，避免污染前一轮的数据
            for t in range(i, -1, -1):
                if j <= dp[t]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + oil)
            print(i, dp)
        for i in range(len(dp)):
            if dp[i] >= target:
                return i
        return -1


target = 100
startFuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
rr = Solution().minRefuelStops(target, startFuel, stations)
print(rr)


# TODO 这个思想还需要加强啊
# 贪心算法嘛，这个比动态规划好理解，我初始能到 i 位置，如果i不是终点，那我必须在 0-i 内加一次油，肯定选油最多的那个加油站（有j 个油）
# 加了这次油后，最多就能到 i+j 位置，如果 还没到终点，那就在 0 - i+j 中间再加一次油，这次就是选 0 - i+j 中那个油最多的加油站（前面加过油的加油站不考虑）
# 1. 初始化一个可以加油的加油站数组 able = []
# 2. 加 0 次油，能到 i 位置。把 0- i 位置内所有的加油站都加入, able =[station1,station2,……,station_k] ,从 able 中挑一个油最多的，就得到了加一次油能到的最远的地方
# 3. 在 步骤2 中得到了加 1 次油能到的最远的地方 j ，我们把那个加油站从 able 中删除，然后把 i - j 中所有的加油站添加早 able 中。重复步骤 2,3
class Solution2(object):
    def minRefuelStops(self, target, startFuel, stations):
        # 当前可以使用的加油站
        able = []
        # 加 k 次油
        k = 0
        arrive = startFuel
        pre_pos = 0
        while arrive < target:
            for j, oil in stations:
                if pre_pos < j <= arrive:
                    able.append(oil)
            k += 1
            if not able:
                break
            max_oil = max(able)
            pre_pos = arrive
            arrive += max_oil
            print(k, able, arrive)
            able.remove(max_oil)
        if arrive < target:
            return -1
        else:
            return k

    # 上面这堆代码里面每加一次油就要遍历一遍所有加油站，有点浪费时间，想想能不能改进一下，只遍历一遍加油站
    def minRefuelStops2(self, target, startFuel, stations):
        arrive = startFuel
        able = []
        k = 0
        for pos, oil in stations:
            print('k,arrive,pos,oil', k, arrive, pos, oil, able)
            if arrive >= target:
                print('okokok: k,arrive,pos,oil', k, arrive, pos, oil)
                return k
            while able and pos > arrive:
                # 这里找最大的那个值有点麻烦了，可以直接使用 堆 heapq
                # 不过 python3 的 heapq 默认是小根堆，需要把每个数搞成负数，有点麻烦，我这里就算了
                k += 1
                max_oil = max(able)
                able.remove(max_oil)
                arrive += max_oil
            if pos <= arrive:
                able.append(oil)
            else:
                return -1
        # 有可能存在 arrvie < target 所有加油站都 在 able 里面，这个时候就找 able 中的最大加油站一个一个加就好了
        while able and arrive < target:
            k += 1
            max_oil = max(able)
            arrive += max_oil
            able.remove(max_oil)
        if arrive >= target:
            return k
        else:
            return -1


rr2 = Solution2().minRefuelStops(target, startFuel, stations)
print(rr2)
rr3 = Solution2().minRefuelStops2(target, startFuel, stations)
print(rr3)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
