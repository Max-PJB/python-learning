#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/10 20:20
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  842. 将数组拆分成斐波那契序列

    用户通过次数 8
    用户尝试次数 15
    通过次数 8
    提交次数 32
    题目难度 Medium

给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。

形式上，斐波那契式序列是一个非负整数列表 F，且满足：

    0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
    F.length >= 3；
    对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。

另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。

返回从 S 拆分出来的所有斐波那契式的序列块，如果不能拆分则返回 []。

示例 1：

输入："123456579"
输出：[123,456,579]

示例 2：

输入: "11235813"
输出: [1,1,2,3,5,8,13]

示例 3：

输入: "112358130"
输出: []
解释: 这项任务无法完成。

示例 4：

输入："0123"
输出：[]
解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。

示例 5：

输入: "1101111"
输出: [110, 1, 111]
解释: 输出 [11,0,11,11] 也同样被接受。

提示：

    1 <= S.length <= 200
    字符串 S 中只含有数字。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        if n < 3:
            return False

        # 判断字符串的合理性
        def is_digital(ss):
            if len(str(int(ss))) == len(ss):
                return True
            else:
                return False

        # 判断是不是以某个开头的斐波那契数列
        def is_fabonacci(f0_start, f0_end, f1_start, f1_end, ans):
            if f1_end == n:
                return ans
            F_0 = S[f0_start:f0_end:]
            F_1 = S[f1_start:f1_end:]
            if not is_digital(F_0) or not is_digital(F_1):
                return False
            F_2 = int(F_0) + int(F_1)
            str_F_2 = str(F_2)
            len_F_2 = len(str_F_2)
            if S[f1_end:f1_end + len_F_2:] == str_F_2:
                return is_fabonacci(f1_start, f1_end, f1_end, f1_end + len_F_2, ans+[F_2])
            else:
                return False

        # 数列第一项的长度最多不超过整个长度的一半，光他自己就大于剩下的了
        for i in range(1, (n - 1) // 2 + 1):
            # 数列第二项的长度不超过 整下整个长度的一半，理由同上。
            # 整下的长度是 n - i
            for j in range(1, (n - i) // 2 + 1):
                F_0 = S[0:i:]
                F_1 = S[i:i + j:]
                if is_digital(F_0) and is_digital(F_1):
                    res = is_fabonacci(0, i, i, i + j, [int(F_0), int(F_1)])
                    if res:
                        print(S, S[0:i:], S[i:i + j:])
                        return res
        return False


inin = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
in_res = [539834657, 21, 539834678, 539834699, 1079669377, 1619504076, 2699173453, 4318677529, 7017850982, 11336528511]
ll = ""
for i in range(len(in_res)):
    ll += str(in_res[i])
print(ll,ll==inin)
for i in range(len(in_res)-2):

    print("{} + {}={}  =={} --{}".format(in_res[i],in_res[i+1],in_res[i]+in_res[i+1],in_res[i+2],in_res[i]+in_res[i+1]==in_res[i+2]))
res = Solution().splitIntoFibonacci(inin)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
