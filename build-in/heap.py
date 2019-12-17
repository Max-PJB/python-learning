#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_PengJB
    @   date    :       2019-7-16 14:38
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :    自己手撸的最大堆代码
-------------------------------------------------
"""


# 大根堆
class Heap:
    def __init__(self, array_list):
        self._heap = array_list
        self.length = len(self._heap)
        i = (self.length - 1) // 2
        for j in range(i, -1, -1):
            self._siftup(j)

    def _siftup(self, j):
        tmp = self._heap[j]
        while j < self.length // 2:
            child = self.left_child(j)
            if child + 1 < self.length:
                if self._heap[child + 1] > self._heap[child]:
                    child = child + 1
            if self._heap[child] > tmp:
                self._heap[j] = self._heap[child]
                j = child
                self._heap[child] = tmp
            else:
                break
        self._heap[j] = tmp

    def push(self, x):
        self.length += 1
        self._heap.append(x)
        j = self.length - 1
        while j > 0:
            parent = self.parent_pos(j)
            if self._heap[parent] < x:
                self._heap[j] = self._heap[parent]
                j = parent
            else:
                break
        self._heap[j] = x
        print(self._heap, self.length - 1)

    def get_max(self):
        print(self._heap)
        if self.length == 1:
            self.length -= 1
            return self._heap.pop(0)
        if self.length > 1:
            rr = self._heap[0]
            self._heap[0] = self._heap[self.length - 1]
            self.length -= 1
            self._heap.pop()
            self._siftup(0)
            return rr
        else:
            raise Exception("no nums")

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def parent_pos(i):
        return (i - 1) // 2


if __name__ == '__main__':
    heap = Heap([1, 3, 10, 22, 4, 665, 23, 5, 77, 46])
    # print(heap._heap)
    print(heap.get_max())
    # print(heap.get_max())
    # print(heap.get_max())
    # print(heap.get_max())
    # print(heap.get_max())
    # print(heap.get_max())
    # print(heap.get_max())
    # print(heap.get_max())
    # print(heap.get_max())
    # heap.push(2)
    # heap.push(3)
    # heap.push(4)
    # heap.push(5)
    # heap.push(6)
    # heap.push(4)
    # heap.push(3)
    # heap.push(2)
    # print(heap.get_max())
    # print(heap.get_max())
    # print(heap.get_max())
    # print(heap.get_max())
    import heapq
    haha = [1, 3, 10, 22, 4, 665, 23, 5, 77, 46]
    heapq.heapify(haha)
    print(heapq.heappop(haha))
    print(haha)
