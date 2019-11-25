#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/25 17:27
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1268. 搜索推荐系统 Search Suggestions System.
    https://leetcode-cn.com/contest/weekly-contest-164/problems/search-suggestions-system/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # 我的思路：
        #     第一想到的是字典树，看到查找的单词只有一个，想想又要建树，又要查询，遍历好几遍，费时。
        #     想到一个简单的：dp 方法 ：
        # 1. 先排序，这没啥好说的
        # 2. searchword 查找到第 i 个字母的时候，其实他查找的范围是 i-1 个字母的结果
        # 3. 你品，你细品
        n = len(searchWord)
        products.sort()
        res = []
        for i in range(n):
            tmp = []
            for pro in products:
                if i < len(pro) and pro[i] == searchWord[i]:
                    tmp.append(pro)
            products = tmp
            res.append(tmp)

        res = list(map(lambda x: x[0:3], res))
        return res


inin = ["havana"]
searchWord = "havana"
rr = Solution().suggestedProducts(inin, searchWord)
print(rr)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
