"""
小团深谙保密工作的重要性，因此在某些明文的传输中会使用一种加密策略，小团如果需要传输一个字符串S，则他会为这个字符串添加一个头部字符串和一个尾部字符串。头部字符串满足至少包含一个“MT”子序列，且以T结尾。尾部字符串需要满足至少包含一个“MT”子序列，且以M开头。例如AAAMT和MAAAT都是一个合法的头部字符串，而MTAAA就不是合法的头部字符串。很显然这样的头尾字符串并不一定是唯一的，因此我们还有一个约束，就是S是满足头尾字符串合法的情况下的最长的字符串。

很显然这样的加密策略是支持解码的，给出你一个加密后的字符串，请你找出中间被加密的字符串S。
样例输入
10
MMATSATMMT
样例输出
SATM
"""
# n = int(input())
# ss = input()
# i = 0
# print(n, ss)
# while ss[i] != 'M':
#     i += 1
# while ss[i] != 'T':
#     i += 1
# j = n - 1
# while ss[j] != 'T':
#     j -= 1
# while ss[j] != 'M':
#     j -= 1
# print(''.join(ss[i + 1:j]))

"""
题目描述：
美团打算选调n名业务骨干到n个不同的业务区域，本着能者优先的原则，公司将这n个人按照业务能力从高到底编号为1~n。编号靠前的人具有优先选择的权力，每一个人都会填写一个意向，这个意向是一个1~n的排列，表示一个人希望的去的业务区域顺序，如果有两个人同时希望去某一个业务区域则优先满足编号小的人，每个人最终只能去一个业务区域。

例如3个人的意向顺序都是1 2 3，则第一个人去1号区域，第二个人由于1号区域被选择了，所以只能选择2号区域，同理第三个人只能选择3号区域。

最终请你输出每个人最终去的区域。



输入描述
输入第一行是一个正整数n，表示业务骨干和业务区域数量。（n≤300）

接下来有n行，每行n个整数，即一个1~n的排列，第 i 行表示 i-1 号业务骨干的意向顺序。

输出描述
输出包含n个正整数，第 i 个正整数表示第 i 号业务骨干最终去的业务区域编号。


样例输入
5
1 5 3 4 2 
2 3 5 4 1 
5 4 1 2 3 
1 2 5 4 3 
1 4 5 2 3
样例输出
1 2 5 4 3
"""
# n = int(input())
# picked = set()
# res = [None for _ in range(n)]
# for i in range(n):
#     wants = list(map(int, input().split()))
#     # print('res', res)
#     # print(i + 1, 'wantts', wants)
#     for j in wants:
#         if j not in picked:
#             res[i] = j
#             picked.add(j)
#             break
# for r in res:
#     print(r, end=' ')

"""
题目描述：
小团惹小美生气了，小美要去找小团“讲道理”。小团望风而逃，他们住的地方可以抽象成一棵有n个结点的树，小美位于x位置，小团位于y位置。小团和小美每个单位时间内都可以选择不动或者向相邻的位置转移，假设小美足够聪明，很显然最终小团会无路可逃，只能延缓一下被“讲道理”的时间，请问最多经过多少个单位时间后，小团会被追上。



输入描述
输入第一行包含三个整数n，x，y，分别表示树上的结点数量，小美所在的位置和小团所在的位置。(1<=n<=50000)

接下来有n-1行，每行两个整数u，v，表示u号位置和v号位置之间有一条边，即u号位置和v号位置彼此相邻。

输出描述
输出仅包含一个整数，表示小美追上小团所需的时间。


样例输入
5 1 2
2 1
3 1
4 2
5 3
样例输出
2
"""


class Node:
    def __init__(self, k):
        self.val = k
        self.next = []

    def get_deep(self):
        if self.next:
            return 1 + max([ne.get_deep() for ne in self.next])
        else:
            return 1


n, x, y = list(map(int, input().split()))
edges = []
for _ in range(n - 1):
    edges.append(list(map(int, input().split())))
root = Node(x)
cur_level = {x: root}
level = 1
y_level = 0
all_nodes = [root]
y_node = None
while edges:
    t = []
    level_nodes = {}
    for a, b in edges:
        if a in cur_level:
            level_nodes[b] = Node(b)
            cur_level[a].next.append(level_nodes[b])
        elif b in cur_level:
            level_nodes[a] = Node(a)
            cur_level[b].next.append(level_nodes[a])
        else:
            t.append([a, b])
    edges = t
    cur_level = level_nodes
    level += 1
    if y in cur_level:
        y_level = level
        y_node = cur_level[y]
    all_nodes.extend(cur_level.values())
path = [y_node]
cur = y_node
while root not in path:
    for node in all_nodes:
        if cur in node.next:
            path.append(node)
            cur = node
            break
