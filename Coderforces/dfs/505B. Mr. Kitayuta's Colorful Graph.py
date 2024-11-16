import sys
from collections import defaultdict, Counter, deque
from copy import deepcopy


input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


def dfs(start, end, k):
    if start == end:
        return True
    for x in g[start]:
        if not vis[x] and k in colors[start][x]:
            vis[x] = True
            if dfs(x, end, k):
                return True
    return False


n, m = input_nums()
g = defaultdict(set)
colors = [[set() for _ in range(n + 1)] for _ in range(n + 1)]
total = set()
for i in range(m):
    a, b, c = input_nums()
    g[a].add(b)
    g[b].add(a)

    colors[a][b].add(c)
    colors[b][a].add(c)
    total.add(c)

# print(g)
k = int(input())

for _ in range(k):
    v, end = input_nums()
    res = 0
    for i in range(1, 101):
        vis = [False] * (n + 1)
        vis[v] = True
        if dfs(v, end, i):
            res += 1

    print(res)

