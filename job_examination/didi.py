n = int(input())
res = [[0 for _ in range(n)] for _ in range(n)]
fib = [1, 1]
for _ in range(n * n - 2):
    fib.append(fib[-2] + fib[-1])
x_min, y_min = 0, 0
x_max, y_max = n - 1, n - 1
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n_x, n_y = 0, 0
cnt = 1
res[n_x][n_y] = fib[-cnt]
direc = 0
while cnt < n * n:
    n_x, n_y = n_x + directions[direc][0], n_y + directions[direc][1]
    if x_min <= n_x <= x_max and y_min <= n_y <= y_max:
        cnt += 1
        res[n_x][n_y] = fib[-cnt]
    else:
        n_x, n_y = n_x - directions[direc][0], n_y - directions[direc][1]

        if direc == 0:
            x_min += 1
        elif direc == 1:
            y_max -= 1
        elif direc == 2:
            x_max -= 1
        elif direc == 3:
            y_min += 1
        direc = (direc + 1) % 4
for r in res:
    for k in r:
        print(k, end=' ')

#
# n = int(input())
# chars = []
# for _ in range(n):
#     chars.append(list(input()))
# # print(chars)
# target = ['C', 'H', 'I', 'N', 'A']
# directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# res = 0
#
#
# def dfs(i, j, k):
#     global res
#     if 0<= i < n and 0 <= j < n and chars[i][j] == target[k]:
#         if k == 4:
#             res += 1
#         else:
#             for direc in directions:
#                 dfs(i + direc[0], j + direc[1], k + 1)
#
#
# for i in range(n):
#     for j in range(n):
#         dfs(i, j, 0)
# print(res)
