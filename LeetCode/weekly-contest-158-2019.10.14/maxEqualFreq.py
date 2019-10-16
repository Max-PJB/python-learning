#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/14 10:57
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :      5225. 最大相等频率 显示英文描述
用户通过次数85
用户尝试次数164
通过次数87
提交次数488
题目难度Hard
给出一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回其长度：

从前缀中 删除一个 元素后，使得所剩下的每个数字的出现次数相同。
如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。



示例 1：

输入：nums = [2,2,1,1,5,3,3,5]
输出：7
解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4]=5，就可以得到 [2,2,1,1,3,3]，里面每个数字都出现了两次。
示例 2：

输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
输出：13
示例 3：

输入：nums = [1,1,1,2,2,2]
输出：5
示例 4：

输入：nums = [10,2,8,9,3,8,1,5,2,3,7,6]
输出：8


提示：

2 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
-------------------------------------------------
"""
import time
from typing import List
import collections

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        num_count_dict = {}
        count_dict = collections.defaultdict(int)
        res = 1
        for i in range(len(nums)):
            num = nums[i]
            print(num)
            if num not in num_count_dict:
                num_count_dict[num] = 1
                count_dict[1] = count_dict[1] + 1
            else:
                count = num_count_dict[num]
                num_count_dict[num] = num_count_dict[num] + 1
                count_dict[count] = count_dict[count] - 1
                count_dict[count + 1] = count_dict[count + 1] + 1
            print("num_count_dict:", num_count_dict)
            print("count_dict", count_dict)
            print(count_dict.items())
            haha = list(filter(lambda x: x[1] != 0, count_dict.items()))
            print("haha",haha)
            if len(haha) == 1 and (haha[0][1] == 1 or haha[0][0] == 1) and i >= res:
                res = i
            if len(haha) == 2:
                if (1, 1) in haha:
                    res = i
                if haha[0][0] > haha[1][0]:
                    h1, h2 = haha[0], haha[1]
                else:
                    h1, h2 = haha[1], haha[0]
                if h1[0] - h2[0] == 1 and h1[1] == 1:
                    res = i
        return res+1


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
res = Solution().maxEqualFreq([1,2,3,4,5,6,7,8,9])
print(res)
