#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/3 16:59
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def four_sum_equal_target(nums, target):
    nums.sort()
    n = len(nums)
    i = 0
    res = []
    if target < nums[0] + nums[1] + nums[2] + nums[3] or nums[n-4] + nums[n-3] + nums[n-2] + nums[n-1] < target:
        return res
    while i < n - 3:
        j = i + 1
        while j < n - 2:
            k = j + 1
            g = n - 1
            while k < g:
                print(i, j, k, g)
                print(nums[i], nums[j], nums[k], nums[g])
                if nums[i] + nums[j] + nums[k] + nums[g] == target:
                    res.append((nums[i], nums[j], nums[k], nums[g]))
                    while k + 1 < n and nums[k] == nums[k + 1]:
                        k += 1
                    k += 1
                    while g - 1 > j and nums[g] == nums[g - 1]:
                        g -= 1
                    g -= 1
                elif nums[i] + nums[j] + nums[k] + nums[g] < target:
                    while k + 1 < n and nums[k] == nums[k + 1]:
                        k += 1
                    k += 1
                else:
                    while g - 1 > j and nums[g] == nums[g - 1]:
                        g -= 1
                    g -= 1
            while j + 1 < n - 2 and nums[j] == nums[j + 1]:
                j += 1
            j += 1
        while i < n - 3 and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return list(map(list, list(set(res))))


nums_in = [-495, -482, -455, -447, -400, -388, -381, -360, -350, -340, -330, -317, -308, -300, -279, -235, -209, -206,
           -188, -186, -171, -145, -143, -141, -137, -129, -121, -115, -97, -56, -47, -28, -20, -19, 8, 11, 35, 41, 46,
           50, 69, 84, 85, 86, 88, 91, 135, 160, 171, 172, 177, 190, 226, 234, 238, 244, 249, 253, 254, 272, 281, 284,
           294, 296, 300, 303, 307, 313, 320, 320, 327, 334, 355, 362, 367, 401, 426, 436, 456, 467, 473, 473, 484]
target_in = -7178
print(four_sum_equal_target(nums_in, target_in))
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
