import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


n, m = input_nums()
g = defaultdict(list)
for _ in range(m):
    a, b = input_nums()
    g[a].append(b)
    g[b].append(a)
# print(g)

def bfs(i):
    q = deque()
    q.append((i, -1))
    vis[i] = 1
    d = set()
    while q:
        cur, pre = q.pop()
        d.add(cur)
        if len(g[cur]) == 2:
            for x in g[cur]:
                if x != pre and x not in d:
                    vis[x] = 1
                    d.add(x)
                    q.append((x, cur))
                if x in d and len(g[x]) == 2 and x != pre:
                    vis[x] = 1
                    if len(d) >= 3 and not q:
                        # print('success', d)
                        return True
    # print(d)
    return False


vis = [0] * (n + 1)
res = 0
for i in range(1, n + 1):
    if not vis[i]:
        # print(i)
        t = bfs(i)
        if t:
            res += 1
print(res)


