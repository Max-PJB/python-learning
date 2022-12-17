# def gcd(a, b):
#     # print(a, b)
#     if b > a:
#         a, b = b, a
#     x, y = divmod(a, b)
#     if y == 0:
#         return b
#     else:
#         return gcd(b, y)
#
#
# # 1/8 + 3/8
# # 1/4 - 1/2
# # 1/8 * 3/8
# # 1/8 / 3/8
# first, oper, second = input().split()
# # print(first, oper, second)
# f_u, f_d = list(map(int, first.split('/')))
# s_u, s_d = list(map(int, second.split('/')))
# # print(f_u, f_d, s_u, s_d)
#
# if oper in ['+', '-']:
#     cd = gcd(f_d, s_d)
#     down = f_d * s_d // cd
#     # print('cd,down',cd,down)
#     if oper == '+':
#         up = f_u * s_d // cd + s_u * f_d // cd
#     else:
#         up = f_u * s_d // cd - s_u * f_d // cd
#         # print('else_up',up)
#
# else:
#     if oper == '/':
#         s_u, s_d = s_d, s_u
#     up = f_u * s_u
#     down = f_d * s_d
# if up == 0:
#     print(0)
# else:
#     tcd = abs(gcd(up, down))
#     # print('up,down,tcd',up,down,tcd)
#     fz = up // tcd
#     fm = down // tcd
#     # print(fz,fm)
#     if fm == 1:
#         print(fz)
#     else:
#         print('/'.join([str(fz), str(fm)]))


"""
4 4
0 0 0 1
1 0 0 0
1 1 1 0
0 0 0 0

2 3
0 1 0
0 0 1
"""
n, m = list(map(int, input().split()))
mat = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    t = set()
    for i, v in enumerate(tmp):
        if v == 1:
            t.add(i)
    # print(tmp, t)
    if t:
        mat.append(t)
# print(mat)
l = len(mat)
res = False


def pick(k, need, have):
    global res
    tk = mat[k]
    if tk == need:
        res = True
    elif k < l - 1:
        # 第 k 个不选
        pick(k + 1, need, have)
        if not have & tk:  # 已经拥有的 1 ，第 k 个不存在
            # 第 k 个选
            pick(k + 1, need - tk, have | tk)


haha = {i for i in range(m)}
for hehe in mat:
    haha -= hehe
if haha:
    print('NO')
else:
    pick(0, {i for i in range(m)}, set())
    if res:
        print("YES")
    else:
        print('NO')
