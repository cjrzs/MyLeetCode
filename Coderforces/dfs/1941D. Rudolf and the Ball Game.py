import threading

import sys

# input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def dfs(u, x):
    if (u, x) in vis:
        return
    vis.add((u, x))
    if u == m:
        res.add(x)
        return
    r, c = nums[u]
    r = int(r)
    if c != '1':
        t = (x + r) % n
        if t == 0: t = n
        dfs(u + 1, t)
    if c != '0':
        t = (x - r) % n
        if t == 0: t = n
        dfs(u + 1, t)


T = int(input())

for _ in range(T):
    res = set()
    vis = set()
    n, m, x = list(map(int, input().split(' ')))
    nums = []
    for _ in range(m):
        r, c = input().split(' ')
        nums.append((r, c))
    dfs(0, x)

    print(len(res))
    for i in range(1, n + 1):
        if i in res:
            print(i, end=" ")
    print()


