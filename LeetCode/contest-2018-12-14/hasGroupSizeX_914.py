#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/14 12:58
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 914. 卡牌分组

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
    题目难度 Easy

给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

    每组都有 X 张牌。
    组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。



示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

示例 2：

输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。

示例 3：

输入：[1]
输出：false
解释：没有满足要求的分组。

示例 4：

输入：[1,1]
输出：true
解释：可行的分组是 [1,1]

示例 5：

输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]


提示：

    1 <= deck.length <= 10000
    0 <= deck[i] < 10000
-------------------------------------------------
"""
import time
import collections

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # 这一段实现，有直接的现成函数 collections.Counter
        # i_dict = collections.defaultdict(int)
        # for i in deck:
        #     i_dict[i] += 1
        i_dict = collections.Counter(deck)
        vs = i_dict.values()
        n = min(vs)
        if n < 2:
            return False
        # print(n)
        i = 2
        cd = []
        while i <= n:
            # print("i=",i)
            if n % i == 0:
                cd.append(i)
            i += 1
        for v in vs:
            for i, d in enumerate(cd):
                if v % d != 0:
                    cd[i] = 1
        # print(cd)
        if cd.count(1) == len(cd):
            return False
        return True

    # 大神啊，用了这么厉害的方法
    def hasGroupsSizeX2(self, deck):
        count = collections.Counter(deck)
        X = min(count.values())
        for x in range(2, X + 1):
            if all(v % x == 0 for v in count.values()):
                return True
        return False


d_in = [1,1,1,1,2,2,2,2,2,2]
res = Solution().hasGroupsSizeX(d_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
