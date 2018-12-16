#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/14 13:34
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  915. 分割数组

    虚拟 用户通过次数 30
    虚拟 用户尝试次数 38
    虚拟 通过次数 30
    虚拟 提交次数 38
    题目难度 Medium

给定一个数组 A，将其划分为两个不相交（没有公共元素）的连续子数组 left 和 right， 使得：

    left 中的每个元素都小于或等于 right 中的每个元素。
    left 和 right 都是非空的。
    left 要尽可能小。

在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。



示例 1：

输入：[5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]

示例 2：

输入：[1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]



提示：

    2 <= A.length <= 30000
    0 <= A[i] <= 10^6
    可以保证至少有一种方法能够按题目所描述的那样对 A 进行划分。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        left_max = []
        right_min = []
        left_ls = -1
        for i in range(n):
            if A[i] > left_ls:
                left_ls = A[i]
            left_max.append(left_ls)
        right_ls = 10 ** 7
        for j in range(n - 1, -1, -1):
            if A[j] < right_ls:
                right_ls = A[j]
            right_min.insert(0, right_ls)
        for i in range(n-1):
            if left_max[i] <= right_min[i+1]:
                return i+1
        return False

    # 大神的想法很厉害啊，两次操作就搞定了
    def partitionDisjoint2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        tmp = A[0]
        ans = 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] < tmp:
                ans = i + 1
                break
        left_max = max(A[:ans])
        for i in range(len(A) - 1, ans - 2, -1):
            if A[i] < left_max:
                ans = i + 1
                break
        return ans


a_in = [1,1]
res = Solution().partitionDisjoint2(a_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
