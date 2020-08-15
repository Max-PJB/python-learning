# if __name__ == '__main__':
# a = input()
# b = input()
# from collections import Counter
#
# if Counter(a) == Counter(b):
#     print(True)
# else:
#     print(False)
# a = int(input())
# p = [0 for _ in range(10001)]
# p[0] = 1
# p[1] = 1
# ps = []
# i = 2
# while i < 10001:
#     if p[i] == 0:
#         ps.append(i)
#     for j in ps:
#         if i*j < 10001:
#             p[i * j] = 1
#     i += 1
# n = len(ps)
# i = 0
# res = 0
# while ps[i] <= a:
#     t = 0
#     j = i
#     s = ps[i]
#     while s < a:
#         j += 1
#         s += ps[j]
#     if s == a:
#         # print(ps[i:j+1])
#         res += 1
#     i += 1
# print(res)

if __name__ == '__main__':
    """
    4 6
    2 9
    2 9
    1 5
    5 99
    """
    n, m = list(map(int, input().split()))
    cost_reward = []
    for _ in range(n):
        cost_reward.append(list(map(int, input().split())))
    cost_reward.sort(key=lambda x: x[0])
    # print(n, m, cost_reward)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        cost, reward = cost_reward[i - 1]
        for j in range(m + 1):
            if j < cost:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + reward)
    for d in dp:
        print(d)
    print(max(dp[n]))
