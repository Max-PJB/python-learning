#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/13 10:47
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1054. 距离相等的条形码
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # 我的思路：
        #     1. 先分类然后数一下各有多少个，[x,y,z ……] [n,m.l……] 找出数量最多的那个 假如是 x ，一共有 n 个 x
        #     2. 把 n 个 x 分别放进去 n 个桶里去
        #     3. 后面的按顺序，从 1~n 一轮又一轮的往 桶里面塞
        #     4. 最后把 n 个桶合并就好了
        # 别人的插入思路更好：
        # 最多的也不过是 数组的一半嘛，按数量的多少排序成一个数组 X
        # 定义个长度相等的 res 数据
        # 把 X 的前一半填充到 res 的奇数位置， 后一半填充到偶数位置 就 ok 了
        # 需要注意的是，当 X 的长度是奇数 2n+1 时候，前一半取 n+1 个，防止 最多的一个数出现 n+1 次
        from collections import Counter
        counter = Counter(barcodes)
        # print(counter.most_common(1))
        # most = counter.most_common(1)[0][1]
        res = [None for _ in range(len(barcodes))]
        tmp = []
        for barcode, i in counter.most_common():
            tmp += [barcode] * i
        print(tmp)
        # 这个迭代写法好新奇！！！！
        res[::2] = tmp[:len(tmp[::2])]
        res[1::2] = tmp[len(tmp[::2]):]

        # res = [[] for _ in range(most)]
        # tmp = 0
        # for barcode, i in counter.most_common():
        #     for j in range(i):
        #         res[(tmp + j) % most].append(barcode)
        #     tmp = (tmp + i) % most
        # print(counter)
        # print(res)
        # from functools import reduce
        # return list(reduce(lambda x, y: x + y, res))
        return res


inin = [2, 2, 1, 3]
rr = Solution().rearrangeBarcodes2(inin)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
