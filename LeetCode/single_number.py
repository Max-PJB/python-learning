#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 21:39
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   只出现一次的数字

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1

示例 2:

输入: [4,1,2,1,2]
输出: 4
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2
            elif nums[i] == nums[i - 1]:
                i += 1
            else:
                break
        return nums[i]


# 大神操作 用异或来实现 注意题目中注明了:!!!! 每个元素均出现 !!两次!!，这是这个注定了可以用异或,两次是关键
# 终极boss。
# 高级用法异或^
# 0异或任何数不变，任何数与自己异或为0。  a⊕b⊕a=b。异或满足加法结合律和交换律
def single_num(nums):
    res = 0
    for i in nums:
        res ^= i
    return res
# 就问你屌不屌


s_in = [2, 2, 1, 1, 4, 4,5,6,6,7,7,8,8]
res = Solution().singleNumber(s_in)
print(res)
print(single_num(s_in))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
