import sys
from collections import defaultdict, Counter

# sys.setrecursionlimit(8 ** 10)
input = sys.stdin.readline


g = [-1] * (10 ** 6 + 1)
for i in range(1, 10):
    g[i] = i


def dfs(x):
    if g[x] != -1:
        return g[x]
    q = 1
    u = x
    while u:
        t = u % 10
        if t != 0:
            q *= t
        u //= 10
    g[x] = dfs(q)
    return g[x]

#
for i in range(10, 10 ** 6 + 1):
    dfs(i)

# 1 ~ i 中满足g(x)=k 的数x的数量。
s = [[0] * 10 for _ in range(10 ** 6 + 1)]
for i in range(1, 10 ** 6 + 1):
    for j in range(1, 10):
        if j == g[i]:
            s[i][j] = s[i - 1][j] + 1
        else:
            s[i][j] = s[i - 1][j]


T = int(input())
for _ in range(T):
    l, r, k = list(map(int, input().split(" ")))
    print(s[r][k] - s[l - 1][k])



