#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/1 22:19
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  864. 获取所有钥匙的最短路径

    用户通过次数 0
    用户尝试次数 4
    通过次数 0
    提交次数 6
    题目难度 Hard

给定一个二维网格 grid。 "." 代表一个空房间， "#" 代表一堵墙， "@" 是起点，（"a", "b", ...）代表钥匙，（"A", "B", ...）代表锁。

我们从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间。我们不能在网格外面行走，也无法穿过一堵墙。如果途经一个钥匙，我们就把它捡起来。除非我们手里有对应的钥匙，否则无法通过锁。

假设 K 为钥匙/锁的个数，且满足 1 <= K <= 6，字母表中的前 K 个字母在网格中都有自己对应的一个小写和一个大写字母。换言之，每个锁有唯一对应的钥匙，每个钥匙也有唯一对应的锁。另外，代表钥匙和锁的字母互为大小写并按字母顺序排列。

返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回 -1 。



示例 1：

输入：["@.a.#","###.#","b.A.B"]
输出：8

示例 2：

输入：["@..aA","..B#.","....b"]
输出：6



提示：

    1 <= grid.length <= 30
    1 <= grid[0].length <= 30
    grid[i][j] 只含有 '.', '#', '@', 'a'-'f' 以及 'A'-'F'
    钥匙的数目范围是 [1, 6]，每个钥匙都对应一个不同的字母，正好打开一个对应的锁。
-------------------------------------------------
"""
import time
from collections import namedtuple, deque

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        要求最短路径，采用广度优先搜索。用队列实现广度优先搜索。
        因为增加了钥匙，所以我们需要引入状态，以表达当前有多少钥匙。

        在同一个位置，若拥有的钥匙数目不同，则视为不同的状态，这些状态需要入队;
        若当前状态此前已经访问过（即钥匙数与坐标位置都相同视为同一个状态），则可跳过，无需访问。

        key只有6种，我们用一个int类型保存当前已经拥有的key的情况，只需要6bit。
        我们从起点开始搜索，遇到钥匙就更新记录，遇到墙就跳过，遇到門若有钥匙则通过，若没有钥匙则跳过。此外，如果当前
        状态已经遍历过，就跳过，否则加入队列，这些属于广度优先搜索的基本操作。
        ---------------------
        作者：goodluckcwl
        来源：CSDN
        原文：https://blog.csdn.net/u014230646/article/details/81189340
        版权声明：本文为博主原创文章，转载请附上博文链接！
        """
        # 定义网格节点
        GridNode = namedtuple("GridNode", ["i", "j", "keys"])
        n = len(grid)
        m = len(grid[0])

        # 初始化
        # 读取起点和钥匙所在的位置,找到 @ 的位置,和所有的钥匙,门
        start_x = 0
        start_y = 0
        key_list = []
        door_list = []
        # 包含所有钥匙，用6bit表示
        all_keys = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    start_x, start_y = i, j
                elif grid[i][j] in ["a", "b", "c", "d", "e", "f"]:
                    all_keys |= 1 << (ord(grid[i][j]) - ord("a"))
                    key_list.append(grid[i][j])
                elif grid[i][j] in ["A", "B", "C", "D", "E", "F"]:
                    door_list.append(grid[i][j])

        # grid_state 记录当前 每一个格子经过过的 (钥匙状态）,
        # 从一个格子到另一个格子能进行的前提必须满足 这个位置从来没有过这种状态
        # 钥匙最多 6 把 就用 000000 6位二进制表示
        # 这个 grid_state[i][j][x]=1 表示在 grid 中 i,j 位置 包含 （x）把 的钥匙的状态访问过
        grid_state = [[[0 for _ in range(2 ** len(key_list))] for _ in range(m)] for _ in range(n)]

        # 队列q，初始节点
        q = deque()
        q.append(GridNode(start_x, start_y, 0))

        # 搜索方向，左右上下
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]
        # 步数
        step = 0
        while q:
            nq = len(q)
            print("111")
            while nq:
                print("222",nq)
                print(q)
                nq -= 1
                node = q.popleft()
                # 已找到所有的钥匙
                if node.keys == all_keys:
                    return step
                for k in range(4):
                    next_x, next_y = node.i + x[k], node.j + y[k]
                    # 坐标越界,跳过
                    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                        continue
                    key_have = node.keys
                    # 访问相邻的节点
                    next_node = grid[next_x][next_y]
                    # 跳过 # 节点
                    if next_node == "#":
                        continue
                    # 如果是门
                    if next_node in door_list:
                        # 没有钥匙的话，跳过
                        if not key_have & (1 << (ord(next_node) - ord("A"))):
                            continue
                    # 如果是钥匙
                    if next_node in key_list:
                        # 更新钥匙
                        key_have |= (1 << (ord(next_node) - ord("a")))
                    # 如果是路，. #，那就不管了，后面再一起判断要不要访问这个点
                    # 判断开始，假设访问这个点，更新后的 key_state = key_have,
                    # 那么这个点 GridNode（next_x,next_y,key_have) 有没有出现过，若出现过，就不访问了
                    if grid_state[next_x][next_y][key_have] == 1:
                        continue
                    # 这下终于可以往下继续了，这个状态没有访问过，访问，加入队列
                    q.append(GridNode(next_x, next_y, key_have))
                    # 设置访问,表示已经访问过
                    grid_state[next_x][next_y][key_have] = 1
            # 处理下一层的节点
            step += 1
        return -1


# grid_in = ["@.a.#", "###.#", "b.A.B"]
# grid_in = ["@..aA", "..B#.", "....b"]
grid_in = ["@abcdeABCDEFf"]
res = Solution().shortestPathAllKeys(grid_in)
print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
