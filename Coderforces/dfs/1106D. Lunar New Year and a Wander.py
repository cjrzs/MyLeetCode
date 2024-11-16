import heapq
from collections import defaultdict

n, m = map(int, input().split(' '))
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split(' '))
    g[a].append(b)
    g[b].append(a)


vis = [0] * (n + 1)
q = [1]
heapq.heapify(q)

res = []
while q:
    # print(q)
    t = heapq.heappop(q)
    # print(t)
    vis[t] = 1
    res.append(t)
    for x in g[t]:
        # print(x)
        if not vis[x]:
            vis[x] = 1
            heapq.heappush(q, x)
    # print(q)
print(*res)

