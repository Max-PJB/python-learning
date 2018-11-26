#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/24 16:01
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   格雷编码

格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1

示例 2:

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2**n。当 n = 0 时，长度为 2**n = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        global res, left
        res = [[0 for _ in range(n)]]
        left = []

        def gg(ls, k):
            """
            :param ls: List[int]
            :param k: int
            :return:None
            """
            if k == n:
                left.append(ls)
            if k < n:
                gg(ls + [0], k + 1)
                gg(ls + [1], k + 1)

        def ff(ls, ll):
            """
            :param pre: List[int]
            :param ll: List[List[int]]
            :param ls: List[List[int]]
            :return:None
            """
            if not ll:
                res.append(ls)
            for k in range(len(ll)):
                if num_change(ls[-1], ll[k]) == 1:
                    ff(ls + [ll[k]], ll[:k:] + ll[k + 1::])

        def num_change(n1, n2):
            """
            :param n1:List[int]
            :param n2:List[int]
            :return: int
            """
            rr = 0
            for i, j in zip(n1, n2):
                rr += abs(i - j)
            return rr

        def list_to_int(lll):
            """
            :param lll:List[List[int]]
            :return: List[int]
            """
            rr = []
            for ll in lll:
                ls = 0
                for i, j in enumerate(ll):
                    ls += 2 ** i * j
                rr.append(ls)
            return rr

        gg([], 0)
        if res[0] in left:
            left.remove(res[0])
        ff([[0 for _ in range(n)]], left)
        # res = list(filter(lambda x: len(x) == 2 ** n, res))
        res = list(map(list_to_int, filter(lambda x: len(x) == 2 ** n, res)))
        return res

    # 这个方法高级啊，高级啊
    def grayCode2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        def gg(k):
            """
            :param k:int
            :return: List[List[int]]
            """
            if k == 1:
                return [[0], [1]]
            else:
                low = gg(k - 1)
                l1 = list(map(lambda x: x + [0], low))
                l2 = list(map(lambda x: x + [1], low[::-1]))
                return l1 + l2

        def to_listint(lll):
            """
            :param lll:List[List[int]]
            :return: int
            """
            ls = 0
            for i, j in enumerate(lll):
                ls += 2 ** i * j
            return ls

        return list(map(to_listint, gg(n)))

    # 这么吊的方法改进一下
    def grayCode4(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        ll = self.grayCode4(n - 1)
        k1 = list(map(lambda x: x << 1, ll))
        k2 = list(map(lambda x: (x << 1) + 1, ll[::-1]))
        return k1+k2

    #  大神的方法，我擦，有点吊啊
    def binary_to_gray(self, num):  # 从自然码变成格雷码的过程，利用数学公式
        result = num ^ (num >> 1)
        return result

    def grayCode3(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 首先遍历真实的数据
        result = []
        for i in range(2 ** n):
            result.append(self.binary_to_gray(i))
        return result


# res = Solution().grayCode2(20)
res4 = Solution().grayCode4(2)
print(res4)
# res3 = Solution().grayCode3(20)
# print(res3)
# print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
