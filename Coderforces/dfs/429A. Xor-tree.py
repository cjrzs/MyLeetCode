import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(8 ** 10)
input = sys.stdin.readline

from collections import defaultdict, deque

n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    x, y = list(map(int, input().split(' ')))
    g[y - 1].append(x - 1)
    g[x - 1].append(y - 1)
# print(g)
origin = list(map(int, input().split(' ')))
target = list(map(int, input().split(' ')))

cnt = 0
res = []
q = deque()

if origin[0] != target[0]:
    cnt += 1
    res.append(1)
    q.append((0, True, -1, False))
else:
    q.append((0, False, -1, False))

vis = set()
while q:
    u, t, pnode, pt = q.popleft()
    vis.add(u)
    for x in g[u]:
        if x not in vis:
            # print('------', x, origin[x], target[x], u, t, pnode, pt)
            w = 1 - origin[x] if pt else origin[x]
            if w != target[x]:
                cnt += 1
                res.append(x + 1)
                q.append((x, not pt, u, t))
            else:
                q.append((x, pt, u, t))
            vis.add(x)
print(cnt)
for x in res:
    print(x)

