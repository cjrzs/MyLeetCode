import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


n, m = input_nums()
nums = input_nums()
g = defaultdict(list)
res = 0
for _ in range(n - 1):
    a, b = input_nums()
    g[a].append(b)
    g[b].append(a)
# print(g)

def dfs():
    q = deque()
    q.append((1, 1, nums[0]))
    res = 0
    while q:
        u, pre, w = q.pop()
        if w > m:
            continue
        if len(g[u]) <= 1 and u != 1:
            res += 1
            continue
        for x in g[u]:
            if x != pre:
                if nums[x - 1]:
                    if nums[u - 1]:
                        t = w + 1
                    else:
                        t = 1
                else:
                    t = 0
                q.append((x, u, t))
    return res


print(dfs())

