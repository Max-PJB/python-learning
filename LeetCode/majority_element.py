#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/14 22:12
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  求众数

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3

示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        left = n
        most = 0
        num_dict = {0:0}
        for k in nums:
            if k in num_dict.keys():
                num_dict[k] += 1
                print(most,k,num_dict[k])
                most = k if num_dict[k] > num_dict[most] else most
                left -= 1
                if num_dict[most] + left <= int(n/2):
                    return False
            else:
                num_dict[k] = 1
        return most


#  再来看看大牛的方法，因为个数比所有的其他的个数加起来还要多一个，
#  所以，指向当前元素时候 加 1，不是当前元素的时候 -1
#  不管众数在啥子地方，最后剩下的那个肯定是那个众数啦
def majority_element(nums):
        cur = nums[0]
        count = 0
        for i in nums:
            if count == 0:
                cur = i
            count += 1 if cur == i else -1
        return cur


s_in = [8,8,7,7,7]
res = Solution().majorityElement(s_in)
print(res)
print(majority_element(s_in))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))



