#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/13 17:11
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   删除排序数组中的重复项

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。

示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def remove_duplicates(nums):
    if not nums:
        return 0
    res = 1
    ls = nums[0]
    n = len(nums)
    i = 1
    while i < n:
        print(res, nums)
        if ls == nums[i]:
            nums.pop(i)
            n -= 1
        else:
            res += 1
            ls = nums[i]
            i += 1
    print(res)


def remove_duplicates2(nums):
    if not nums:
        return 0
    tmp = nums[0]
    res = 1
    for i in range(1,len(nums)):
        if tmp < nums[i]:
            nums[res] = nums[i]
            tmp = nums[i]
            res += 1
            i += 1
    print(res)
    for i in range(res):
        print(nums[i])
    return res


# nums_in = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums_in2 = [-50, -50, -49, -47, -47, -47, -47, -46, -45, -44, -44, -43, -42, -41, -41, -40, -40, -40, -39, -39, -39, -37,
           -35, -34, -33, -31, -31, -28, -27, -27, -26, -25, -25, -24, -24, -24, -23, -23, -21, -20, -20, -18, -17, -16,
           -16, -15, -14, -13, -13, -12, -10, -10, -9, -8, -8, -8, -6, -5, -3, -2, -2, -1, 3, 3, 4, 5, 5, 8, 8, 8, 8, 9,
           10, 11, 11, 12, 13, 14, 16, 16, 17, 18, 18, 19, 19, 20, 20, 20, 21, 22, 23, 23, 23, 25, 25, 26, 27, 27, 28,
           30, 31, 32, 33, 33, 33, 34, 34, 35, 37, 37, 39, 40, 41, 42, 43, 43, 44, 44, 45, 46, 47, 48, 48, 48, 49, 49,
           50]
# remove_duplicates(nums_in)
print(nums_in2)
print(remove_duplicates2(nums_in2))
print(nums_in2)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
