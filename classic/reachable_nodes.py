#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/7 13:55
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 882. 细分图中的可到达结点

    用户通过次数 1
    用户尝试次数 2
    通过次数 1
    提交次数 2
    题目难度 Hard

从具有 0 到 N-1 的结点的无向图（“原始图”）开始，对一些边进行细分。

该图给出如下：edges[k] 是整数对 (i, j, n) 组成的列表，使 (i, j) 是原始图的边。

n 是该边上新结点的总数

然后，将边 (i, j) 从原始图中删除，将 n 个新结点 (x_1, x_2, ..., x_n) 添加到原始图中，

将 n+1 条新边 (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) 添加到原始图中。

现在，你将从原始图中的结点 0 处出发，并且每次移动，你都将沿着一条边行进。

返回最多 M 次移动可以达到的结点数。



示例 1：

输入：edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
输出：13
解释：
在 M = 6 次移动之后在最终图中可到达的结点如下所示。

示例 2：

输入：edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
输出：23



提示：

    0 <= edges.length <= 10000
    0 <= edges[i][0] < edges[i][1] < N
    不存在任何 i != j 情况下 edges[i][0] == edges[j][0] 且 edges[i][1] == edges[j][1].
    原始图没有平行的边。
    0 <= edges[i][2] <= 10000
    0 <= M <= 10^9
    1 <= N <= 3000
-------------------------------------------------
"""
import collections
import heapq
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
# class Solution(object):
#     def reachableNodes(self, edges, M, N):
#         # 解题错误，这其实是一个最短路径的问题
#         global res_cnt
#         res_cnt = 0
#         # 一个层次遍历的变种
#         node_to_node = [{} for _ in range(N)]
#         node_visited = [0 for _ in range(N)]
#         for edge in edges:
#             node1_index = edge[0]
#             node2_index = edge[1]
#             nodes_num = edge[2]
#             node_to_node[node1_index][node2_index] = nodes_num
#             node_to_node[node2_index][node1_index] = nodes_num
#
#         # 从 某个点开始往下走 K 步
#         def walk(node_index, k):
#             global res_cnt
#             if not node_visited[node_index]:
#                 node_visited[node_index] = 1
#                 res_cnt += 1
#                 k -= 1
#                 for next_node_index, to_node_num in node_to_node[node_index].items():
#                     if k > to_node_num:
#                         res_cnt += to_node_num
#                         node_to_node[next_node_index][node_index] = 0
#                         walk(next_node_index, k - to_node_num)
#                     else:
#                         res_cnt += k
#                         nodes_num_left = to_node_num - k
#                         node_to_node[next_node_index][node_index] = nodes_num_left
#
#         print(node_to_node)
#         print(node_visited)
#         walk(0, M + 1)
#         print(node_to_node)
#         print(node_visited)
#         print(res_cnt)
#         return res_cnt
class Solution(object):
    def reachableNodes(self, edges, M, N):
        """
        最短路径问题：
        方法：Dijkstra 算法

        思路

        将原始图作为加权无向图处理，我们可以使用 Dijkstra 算法查找原始图中的所有可到达结点。
        但是，这不足以解决仅部分使用细分边的示例。
        当我们沿着边（沿任一方向）行进时，我们可以跟踪我们使用它的程度。
        最后，我们想知道我们在原始图中到达的每个结点，以及每条边的利用率之和。

        算法
        我们使用 Dijkstra 算法 来找出从源到所有目标的最短距离。
        这是一个教科书算法， 请参阅此链接https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm了解详细信息。
        另外，对于每条（有向）边 (node，nei)，我们将跟踪有多少新结点（从原始边细分而来的新结点）被使用。
        最后，我们将总结每条边的利用率。
        """
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0

        while pq:
            d, node = heapq.heappop(pq)
            print(d,node)
            if d > dist[node]: continue
            # Each node is only visited once.  We've reached
            # a node in our original graph.
            ans += 1

            for nei, weight in graph[node].items():
                # M - d is how much further we can walk from this node;
                # weight is how many new nodes there are on this edge.
                # v is the maximum utilization of this edge.
                v = min(weight, M - d)
                used[node, nei] = v

                # d2 is the total distance to reach 'nei' (neighbor) node
                # in the original graph.
                d2 = d + weight + 1
                if d2 < dist.get(nei, M+1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2

        # At the end, each edge (u, v, w) can be used with a maximum
        # of w new nodes: a max of used[u, v] nodes from one side,
        # and used[v, u] nodes from the other.
        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans


edges = [[0,2,3],[0,4,4],[2,3,8],[1,3,5],[0,3,9],[3,4,6],[0,1,5],[2,4,6],[1,2,3],[1,4,1]]
M = 8
N = 5
res = Solution().reachableNodes(edges,M,N)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
