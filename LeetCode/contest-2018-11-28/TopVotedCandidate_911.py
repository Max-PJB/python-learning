#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/28 16:24
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :911. 在线选举

    用户通过次数 14
    用户尝试次数 35
    通过次数 14
    提交次数 94
    题目难度 Medium

在选举中，第 i 张票是在时间为 times[i] 时投给 persons[i] 的。

现在，我们想要实现下面的查询函数： TopVotedCandidate.q(int t) 将返回在 t 时刻主导选举的候选人的编号。

在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。

示例：

输入：["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
输出：[null,0,1,1,0,0,1]
解释：
时间为 3，票数分布情况是 [0]，编号为 0 的候选人领先。
时间为 12，票数分布情况是 [0,1,1]，编号为 1 的候选人领先。
时间为 25，票数分布情况是 [0,1,1,0,0,1]，编号为 1 的候选人领先（因为最近的投票结果是平局）。
在时间 15、24 和 8 处继续执行 3 个查询。



提示：

    1 <= persons.length = times.length <= 5000
    0 <= persons[i] <= persons.length
    times 是严格递增的数组，所有元素都在 [0, 10^9] 范围中。
    每个测试用例最多调用 10000 次 TopVotedCandidate.q。
    TopVotedCandidate.q(int t) 被调用时总是满足 t >= times[0]。
-------------------------------------------------
"""
import bisect
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        # self.time = [0]
        # vote = [persons[0]]
        # p_vote = set(persons)
        # p_index = dict(zip(p_vote, [i for i in range(len(p_vote))]))
        # p_win = [0 for _ in p_vote]
        # p_most_person = persons[0]
        # p_most_cnt = 0
        # for ind, peo in enumerate(persons):
        #     peo_index = p_index[peo]
        #     p_win[peo_index] += 1
        #     if peo == p_most_person:
        #         p_most_cnt += 1
        #     elif p_win[peo_index] >= p_most_cnt:
        #         vote.append(peo_index)
        #         self.time.append(times[ind])
        #         p_most_person, p_most_cnt = peo_index, p_win[peo_index]
        #     else:
        #         pass
        p_win = dict(zip(set(persons), [0 for _ in range(len(set(persons)))]))
        p_most_person = persons[0]
        p_most_cnt = 0
        self.time_vote = {0: p_most_person}
        for p, t in zip(persons, times):
            p_win[p] += 1
            if p == p_most_person:
                p_most_cnt += 1
            elif p_win[p] >= p_most_cnt:
                self.time_vote[t] = p
                p_most_person, p_most_cnt = p, p_win[p]
            else:
                pass
        self.time = sorted(self.time_vote.keys())
        # print(self.time, vote)
        # print(self.vote)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        # ind = bisect.bisect(self.time, t)
        # print(t, self.time_vote, self.time, ind, self.time[ind-1])
        """Return the index where to insert item x in list a, assuming a is sorted.

        The return value i is such that all e in a[:i] have e <= x, and all e in
        a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
        insert just after the rightmost x already there.

        Optional args lo (default 0) and hi (default len(a)) bound the
        slice of a to be searched.
        我们需要使用bisect模块来进行二分查找，前提我们的列表是一个有序的列表。
        bisect_right(a, x, lo=0, hi=None):
        在有序列表 a 中，返回 插入点，使得插入 x 后仍是有序列表的 插入位置 
        """
        return self.time_vote[self.time[bisect.bisect(self.time, t)-1]]


# topV = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
# print(topV.q(20))
# topV2 = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
topV3 = TopVotedCandidate([0, 0, 1, 1, 2], [0, 67, 69, 74, 87])
a = [1,2,3,4,5,6,6,8,9]
print(bisect)
# topV1 = TopVotedCandidate([0, 0, 0, 0, 1], [0, 6, 39, 52, 75])
# print(topV1.q(20))
for i in [[4], [62], [100], [88], [70], [73], [22], [75], [29], [10]]:
    print(topV3.q(i[0]), end=" ")
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
