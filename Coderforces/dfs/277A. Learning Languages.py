import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def merge(u, x):
    a, b = find(u), find(x)
    global flag
    flag = True
    if a != b:
        p[a] = b

flag = False
n, m = input_nums()
p = [0] * (n + m + 1)
for i in range(n + m + 1):
    p[i] = i

for i in range(1, n + 1):
    t = input_nums()
    for x in t[1:]:
        merge(x + n, i)
# print(p)
res = 0
for i in range(1, n + 1):
    if p[i] == i:
        res += 1
# print(flag)
if not flag:
    print(n)
else:
    print(res - 1)




