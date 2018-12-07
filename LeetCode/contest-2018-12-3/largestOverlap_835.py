#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/3 21:31
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   835. 图像重叠

    虚拟 用户通过次数 3
    虚拟 用户尝试次数 12
    虚拟 通过次数 3
    虚拟 提交次数 12
    题目难度 Medium

给出两个图像 A 和 B ，A 和 B 为大小相同的二维正方形矩阵。（并且为二进制矩阵，只包含0和1）。

我们转换其中一个图像，向左，右，上，或下滑动任何数量的单位，并把它放在另一个图像的上面。之后，该转换的重叠是指两个图像都具有 1 的位置的数目。

（请注意，转换不包括向任何方向旋转。）

最大可能的重叠是什么？

示例 1:

输入：A = [[1,1,0],
          [0,1,0],
          [0,1,0]]
     B = [[0,0,0],
          [0,1,1],
          [0,0,1]]
输出：3
解释: 将 A 向右移动一个单位，然后向下移动一个单位。

注意:

    1 <= A.length = A[0].length = B.length = B[0].length <= 30
    0 <= A[i][j], B[i][j] <= 1
-------------------------------------------------
"""
import time
import itertools

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        one_coordinates = []
        n = len(A)
        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    one_coordinates.append((i, j))
        print(one_coordinates)
        res = 0
        v = 0
        h = 0
        for vertical in range(1 - n, n):
            for horizontal in range(1 - n, n):
                cnt = 0
                for i, j in one_coordinates:
                    if 0 <= i + vertical < n and 0 <= j + horizontal < n and B[i + vertical][j + horizontal]:
                        cnt += 1
                if cnt > res:
                    res, v, h = cnt, vertical, horizontal
        return res


A = [[1, 1, 0],
     [0, 1, 0],
     [0, 1, 0]]
B = [[0, 0, 0],
     [0, 1, 1],
     [0, 0, 1]]
res = Solution().largestOverlap(A, B)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
