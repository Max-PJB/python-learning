#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/27 13:24
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    861. 翻转矩阵后的得分

    用户通过次数 31
    用户尝试次数 38
    通过次数 31
    提交次数 49
    题目难度 Medium

有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。



示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39



提示：

    1 <= A.length <= 20
    1 <= A[0].length <= 20
    A[i][j] 是 0 或 1
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for a in A:
            # 第一个字母是 0
            if not a[0]:
                for k in range(len(a)):
                    a[k] = abs(a[k] - 1)
        A_T = list(zip(*A))
        res = 0
        for i, j_list in enumerate(A_T[::-1]):
            res += 2 ** i * max(j_list.count(0), j_list.count(1))
        return res


A_in = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
res = Solution().matrixScore(A_in)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
