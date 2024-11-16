import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


T = int(input())
for _ in range(T):
    n = int(input())
    id = [0] * (n + 1)
    f = [0] * (n + 1)
    f[1] = 1
    g = defaultdict(list)
    for i in range(1, n):
        a, b = input_nums()
        g[a].append((b, i))
        g[b].append((a, i))
    res = 0
    q = deque()
    q.append(1)
    while q:
        u = q.popleft()
        for x, i in g[u]:
            if f[x] == 0:
                f[x] = f[u] + int(i <= id[u])
                id[x] = i
                q.append(x)
        res = max(res, f[u])
    print(res)


