#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/7 10:53
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :   864. 获取所有钥匙的最短路径

    虚拟 用户通过次数 0
    虚拟 用户尝试次数 0
    虚拟 通过次数 0
    虚拟 提交次数 0
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
import copy

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]
        # state 记录当前 每一个格子 (钥匙状态）,
        # 从一个格子到另一个格子能进行的前提必须满足 钥匙变多
        # 钥匙最多 6 把 就用 000000 6位二进制表示
        init_state = [[None for _ in range(m)] for _ in range(n)]
        # 找到 @ 的位置,和所有的钥匙
        start_x = 0
        start_y = 0
        keys = []
        doors = []
        keys_int = 0
        keys_cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    start_x, start_y = i, j
                    init_state[i][j] = 0
                elif grid[i][j] in ["a", "b", "c", "d", "e", "f"]:
                    keys_int |= 1 << (ord(grid[i][j]) - ord("a"))
                    keys_cnt += 1
                    keys.append(grid[i][j])
                elif grid[i][j] in ["A", "B", "C", "D", "E", "F"]:
                    doors.append(grid[i][j])

        print(start_x, start_y, keys_int, keys, doors)
        r = []
        steps = 0
        luxian = [(start_x, start_y)]

        def next_step(arg_x, arg_y, cur_sta, step_cnt, luxian):
            cur_keys = cur_sta[arg_x][arg_y]
            if cur_keys == keys_int:
                # r.append((step_cnt, arg_x, arg_y, luxian, cur_sta))
                r.append(step_cnt)
            else:
                for k in range(4):
                    next_x, next_y = arg_x + x[k], arg_y + y[k]
                    next_state = copy.deepcopy(cur_sta)
                    next_steps_count = step_cnt + 1
                    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                        # 超出边界就退出啦
                        continue
                    elif grid[next_x][next_y] == "#":
                        # 这个方向是墙就不要走了
                        continue
                    else:
                        next_keys = next_state[next_x][next_y]
                        next_grid = grid[next_x][next_y]
                        if next_grid == "." or next_grid == "@":
                            if next_keys is None or cur_keys > next_keys:
                                next_state[next_x][next_y] = cur_keys
                                next_step(next_x, next_y, next_state, next_steps_count, luxian + [(next_x, next_y)])
                        elif next_grid in keys:
                            # 更新钥匙，人家一步就搞定：
                            key_int = 1 << (ord(next_grid) - ord("a"))
                            if (cur_keys & key_int) > 0:
                                # 已经拥有这把钥匙了
                                if next_keys is None or cur_keys > next_keys:
                                    next_state[next_x][next_y] = cur_keys
                                    next_step(next_x, next_y, next_state, next_steps_count, luxian + [(next_x, next_y)])
                            else:
                                # 这把钥匙的位置还没有走过
                                # 看人家更新钥匙的操作，多骚气
                                next_state[next_x][next_y] = cur_keys | key_int
                                next_step(next_x, next_y, next_state, next_steps_count, luxian + [(next_x, next_y)])
                        elif next_grid in doors:
                            # 如果是门，就检查有没有这把门的钥匙
                            door_key = 1 << (ord(next_grid) - ord("A"))
                            if (cur_keys & door_key) > 0:
                                # print("门是{}，我又这个门的钥匙".format(next_grid))
                                # 有这个门的钥匙
                                next_state[next_x][next_y] = cur_keys
                                next_step(next_x, next_y, next_state, next_steps_count, luxian + [(next_x, next_y)])

        next_step(start_x, start_y, init_state, steps, luxian)
        # print(len(r), r)
        # return min(list(map(lambda x: x[0], r)))
        return min(r)


# grid_in = ["@.a.#", "###.#", "b.A.B"]
grid_in = ["@..aA", "..B#.", "....b"]
res = Solution().shortestPathAllKeys(grid_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
