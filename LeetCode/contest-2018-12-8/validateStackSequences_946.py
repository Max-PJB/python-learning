#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/12/8 21:26
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :     946. 验证栈序列

    用户通过次数 117
    用户尝试次数 138
    通过次数 119
    提交次数 272
    题目难度 Medium

给定 pushed 和 popped 两个序列，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。



示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

示例 2：

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。



提示：

    0 <= pushed.length == popped.length <= 1000
    0 <= pushed[i], popped[i] < 1000
    pushed 是 popped 的排列。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start_time = time.time()


# 下面写上代码块
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        n = len(popped)
        if n < 3:
            return True
        pushed_map = {vu: i for i, vu in enumerate(pushed)}
        popped = list(map(lambda x: pushed_map[x], popped))
        pre = popped[0]
        already = {pre: 1}
        i = 1
        while i < n:
            cur = popped[i]
            already[cur] = 1
            if cur > pre:
                pre = cur
            elif cur < pre:
                for k in range(pre, cur, -1):
                    if k not in already:
                        print(cur, k, already)
                        return False
            else:
                pass
            i += 1
        return True

    # 人家的方法，非常可以
    def validateStackSequences2(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0
        for item in pushed:
            stack.append(item)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0


pushed = [2, 1, 0]
popped = [2, 0, 1]
res = Solution().validateStackSequences(pushed, popped)
print(res)
# 上面中间写上代码块
end_time = time.time()
print('Running time: %s Seconds' % (end_time - start_time))
