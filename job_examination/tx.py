# n, k = list(map(int, input().split()))
# nodes = list(map(int, input().split()))
# print(n,k)
# print(nodes)
# nodes.pop(k - 1)
# print(' '.join(list(map(str,nodes))))

# import bisect
# s = input()
# n = len(s)
# k = int(input())
# res = []
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         ss = s[i:j]
#         if ss not in res:
#             if len(res) < k:
#                 bisect.insort(res, ss)
#             else:
#                 if ss < res[-1]:
#                     bisect.insort(res, ss)
#                     res.pop()
# # print(res)
# print(res[- 1])

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     res = 0
#     while n:
#         if n >= 10:
#             # print(9, (n - 9) % 10)
#             t = (n - 9) % 10 + 9
#             res += t
#             n = (n - t) // 10
#         else:
#             res += n
#             n = 0
#     print(res)

# n = 10
# a = [4, 1, 6, 7, 3, 2, 2, 8, 5, 9]
# a = [2,2,1,2,1]
#
# n = input()
a = list(map(int,input().split()))
def shua(ll):
    # print('lllllllll', ll)
    if not ll:
        return 0
    res = 1
    if len(ll) >= max(ll):
        kk = list(map(lambda x: x - 1, ll))
        kk.append(0)
        start = None
        tt = []
        for i, k in enumerate(kk):
            if k != 0:
                if start is None:
                    start = i
            else:
                if start is not None:
                    tt.append(kk[start:i])
                    start = None
        # print('ll,kk,tt',ll, kk, tt)
        for t in tt:
            res += shua(t)
    else:
        # print('ll',ll)
        ind = ll.index(max(ll))
        res += shua(ll[:ind]) + shua(ll[ind + 1:])
    return res


print(shua(a))

# # s = 'ababa'
# # lrs = [(1, 4), (1, 5), (1, 2), (1, 3)]
# s = input()
# n = len(s)
# cnt = int(input())
# lrs = []
# for _ in range(cnt):
#     lrs.append(list(map(int, input().split())))
# hw = [0 for _ in range(n)]
# for i in range(n // 2 + 1):
#     j = 1
#     while 0 <= i - j < i + j < n and s[i - j] == s[i + j]:
#         j += 1
#     hw[i] = j - 1
#     hw[n - i - 1] = j - 1
#
#
# # print('hw', hw)
#
#
# def ff(l, r):
#     print('l,r', l, r)
#     if l > r:
#         return 0
#     if l == r:
#         return 1
#     if l == r - 1:
#         return 2
#     t = 0
#     mi = 0
#     # k = []
#     for i in range(l, r + 1):
#         j = min(hw[i], i - l, r - i)
#         # k.append(j)
#         if j > t:
#             mi = i
#             t = j
#     # print('k', k, t, mi)
#     sl, sr = mi - t, mi + t
#     return ff(l, sl - 1) + 1 + ff(sr + 1, r)
#
#
# for ll, rr in lrs:
#     print(ff(ll - 1, rr - 1))
