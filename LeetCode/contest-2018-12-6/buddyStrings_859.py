#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/6 13:27
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   859. 亲密字符串

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Easy

给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。



示例 1：

输入： A = "ab", B = "ba"
输出： true

示例 2：

输入： A = "ab", B = "ab"
输出： false

示例 3:

输入： A = "aa", B = "aa"
输出： true

示例 4：

输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true

示例 5：

输入： A = "", B = "aa"
输出： false



提示：

    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A 和 B 仅由小写字母构成。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        n = len(A)
        if n != len(B):
            print("111")
            return False
        no_equal = []
        no_equal_cnt = 0
        for i in range(n):
            if A[i] != B[i]:
                no_equal.append(i)
                no_equal_cnt += 1
                if no_equal_cnt > 2:
                    return False
        if no_equal_cnt == 0 and len(set(B)) != len(B):
            return True
        elif no_equal_cnt == 2 and A[no_equal[0]] == B[no_equal[1]] and A[no_equal[1]] == B[no_equal[0]]:
            return True
        else:
            return False


A = "ab"
B = "ab"
res = Solution().buddyStrings(A, B)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
