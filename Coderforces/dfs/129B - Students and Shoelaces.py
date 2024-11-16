from collections import defaultdict, deque

n, m = list(map(int, input().split(' ')))
g = defaultdict(list)
du = defaultdict(int)
res = 0
for _ in range(m):
    a, b = list(map(int, input().split(' ')))
    g[a].append(b)
    g[b].append(a)
    du[a] += 1
    du[b] += 1
# print(g)
q = deque()
for u in range(1, n + 1):
    if du[u] == 1:
        q.append(u)

while q:
    l = len(q)
    # print(q)
    for i in range(l):
        x = q.popleft()
        du[x] -= 1
        for u in g[x]:
            du[u] -= 1
    res += 1
    for u in range(1, n + 1):
        if du[u] == 1:
            q.append(u)
print(res)


