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
        """
        最后一题，考虑四种情况：
            1、前缀数组中所有数字的频率只有两种，设为A和B，其中A=B+1，且只有一个数字频率为A；
            2、前缀数组中所有数字的频率只有两种，其中只有一个数字的频率为1，其他数字的频率都大于1且相等；
            3、整个数组的数字的频率都是1；
            4、整个数组都是同一个数字。

            对应的处理：
            1、把前缀数组中频率为A的数字删去1个即可；
            2、把前缀数组中频率为1的数字删去即可；
            3、整个数组删去任意一个数字都可；
            4、整个数组删去任意一个数字都可。

            或许代码中的 fre[maxcnt]==1&&1+fre[maxcnt-1](maxcnt-1)==i+1) 比较难理解，
            我们要先知道fre是怎么存储的，例如我们已经遍历了[5,1,1,5,5]，
            那此时fre[1]=2（包含了1和5）,fre[2]=2（包含了1和5）,fre[3]=1（只包含5）。
            所以上面的 1+fre[maxcnt-1](maxcnt-1)==i+1 表示为 (fre[maxcnt-1]-1)*(maxcnt-1) + (maxcnt)==i+1 即频率为B的数字总数 + 频率为A的数字总数。

            作者：yang-tian-lun
            链接：https://leetcode-cn.com/problems/maximum-equal-frequency/solution/conkao-lu-san-chong-qing-kuang-by-yang-tian-lun/

        """



# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
res = Solution().maxEqualFreq([1,2,3,4,5,6,7,8,9])
print(res)
