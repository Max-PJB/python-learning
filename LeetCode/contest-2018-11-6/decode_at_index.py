#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/6 22:23
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    880. 索引处的解码字符串

    虚拟 用户通过次数 7
    虚拟 用户尝试次数 92
    虚拟 通过次数 7
    虚拟 提交次数 92
    题目难度 Medium

给定一个编码字符串 S。为了找出解码字符串并将其写入磁带，从编码字符串中每次读取一个字符，并采取以下步骤：

    如果所读的字符是字母，则将该字母写在磁带上。
    如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。

现在，对于给定的编码字符串 S 和索引 K，查找并返回解码字符串中的第 K 个字母。



示例 1：

输入：S = "leet2code3", K = 10
输出："o"
解释：
解码后的字符串为 "leetleetcodeleetleetcodeleetleetcode"。
字符串中的第 10 个字母是 "o"。

示例 2：

输入：S = "ha22", K = 5
输出："h"
解释：
解码后的字符串为 "hahahaha"。第 5 个字母是 "h"。

示例 3：

输入：S = "a2345678999999999999999", K = 1
输出："a"
解释：
解码后的字符串为 "a" 重复 8301530446056247680 次。第 1 个字母是 "a"。



提示：

    2 <= S.length <= 100
    S 只包含小写字母与数字 2 到 9 。
    S 以字母开头。
    1 <= K <= 10^9
    解码后的字符串保证少于 2^63 个字母。
-------------------------------------------------
"""
import time
import re

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
def decode_at_index(S, K):
    if re.match("[2-9]", S[0]):
        return False
    record = []
    i = 0
    count = 0
    while count < K and i < K:
        if not S[i].isdigit():
            count += 1
        else:
            count *= int(S[i])
        record.append((S[i], count))
        i += 1
    j = len(record) - 1
    K = K % record[j][1]
    print(record)
    while K != 0:
        # if re.match("[2-9]", record[j][0]):
        #     j -= 1
        #     K %= record[j][1]
        # else:
        #     j -= 1
        #     K -= 1
        # print(K, j, record[j][1])
        while K < record[j][1]:
            j -= 1
        K %= record[j][1]
        print("while K != 0:的时候", K, j, record[j][1])
    print("While K=0 de j ", j)
    while re.match("[2-9]", record[j][0]):
        j -= 1
    print(record[j][0])
    return record


# 看看大神的优秀方法
def decodeAtIndex(S, K):
    size = 0
    for i in S:
        if i.isdigit():
            size *= int(i)
        else:
            size += 1
    for index in reversed(S):
        K %= size
        if K == 0 and index.isalpha():
            return index
        if index.isdigit():
            size /= int(index)
        else:
            size -= 1
    return


# s_in = "a2345678999999999999999"
# k_in = 1
# s_in = "ha22"
# k_in = 5
# s_in = "leet2code3"
# k_in = 10
# s_in = "y959q969u3hb22odq595"
# k_in = 222280369
# s_in = "vk6u5xhq9v"
# k_in = 554
s_in = "vzpp636m8y"
k_in = 2920
print(decode_at_index(s_in, k_in))


# 判断一个字符是不是数字
# 正则的方法是
# import re
# return re.match('\d',x)
# python 内置了  isdigit() 和 isalpha() 函数
def is_digit(x):
    try:
        x = int(x)
        return isinstance(x, int)
    except ValueError:
        return False


# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
