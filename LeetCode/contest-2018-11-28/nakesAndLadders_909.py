#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/28 12:24
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :     909. 爬坡和梯子

    虚拟 用户通过次数 2
    虚拟 用户尝试次数 4
    虚拟 通过次数 2
    虚拟 提交次数 4
    题目难度 Medium

在一块 N x N 的板子 board 上，从板的左下角开始，每一行交替方向，按从 1 到 N*N 的数字给方格编号。例如，对于一块 6 x 6 大小的板子，可以编号如下：

36 35 34 33 32 31
25 26 27 28 29 30
24 23 22 21 20 19
13 14 15 16 17 18
12 11 10 09 08 07
01 02 03 04 05 06

从板子的方块 1 开始（总是在最后一行、第一列）出发。

从方块 x 开始，每一次移动都包含以下内容：

    你选择一个目标方块 S，它的编号是 x+1，x+2，x+3，x+4，x+5，或者 x+6，只要这个数字满足 <= N*N。
    如果 S 有一个坡或梯子，你就移动到那个坡或梯子的目的地。否则，你会移动到 S。

在 r 行 c 列上的方格里有 “坡” 或 “梯子”；如果 board[r][c] != -1，那个坡或梯子的目的地将会是 board[r][c]。

注意，你每次移动最多只能爬过一个坡或梯子一次：就算目的地是另一个坡或梯子的起点，你也不会继续移动。

返回达到方格 N*N 所需的最少移动次数，如果不可能，则返回 -1。



示例：

输入：[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
输出：4
解释：
首先，从方格 1 [第 5 行，第 0 列] 开始。
你决定移动到方格 2，并必须爬过梯子移动到到方格 15。
然后你决定移动到方格 17 [第 3 行，第 5 列]，必须爬过坡到方格 13。
然后你决定移动到方格 14，且必须通过梯子移动到方格 35。
然后你决定移动到方格 36, 游戏结束。
可以证明你需要至少 4 次移动才能到达第 N*N 个方格，所以答案是 4。



提示：

    2 <= board.length = board[0].length <= 20
    board[i][j] 介于 1 和 N*N 之间或者等于 -1。
    编号为 1 的方格上没有坡或梯子。
    编号为 N*N 的方格上没有坡或梯子。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        N = n * n
        line = [0]
        while board:
            if board:
                ll = board.pop()
                line.extend(ll)
            if board:
                ll = board.pop()
                line.extend(ll[::-1])
        cnt = 0
        des = [1]
        queList1 = [1]
        queList2 = []
        # print(line)
        while N not in des:
            if queList1:
                cnt += 1
            while queList1:
                node = queList1.pop(0)
                for i in range(1, 7):
                    j = node + i
                    if j in des:
                        continue
                    else:
                        if j == N:
                            return cnt
                        elif j > N:
                            break
                        else:
                            des.append(j)
                            if line[j] == -1:
                                queList2.append(j)
                            else:
                                if line[j] == N:
                                    return cnt
                                else:
                                    if line[j] not in des:
                                        queList2.append(line[j])
            if queList2:
                cnt += 1
            while queList2:
                node = queList2.pop(0)
                for i in range(1, 7):
                    j = node + i
                    if j in des:
                        continue
                    else:
                        if j == N:
                            return cnt
                        elif j > N:
                            break
                        else:
                            des.append(j)
                            if line[j] == -1:
                                queList1.append(j)
                            else:
                                if line[j] == N:
                                    return cnt
                                else:
                                    if line[j] not in des:
                                        queList1.append(line[j])
            if not queList1 and not queList2:
                return -1

    # 太复杂了，看看大神的代码
    def snakesAndLadders2(self, board):
        n = len(board)
        need = {1: 0}
        bfs = [1]
        for x in bfs:
            for i in range(x + 1, x + 7):
                a, b = (i - 1) // n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0:
                    i = nxt
                if i == n * n:
                    return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1


# board_in = [[36, 35, 34, 33, 32, 31], [25, 26, 27, 28, 29, 30], [24, 23, 22, 21, 20, 19], [13, 14, 15, 16, 17, 18],
#             [12, 11, 10, 9, 8, 7], [1, 2, 3, 4, 5, 6]]
# board_in = [[1, 1, -1],[1, 1, 1],[-1, 1, 1]]
board_in = [[-1, -1, -1, 135, -1, -1, -1, -1, -1, 185, -1, -1, -1, -1, 105, -1],
            [-1, -1, 92, -1, -1, -1, -1, -1, -1, 201, -1, 118, -1, -1, 183, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, 179, -1, -1, -1, -1, -1, -1],
            [-1, 248, -1, -1, -1, -1, -1, -1, -1, 119, -1, -1, -1, -1, -1, 192],
            [-1, -1, 104, -1, -1, -1, -1, -1, -1, -1, 165, -1, -1, 206, 104, -1],
            [145, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 229, -1],
            [-1, -1, 75, 140, -1, -1, -1, -1, -1, -1, -1, -1, 43, -1, 34, -1],
            [-1, -1, -1, -1, -1, -1, 169, -1, -1, -1, -1, -1, -1, 188, -1, -1],
            [-1, -1, -1, -1, -1, -1, 92, -1, 171, -1, -1, -1, -1, -1, -1, 66],
            [-1, -1, -1, 126, -1, -1, 68, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, 109, -1, 86, 28, 228, -1, -1, 144, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, 59, -1, -1, -1, -1, -1, 51, -1, -1, -1, 62, -1],
            [-1, 71, -1, -1, -1, 63, -1, -1, -1, -1, -1, -1, 212, -1, -1, -1],
            [-1, -1, -1, -1, 174, -1, 59, -1, -1, -1, -1, -1, -1, 133, -1, -1],
            [-1, -1, 62, -1, 5, -1, 16, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, 59, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
res2 = Solution().snakesAndLadders2(board_in)
print(res2)
# res = Solution().snakesAndLadders(board_in)
# print(res)
# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
