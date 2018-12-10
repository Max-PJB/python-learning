#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/10 19:57
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :  841. 钥匙和房间

    虚拟 用户通过次数 49
    虚拟 用户尝试次数 59
    虚拟 通过次数 49
    虚拟 提交次数 59
    题目难度 Medium

有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

最初，除 0 号房间外的其余所有房间都被锁住。

你可以自由地在房间之间来回走动。

如果能进入每个房间返回 true，否则返回 false。

示例 1：

输入: [[1],[2],[3],[]]
输出: true
解释:
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。

示例 2：

输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。

提示：

    1 <= rooms.length <= 1000
    0 <= rooms[i].length <= 1000
    所有房间中的钥匙数量总计不超过 3000。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        if n < 2:
            return True
        flag_key = [0 for _ in range(n)]
        # 拥有0号门的钥匙
        flag_key[0] = 1
        flag_room = [0 for _ in range(n)]
        stack_key = [0]
        while stack_key:
            kr_index = stack_key.pop()
            # 房间没有访问,那就访问
            if not flag_room[kr_index]:
                flag_room[kr_index] = 1
                # 打开这个房间，遍历里面的钥匙
                for key in rooms[kr_index]:
                    # 如果之前没有这把钥匙，就加入栈，并且 flag_key 标记 拥有这把钥匙
                    if not flag_key[key]:
                        stack_key.append(key)
                        flag_key[key] = 1
        if flag_key.count(1) < n:
            return False
        else:
            return True


# rooms_in = [[1],[2],[3],[]]
rooms_in = [[1,3],[3,0,1],[2],[0]]
res = Solution().canVisitAllRooms(rooms_in)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
