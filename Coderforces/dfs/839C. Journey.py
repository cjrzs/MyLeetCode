import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


n = int(input())
g = defaultdict(list)
res = 0
for _ in range(n - 1):
    a, b = input_nums()
    g[a].append(b)
    g[b].append(a)

vis = set()
q = [(1, 1, 0)]
while q:
    u, cnt, num = q.pop()
    vis.add(u)
    deep = 0
    for x in g[u]:
        if x not in vis:
            deep += 1
    if deep == 0:
        res += cnt * num
    else:
        for x in g[u]:
            if x not in vis:
                q.append((x, cnt / deep, num + 1))
print(res)

