import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def input_nums():
    return list(map(int, input().split(' ')))


n, m = map(int, input().strip().split(" "))
vis = [0] * (n + 1)
du = [0] * (n + 1)
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().strip().split(" "))
    du[a] += 1
    du[b] += 1
    g[a].append(b)
    g[b].append(a)

# print(du, g)


def dfs(u, pre, level, t):
    global res
    if level == 3:
        if u in vis:
            res = min(t, res)
        return
    vis.add(u)
    for x in g[u]:
        if x != pre:
            dfs(x, u, level + 1, t + du[x] - 2)


res = float("inf")
for i in range(1, n + 1):
    t = 0
    vis = set()
    dfs(i, -1, 1, du[i] - 2)


print(res if res != float("inf") else -1)









