import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


def solve():
    # print(g)
    if max(len(g[i]) for i in range(n + 1)) > 2:
        print(-1)
        return

    # def dfs(u, v, pre):
    #     # print(u, v, pre)
    #     # if len(g[u]) <= 1:
    #     #     return
    #     for x in g[u]:
    #         a, i = x
    #         if a != pre:
    #             # print(a, i)
    #             res[i] = v
    #             dfs(x[0], 5 - v, u)
    #
    # dfs(start, 2, -1)
    start = 1
    pre = -1
    v = 2
    while len(g[start]) != 1: start += 1
    q = [start]
    vis = set()
    vis.add(start)
    while q:
        cur = q.pop()
        for x, i in g[cur]:
            if x != pre and x not in vis:
                res[i] = v
                v = 5 - v
                q.append(x)
                vis.add(x)
    print(*res)
    return


T = int(input())
for _ in range(T):
    n = int(input())
    g = defaultdict(list)
    for i in range(n - 1):
        x, y = input_nums()
        g[x].append((y, i))
        g[y].append((x, i))

    res = [-1] * (n - 1)
    solve()



