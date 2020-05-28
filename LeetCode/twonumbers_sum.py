#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/10/20 14:59
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]


-------------------------------------------------
"""
import time
from collections import OrderedDict
__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numsSorted = sorted(nums)
    n = len(nums)
    print(numsSorted)
    for i in range(n - 1, 0, -1):
        # for j in range(i+1, n):
        #     if nums[i] + nums[j] == target:
        #         print(nums[i], " = ", i)
        #         print(nums[j], " = ", j)
        #         return [i, j]
        j = 0
        print(i, "  ", j, "  ", numsSorted[i], "  ", numsSorted[j])
        while numsSorted[i] + numsSorted[j] < target:
            print("do while")
            j += 1
        if numsSorted[i] + numsSorted[j] == target:
            print(numsSorted)
            print(i, "  ", j, "  ", numsSorted[i], "  ", numsSorted[j])
            a = nums.index(numsSorted[j])
            nums.reverse()
            b = n - 1 - nums.index(numsSorted[i])
            return [a, b]
        pass


nums = [3, 3]
target = 6
kk = twoSum(nums, target)
print(kk)

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
"""
方法一：暴力法

暴力法很简单。遍历每个元素 xxx，并查找是否存在一个值与 target−xtarget - xtarget−x 相等的目标元素。
public int[] twoSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[j] == target - nums[i]) {
                return new int[] { i, j };
            }
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}

复杂度分析：

    时间复杂度：O(n2)O(n^2)O(n2)， 对于每个元素，我们试图通过遍历数组的其余部分来寻找它所对应的目标元素，这将耗费 O(n)O(n)O(n) 的时间。因此时间复杂度为 O(n2)O(n^2)O(n2)。

    空间复杂度：O(1)O(1)O(1)。

方法二：两遍哈希表

为了对运行时间复杂度进行优化，我们需要一种更有效的方法来检查数组中是否存在目标元素。如果存在，我们需要找出它的索引。保持数组中的每个元素与其索引相互对应的最好方法是什么？哈希表。

通过以空间换取速度的方式，我们可以将查找时间从 O(n)O(n)O(n) 降低到 O(1)O(1)O(1)。哈希表正是为此目的而构建的，它支持以 近似 恒定的时间进行快速查找。我用“近似”来描述，是因为一旦出现冲突，查找用时可能会退化到 O(n)O(n)O(n)。但只要你仔细地挑选哈希函数，在哈希表中进行查找的用时应当被摊销为 O(1)O(1)O(1)。

一个简单的实现使用了两次迭代。在第一次迭代中，我们将每个元素的值和它的索引添加到表中。然后，在第二次迭代中，我们将检查每个元素所对应的目标元素（target−nums[i]target - nums[i]target−nums[i]）是否存在于表中。注意，该目标元素不能是 nums[i]nums[i]nums[i] 本身！
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], i);
    }
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement) && map.get(complement) != i) {
            return new int[] { i, map.get(complement) };
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}
复杂度分析：

    时间复杂度：O(n)O(n)O(n)， 我们把包含有 nnn 个元素的列表遍历两次。由于哈希表将查找时间缩短到 O(1)O(1)O(1) ，所以时间复杂度为 O(n)O(n)O(n)。

    空间复杂度：O(n)O(n)O(n)， 所需的额外空间取决于哈希表中存储的元素数量，该表中存储了 nnn 个元素。

方法三：一遍哈希表

事实证明，我们可以一次完成。在进行迭代并将元素插入到表中的同时，我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。如果它存在，那我们已经找到了对应解，并立即将其返回。
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
        }
        map.put(nums[i], i);
    }
    throw new IllegalArgumentException("No two sum solution");
}
复杂度分析：

    时间复杂度：O(n)O(n)O(n)， 我们只遍历了包含有 nnn 个元素的列表一次。在表中进行的每次查找只花费 O(1)O(1)O(1) 的时间。

    空间复杂度：O(n)O(n)O(n)， 所需的额外空间取决于哈希表中存储的元素数量，该表最多需要存储 nnn 个元素。


"""
