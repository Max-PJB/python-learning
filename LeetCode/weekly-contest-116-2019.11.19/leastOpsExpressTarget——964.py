#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/20 15:26
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       964. 表示数字的最少运算符

-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        # TODO 不会啊 跪下了 https://leetcode-cn.com/problems/least-operators-to-express-number/solution/di-gui-de-chai-jie-shu-zi-by-clamcy/

        res = []
        result = 0
        while target:
            target, b = divmod(target, x)
            res.append(b)
        print(res)
        for i, r in enumerate(res):
            # if i == 0:
            if i == 0 and r == x // 2 + 1:
                res[i] = x - r
                if i + 1 < len(res):
                    res[i + 1] += 1
                else:
                    res.append(1)
            if r > x // 2 + 1:
                res[i] = x - r
                if i + 1 < len(res):
                    res[i + 1] += 1
                else:
                    res.append(1)
        print(res)
        for i, r in enumerate(res):
            result += abs(i - 1) * r + r
            print(i - 1, r, "->", result)
        return result - 1


in_x = 3
target = 929
rr = Solution().leastOpsExpressTarget(in_x, target)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
