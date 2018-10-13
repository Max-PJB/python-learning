#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/23 22:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

"""
arr = map(int, input().split())这句话进场看见，在python3中：

    arr = map(int, input().split())    #2 4 6 8
    print(arr)                         #output  <map object at 0x0000025A09157F28>

这样输出就行："""


arr = map(int, input().split())  # 2 4 6 8
print(list(arr))  # output   [2, 4, 6, 8]
"""
原因：
python3下的map()函数返回类型为iterators，不再是list，所以可将上述语句修改为
"""