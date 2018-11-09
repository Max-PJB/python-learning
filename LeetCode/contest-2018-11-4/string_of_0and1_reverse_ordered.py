#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/4 12:33
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
将字符串翻转到单调递增

    虚拟 用户通过次数 49
    虚拟 用户尝试次数 84
    虚拟 通过次数 49
    虚拟 提交次数 84
    题目难度 Medium

如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调递增的。

我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。

返回使 S 单调递增的最小翻转次数。


示例 1：

输入："00110"
输出：1
解释：我们翻转最后一位得到 00111.

示例 2：

输入："010110"
输出：2
解释：我们翻转得到 011111，或者是 000111。

示例 3：

输入："00011000"
输出：2
解释：我们翻转得到 00000000。


提示：

    1 <= S.length <= 20000
    S 中只包含字符 '0' 和 '1'
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
# 给s左右补充一个 0 和 1 构成 [0 s 1] 假设最后翻转的结果全是 1 的位置在 x
def min_flips_mono_incr(s):
    ss = "0" + s + "1"
    print(list(ss))
    n = len(ss)
    # 1 在 i 位置时，需要翻动左边使 左边的 1 变为 0 和 翻动自己使 0 变成 1 的次数
    res_left = [0]
    res_right = [0]
    for i in range(1, n):
        a = 1 if ss[i - 1] == "1" else 0
        res_left.append(res_left[i - 1] + a)
    res_left.pop(0)
    print(res_left)
    # 1 在 i 位置时，需要翻动右边使 右边的 0 变为 1 和 翻动自己使 0 变成 1 的次数
    for i in range(n - 2, 0, -1):
        b = 1 if ss[i] == "0" else 0
        res_right.insert(0, b + res_right[0])
    # res_right.pop()
    print(res_right)
    res = min(map(lambda x, y: x + y, res_left, res_right))
    print(res)


s_in = "00110"
min_flips_mono_incr(s_in)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
