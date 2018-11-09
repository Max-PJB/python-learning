#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/6 21:53
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 881. 救生艇

    虚拟 用户通过次数 85
    虚拟 用户尝试次数 132
    虚拟 通过次数 85
    虚拟 提交次数 132
    题目难度 Medium

第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。



示例 1：

输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)

示例 2：

输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)

示例 3：

输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)

提示：

    1 <= people.length <= 50000
    1 <= people[i] <= limit <= 30000
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def num_rescue_boats(people, limit):
    if limit < max(people):
        return False
    people.sort()
    n = len(people)
    i, j = 0, n - 1
    ls = [1 for _ in range(n)]
    while i < j:
        if people[i] + people[j] <= limit:
            ls[j] = 0
            i += 1
            j -= 1
        else:
            j -= 1
    return ls.count(1)


# people_in = [3, 5, 3, 4]
# limit_in = 5
people_in = [1, 2]
limit_in = 3
print(num_rescue_boats(people_in, limit_in))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
