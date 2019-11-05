#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/4 14:12
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1108. IP 地址无效化
    https://leetcode-cn.com/contest/weekly-contest-144/problems/defanging-an-ip-address/
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()

# 下面写上代码块
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))



