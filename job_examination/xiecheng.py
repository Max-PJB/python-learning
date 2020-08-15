a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
n = (len(a_list) + len(b_list) + 1) // 2

"""
300 500 650 700
200 275 330
"""


def find(a, b, k):
    # print(a, b, k)
    if not a:
        return b[k - 1]
    elif not b:
        return a[k - 1]
    elif k == 1:
        return min(a[0],b[0])
    else:
        if len(b) < len(a):
            a, b = b, a
        a_i = len(a) if len(a) < k // 2 else k // 2
        b_i = k - a_i
        # print('a_i,b_i', a_i, b_i)
        if a[a_i - 1] == b[b_i - 1]:
            return a[a_i - 1]
        elif a[a_i - 1] < b[b_i - 1]:
            return find(a[a_i:], b, k - a_i)
        else:
            return find(a, b[b_i:], k - b_i)


x = find(a_list, b_list, n)
print(x)

"""
给定一笔经费金额和一组旅游产品以及对应的价格。同一个产品可以重复购买多份。

问：最少能够购买多少份产品，正好花掉所有的经费。若没有任何一种产品组合能够正好花掉所有的经费，返回-1.
"""
# p_list = list(map(int, input().split()))
# m = int(input())
# p_list.sort()
# res = []
# """
# 10 20 50
# 110
# """
#
#
# def consumer(money, p_k, times):
#     cost = p_list[p_k]
#     t, y = divmod(money, cost)
#     if y == 0:
#         res.append(times + t)
#     elif p_k > 0:
#         for i in range(t + 1):
#             consumer(money - cost * i, p_k - 1, times + i)
#
#
# consumer(m, len(p_list) - 1, 0)
# if res:
#     # print(res)
#     print(min(res))
# else:
#     print(-1)