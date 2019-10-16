#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/16 14:33
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    898. 子数组按位或操作 显示英文描述
用户通过次数14
用户尝试次数123
通过次数14
提交次数348
题目难度Medium
我们有一个非负整数数组 A。

对于每个（连续的）子数组 B = [A[i], A[i+1], ..., A[j]] （ i <= j），我们对 B 中的每个元素进行按位或操作，获得结果 A[i] | A[i+1] | ... | A[j]。

返回可能结果的数量。 （多次出现的结果在最终答案中仅计算一次。）



示例 1：

输入：[0]
输出：1
解释：
只有一个可能的结果 0 。
示例 2：

输入：[1,1,2]
输出：3
解释：
可能的子数组为 [1]，[1]，[2]，[1, 1]，[1, 2]，[1, 1, 2]。
产生的结果为 1，1，2，1，3，3 。
有三个唯一值，所以答案是 3 。
示例 3：

输入：[1,2,4]
输出：6
解释：
可能的结果是 1，2，3，4，6，以及 7 。


提示：

1 <= A.length <= 50000
0 <= A[i] <= 10^9
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()

# 下面写上代码块
"""我们尝试优化一下这种最简单的枚举方法。可以发现，对于固定的 j，result(j, j), result(j - 1, j), result(j - 2), j, ..., result(1, j) 的值是单调不降的，因为将 result(k, j) 对 A[k - 1] 做按位或操作，得到的结果 result(k - 1, j) 一定不会变小。并且，根据按位或操作的性质，如果把 result(k, j) 和 result(k - 1, j) 都用二进制表示，那么后者将前者二进制表示中的若干个 0 变成了 1。

由于数组 A 中都是小于 10^9 的正整数，它们的二进制表示最多只有 32 位。因此从 result(j, j) 开始到 result(1, j) 结束，最多只会有 32 个 0 变成了 1，也就是说，result(j, j), result(j - 1, j), result(j - 2), j, ..., result(1, j) 中最多只有 32 个不同的数。这样我们就可以维护一个集合，存储所有以 j 为结尾的 result 值。当结尾从 j 枚举到 j + 1 时，我们将集合中的每个数对 A[j + 1] 做按位或操作，得到的新的 result 值也不会超过 32 个。

算法

我们用一个集合 cur 存储以 j 为结尾的 result 值，即所有满足 i <= j 的 A[i] | ... | A[j] 的值。集合的大小不会超过 32。
"""


class Solution(object):
    def subarrayBitwiseORs(self, A):
        ans = set()
        cur = {0}
        for x in A:
            print("111",cur,ans)
            cur = {x | y for y in cur} | {x}
            ans |= cur
            print("2222",cur,ans)
        return len(ans)

print({2,3}|{1,2,3})
haha = [1,2,4]
res = Solution().subarrayBitwiseORs(haha)
print(res)
"""复杂度分析

时间复杂度：O(N \log W)O(NlogW)，其中 NN 是数组 A 的长度，WW 是 A 中最大的数。

空间复杂度：O(N \log W)O(NlogW)。在给出的代码中用集合 ans 存放了所有答案，会使用 O(N \log W)O(NlogW) 的空间。但这题只要返回答案的数量，因此可以只用一个变量对集合 cur 的大小进行累加，这样空间复杂度可以降低为 O(\log W)O(logW)。"""

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
