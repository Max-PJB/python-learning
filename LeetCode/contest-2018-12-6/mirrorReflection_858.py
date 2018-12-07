#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/6 18:39
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   858. 镜面反射

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Medium

有一个特殊的正方形房间，每面墙上都有一面镜子。除西南角以外，每个角落都放有一个接受器，编号为 0， 1，以及 2。

正方形房间的墙壁长度为 p，一束激光从西南角射出，首先会与东墙相遇，入射点到接收器 0 的距离为 q 。

返回光线最先遇到的接收器的编号（保证光线最终会遇到一个接收器）。



示例：

输入： p = 2, q = 1
输出： 2
解释： 这条光线在第一次被反射回左边的墙时就遇到了接收器 2 。



提示：

    1 <= p <= 1000
    0 <= q <= p
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """

        def gcd(a, b):
            """
            :param a: int
            :param b: int
            a >= b
            :return: int
            """
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        divisor = gcd(p, q)
        x, y = q // divisor, p // divisor
        print(divisor, x, y)
        res = None
        if x % 2 == 1:
            if y % 2 == 1:
                res = 1
            else:
                res = 2
        else:
            if y % 2 == 1:
                res = 0
            else:
                pass
        return res


res = Solution().mirrorReflection(3, 2)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