ss = len(path)
print(path[(ss-1)//2].get_deep())
# def p_node(r):
#     print(r.val)
#     for i in r.next:
#         print(i.val, end=' ')


# print('y_level', y_level, 'level', level)
# p_node(root)
# print('')
# for i in root.next:
#     p_node(i)
#     print(' ')
# print('root.get_deep()', root.get_deep())

"""
题目描述：
小团从某不知名论坛上突然得到了一个测试默契度的游戏，想和小美玩一次来检验两人的默契程度。游戏规则十分简单，首先有给出一个长度为n的序列，最大值不超过m。

小团和小美各自选择一个[1,m]之间的整数，设小美选择的是l，小团选择的是r，我们认为两个人是默契的需要满足以下条件:

1. l 小于等于r。

2. 对于序列中的元素x，如果0<x<l,或r<x<m+1,则x按其顺序保留下来，要求保留下来的子序列单调不下降。

小团为了表现出与小美最大的默契，因此事先做了功课，他想知道能够使得两人默契的二元组<l,r>一共有多少种。

我们称一个序列A为单调不下降的，当且仅当对于任意的i>j,满足A_i>=A_j。



输入描述
输入第一行包含两个正整数m和n，表示序列元素的最大值和序列的长度。(1<=n,m<=100000)

输入第二行包含n个正整数，表示该序列。

输出描述
输出仅包含一个整数，表示能使得两人默契的二元组数量。


样例输入
5 5
4 1 4 1 2
样例输出
10
"""
# m, n = list(map(int, input().split()))
# xs = list(map(int, input().split()))
# ls = []
# rs = []
# # print('m,n,xs', m, n, xs)
#
#
# def chuli(alist):
#     # print('alist', alist)
#     i = 0
#     j = n - 1
#     while i < n and alist[i] is None:
#         i += 1
#     while j >= 0 and alist[j] is None:
#         j -= 1
#     alist = list(filter(lambda x: x is not None, alist))
#     p = 0
#     # print(alist)
#     while p < len(alist) - 1:
#         if alist[p] > alist[p + 1]:
#             return False, None, None
#         p += 1
#     return True, i, j
#
#
# for i in range(1, m + 1):
#     lt = []
#     rt = []
#     for k in xs:
#         if 0 < k < i:
#             lt.append(k)
#         else:
#             lt.append(None)
#         if i < k < m + 1:
#             rt.append(k)
#         else:
#             rt.append(None)
#     # print('lt: ', lt, 'rt: ', rt)
#     # print('zheshi_i: ', i)
#     ls.append(chuli(lt))
#     rs.append(chuli(rt))
# # print(ls)
# # print(rs)
# res = 0
# for i, (a, ai, aj) in enumerate(ls):
#     for j in range(i, len(rs)):
#         b, bi, bj = rs[j]
#         if a and b:
#             if ai > aj or bi > bj:
#                 res += 1
#             elif aj < bi:
#                 res += 1
# print(res)

"""
题目描述：
小团是一个莫得感情的CtrlCV大师，他有一个下标从1开始的序列A和一个初始全部为-1的序列B，两个序列的长度都是n。他会进行若干次操作，每一次操作，他都会选择A序列中一段连续区间，将其粘贴到B序列中的某一个连续的位置，在这个过程中他也会查询B序列中某一个位置上的值。

我们用如下的方式表示他的粘贴操作和查询操作：

粘贴操作：1  k x y，表示把A序列中从下标x位置开始的连续k个元素粘贴到B序列中从下标y开始的连续k个位置上，原始序列中对应的元素被覆盖。（数据保证不会出现粘贴后k个元素超出B序列原有长度的情况）

查询操作：2 x，表示询问当前B序列下标x处的值是多少。



输入描述
输入第一行包含一个正整数n，表示序列A和序列B的长度。(1<=n<=2000)

输入第二行包含n个正整数，表示序列A中的n个元素，第 i 个数字表示下标为 i 的位置上的元素，每一个元素保证在10^9以内。

输入第三行是一个操作数m，表示进行的操作数量。(1<=m<=2000)

接下来m行，每行第一个数字为1或2，具体操作细节详见题面。

输出描述
对于每一个操作2输出一行，每行仅包含一个整数，表示针对某一个询问的答案。


样例输入
5
1 2 3 4 5 
5
2 1
2 5
1 2 3 4
2 3
2 5
样例输出
-1
-1
-1
4

提示
输入样例2
5
1 2 3 4 5 
9
1 2 3 4
2 3
2 5
1 2 2 3
2 1
2 2
2 3
2 4
2 5

输出样例2
-1
4
-1
-1
2
3
4
"""