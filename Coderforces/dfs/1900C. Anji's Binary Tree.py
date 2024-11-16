import sys
from collections import defaultdict, Counter
from typing import List

sys.setrecursionlimit(8 ** 10)
input = sys.stdin.readline


def dfs(u):
    l = g[u][0]
    r = g[u][1]
    if l != -1:
        dist[l] = dist[u] + 1
        if s[u] == 'L':
            dist[l] = dist[u]
        dfs(l)
    if r != -1:
        dist[r] = dist[u] + 1
        if s[u] == 'R':
            dist[r] = dist[u]
        dfs(r)


T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    g = []
    vis = set()
    for i in range(n):
        x, y = list(map(int, input().split(' ')))
        if x == y == 0:
            vis.add(i)
        g.append([x - 1, y - 1])
    dist = [0] * n
    # print(g)
    dfs(0)
    # print(dist)
    res = float("inf")
    for i in range(n):
        if i in vis:
            res = min(res, dist[i])
    print(res)

