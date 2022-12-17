# n = int(input())
# for _ in range(n):
#     t, v1, v2, v3, v4 = list(map(int, input().split()))
#     # print('t, v1, v2, v3, v4 ', t, v1, v2, v3, v4)
#     cur = 0
#     arrive = {0: 0}
#     # cur = n
#     # arrive = {n: 0}
#     beixuan = {}
#     while t not in arrive:
#         cost = arrive[cur]
#
#         # n_v = [(cur + 1, cost + v3), (cur - 1, cost + v4)]
#         # if cur % 3 == 0:
#         #     n_v.append((cur // 3, cost + v1))
#         # if cur % 2 == 0:
#         #     n_v.append((cur // 2, cost + v2))
#
#         n_v = [(cur * 3, cost + v1), (cur * 2, cost + v2), (cur - 1, cost + v3), (cur + 1, cost + v4)]
#         # print(n_v, beixuan, arrive)
#         for k, v in n_v:
#             if k > 0:
#                 if k in beixuan:
#                     beixuan[k] = min(beixuan[k], v)
#                 else:
#                     beixuan[k] = v
#         minv = min(beixuan.values())
#         for k, v in beixuan.items():
#             if v == minv:
#                 cur = k
#                 arrive[k] = v
#                 beixuan.pop(k)
#                 break
#     print(arrive[t])
#     # print('arr',arrive[t])
"""
8
1 1 1 1 10000
2 10 1000 1 10000
13 1 1 1 1
100 1 1 1 1
256 1 1 1 1
256 1 2 1 1
114514 1 1 1 1
1000000000 1000000000 1000000000 1000000000 1000000000
"""
n = int(input())
import random
for _ in range(n):
    print(random.random()>0.5)