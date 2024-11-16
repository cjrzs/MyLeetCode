import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


n = int(input())
g = defaultdict(list)
root = None
res = []
for i in range(1, n + 1):
    a, b = input_nums()
    if a == -1:
        root = i
    else:
        g[a].append((i, b))
# print(g, root)


def dfs():
    q = deque()
    q.append((root, 0))
    while q:
        # print(q)
        u, k = q.popleft()
        flag = False
        for x, v in g[u]:
            # print(u, k, x, v)
            if v == 0:
                flag = True
            q.append((x, v))
        # print('---')
        if not flag and k == 1:
            res.append(u)


dfs()
if not res:
    print(-1)
else:
    res.sort()
    print(*res)





