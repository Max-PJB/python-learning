"""
可 今日 小 主要 参加 殿 选 可 今日 小 主要 参加 殿 选
小主 殿选
"""
a = input()
b = input().split()
c = ''.join(a.split())
print(c)
import re

print(b)
dd = []
for p in b:
    dd.extend([i.span() for i in re.finditer(p, c)])
print(dd)
a = list(a)
print(a)
blanks = []
st = 0
for i, f in enumerate(a):
    if f == ' ':
        blanks.append(i)
print(blanks)
for blank in blanks:
    for sta,end in dd:
        pass