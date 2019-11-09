#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/9 11:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       906. 超级回文数
    https://leetcode-cn.com/contest/weekly-contest-102/problems/super-palindromes/
-------------------------------------------------
"""
import time
from typing import List
"""
当一个回文数字的长度是偶数时，设长度为2n，其一半数字从左边开始分别记作a_0, a_1 ... a_n。当长度为奇数时，设长度为2n+1，其一半数字从左边开始分别记作a_0, a_1 ... a_(n+1)。

这个数字平方时，会有一位的值为：
长度为偶数时: 2(a_0)^2 + 2(a_1)^2 + ... + 2(a_n)^2
长度为奇数时: 2(a_0)^2 + 2(a_1)^2 + ... + 2(a_n)^2 + (a_(n+1))^2

为了保证平方后的依旧是回文，必须确保每一位都没有“进位”(<=9)，所以首先上述位置必须<=9。

然后尝试代入数字，先确定a_0
0 < 2(a_0)^2 <= 9，可得1 <= a_0 <= 2，也就是回文数字的第一位只能是1或者2

规则1: 必须是以数字1或者2开头

设a_0=2, 因为2*2^2=8，所以留下的空间只有1了。
偶数的情况下，由于a_1 ~ a_n都乘了2，所以都只能为0。因此：

规则2: 数字2开头且长度为偶数的回文数字，其他数都必须是0

奇数的情况下，可以直观的看出a_(n+1)可以是0或者1

规则3: 数字2开头且长度为奇数的回文数字，除中间数字可以是0或者1以外，其他数都必须是0

接着看a_0=1的情况。因为2*1^2=2，所以留下的空间为7。可以直观的看出

规则4: 数字1开头且长度为偶数的回文数字，单边可以最多有3个1

规则5: 数字1开头且长度为奇数的回文数字，如果中间数字是2，则单边可以最多有1个1；如果中间数字是1或者0，则单边可以最多有3个1

基于上述规则，先找出能构建超级回文数字的回文数字，然后平方后获得超级回文数字
"""
__author__ = 'Max_Pengjb'
start_time = time.time()

for i in range(10):
    for j in range(10):
        if (i*i*10 + 2*i*j) // 10 == i*i % 10:
            print(i,j)

# 下面写上代码块
class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:

        # 根据长度，返回这个长度的所有回文数 如 长度=3 返回 101 111 121 131 .... 999
        # https://leetcode-cn.com/problems/super-palindromes/solution/zhao-chu-neng-gou-jian-chao-ji-hui-wen-shu-zi-de-h/
        pass


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
