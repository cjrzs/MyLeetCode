import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    a, b, w = input_nums()
    g[a].append((b, w))
    g[b].append((a, w))
# print(g)

res = 0
def dfs(u, v, pre):
    # print(u, v, pre)
    global res
    res = max(res, v)
    for x, w in g[u]:
        if x != pre:
            dfs(x, v + w, u)

dfs(0, 0, -1)
print(res)



