#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/10/29 22:44
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       1015. 可被 K 整除的最小整数
-------------------------------------------------
"""
import time
from typing import List

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # 假设存在一个数 X = Xn Xn-1 …… X2 X1 X0 满足 K*X = 11111……11111
        # 从个位开始，K0 * X0 = 10a+y ，那么一定要满足 y == 1；然后 R = K0*X1 = K * X0
        # 十位： K0 * X1 + R//10%10(R的十位） = 10b+y , 同样需要满足 y == 1,；然后 R = R + K*X1*10
        # 百位： K0 * X2 + R//100%10(R的百位） = 10c + y 同理：y要满足 y == 1 然后 R = R + K*X2*100
        """判断一个数是不是全是 1"""

        def ok(rr):
            # 当 rr ！= 0 时
            rr, remainder = divmod(rr, 10)
            if remainder != 1:
                return False
            while rr:
                print("111")

                rr, remainder = divmod(rr, 10)
                if remainder != 1:
                    return False
            return True

        R = 0
        w = 0
        k = K % 10
        while not ok(R):
            print(R,"rrrrrrrrrrrrrr","222")

            value_w = R % 10
            x = 0
            while x < 10 and (k * x + value_w) % 10 != 1:
                x += 1
                print(x,"xxxxxxx","1333331")

            # 如果是以 x == 10 结束的循环，说明不符合要求，不存在 x
            if x == 10:
                return -1
            else:
                R = (R + K * x)//10
                if not R:
                    return w+1
            w += 1
        return w + len(str(R))

aa = 3
res = Solution().smallestRepunitDivByK(aa)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
