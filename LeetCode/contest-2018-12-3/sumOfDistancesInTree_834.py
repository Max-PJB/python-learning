#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/3 22:30
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    834. 树中距离之和

    用户通过次数 1
    用户尝试次数 8
    通过次数 1
    提交次数 18
    题目难度 Hard

给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。

第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。

返回一个表示节点 i 与其他所有节点距离之和的列表 ans。

示例 1:

输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
输出: [8,12,6,10,10,10]
解释:
如下为给定的树的示意图：
  0
 / \
1   2
   /|\
  3 4 5

我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。

说明: 1 <= N <= 10000
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        sons = [[] for _ in range(N)]
        for edge in edges:
            sons[edge[0]].append(edge[1])
            sons[edge[1]].append(edge[0])
        print(sons)
        answer = [0 for _ in range(N)]
        for index in range(N):
            already = [index]
            stack1 = [index]
            stack2 = []
            step = 0
            while stack1 or stack2:
                if stack1:
                    step += 1
                while stack1:
                    son = sons[stack1.pop()]
                    for so in son:
                        if so not in already:
                            answer[index] += step
                            stack2.append(so)
                            already.append(so)
                if stack2:
                    step += 1
                while stack2:
                    son = sons[stack2.pop()]
                    for so in son:
                        if so not in already:
                            answer[index] += step
                            stack1.append(so)
                            already.append(so)
        return answer


N = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
res = Solution().sumOfDistancesInTree(N, edges)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
