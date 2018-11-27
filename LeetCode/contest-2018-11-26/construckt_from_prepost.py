#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2018/11/26 20:11
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description : 889. 根据前序和后序遍历构造二叉树

    虚拟 用户通过次数 7
    虚拟 用户尝试次数 8
    虚拟 通过次数 7
    虚拟 提交次数 8
    题目难度 Medium

返回与给定的前序和后序遍历匹配的任何二叉树。

 pre 和 post 遍历中的值是不同的正整数。



示例：

输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]



提示：

    1 <= pre.length == post.length <= 30
    pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
    每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()


# 下面写上代码块
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        left = pre[1]
        right = post[-2]
        if left == right:
            root.left = self.constructFromPrePost(pre[1::], post[:post.index(right) + 1:])
            return root
        # left_pre = pre[1:pre.index(right):]
        # left_post = post[:post.index(left) + 1:]
        # root.left = self.constructFromPrePost(left_pre, left_post)
        # right_pre = pre[pre.index(right)::]
        # right_post = post[post.index(left) + 1:post.index(right) + 1:]
        # root.right = self.constructFromPrePost(right_pre, right_post)
        root.left = self.constructFromPrePost(pre[1:pre.index(right):], post[:post.index(left) + 1:])
        root.right = self.constructFromPrePost(pre[pre.index(right)::],
                                               post[post.index(left) + 1:post.index(right) + 1:])
        return root


pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]
pre1 = [2, 1, 3]
post1 = [3, 1, 2]
res1 = Solution().constructFromPrePost(pre1, post1)


def dfs(k):
    """
    :param k:TreeNode
    :return: None
    """
    if k.left:
        dfs(k.left)
    print(k.val)
    if k.right:
        dfs(k.right)


dfs(res1)

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))
