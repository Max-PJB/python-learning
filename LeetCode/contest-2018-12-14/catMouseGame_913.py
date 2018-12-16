#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/14 14:50
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  913. 猫和老鼠

    用户通过次数 0
    用户尝试次数 11
    通过次数 0
    提交次数 28
    题目难度 Hard

两个玩家分别扮演猫（Cat）和老鼠（Mouse）在无向图上进行游戏，他们轮流行动。

该图按下述规则给出：graph[a] 是所有结点 b 的列表，使得 ab 是图的一条边。

老鼠从结点 1 开始并率先出发，猫从结点 2 开始且随后出发，在结点 0 处有一个洞。

在每个玩家的回合中，他们必须沿着与他们所在位置相吻合的图的一条边移动。例如，如果老鼠位于结点 1，那么它只能移动到 graph[1] 中的（任何）结点去。

此外，猫无法移动到洞（结点 0）里。

然后，游戏在出现以下三种情形之一时结束：

    如果猫和老鼠占据相同的结点，猫获胜。
    如果老鼠躲入洞里，老鼠获胜。
    如果某一位置重复出现（即，玩家们的位置和移动顺序都与上一个回合相同），游戏平局。

给定 graph，并假设两个玩家都以最佳状态参与游戏，如果老鼠获胜，则返回 1；如果猫获胜，则返回 2；如果平局，则返回 0。



示例：

输入：[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
输出：0
解释：
4---3---1
|   |
2---5
 \ /
  0



提示：

    3 <= graph.length <= 200
    保证 graph[1] 非空。
    保证 graph[2] 包含非零元素。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution:
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        def a_to_b(a,b):
            """
            :param a:int
            :param b: int
            :return:
            节点a到节点b的最短路径
            """
        def mouse_step(mouse,cat):
            """
            :param mouse:int
            :param cat: int
            :return:
            老鼠走一步：
            1，保证猫再走一步不会抓到老鼠
                2，离0点的距离更近
            """
        def cat_step(mouse,cat):
            """
            :param mouse:int
            :param cat: int
            :return:
            猫走一步：
            1，老鼠到0点的最短路径上，猫能比老鼠最少先到一个节点
                2，离老鼠距离更近
            """


# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
