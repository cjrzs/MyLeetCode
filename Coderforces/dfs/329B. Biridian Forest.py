import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def input_nums():
    return list(map(int, input().split(' ')))


n, m = input_nums()
nums = []
p = []
start = None
end = None
dist = [[float("inf")] * m for _ in range(n)]
for i in range(n):
    t = []
    for j, x in enumerate(list(input().strip())):
        t.append(x)
        if x == 'S':
            start = (i, j)
        elif x == 'E':
            end = (i, j, 0)
        elif x == 'T':
            dist[i][j] = 0
        else:
            c = int(x)
            if c > 0:
                p.append((i, j, c))

    nums.append(t)

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
res = 0
q = deque()
q.append(end)

while q:
    x, y, d = q.popleft()
    if dist[x][y] <= d:
        continue
    dist[x][y] = d
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < n and 0 <= b < m and dist[a][b] > d + 1:
            q.append((a, b, d + 1))

l = dist[start[0]][start[1]]
res = 0
for a, b, w in p:
    if dist[a][b] <= l:
        res += w
print(res)
#
#
#
#
#
import sys

input = lambda: sys.stdin.readline().rstrip()
from collections import deque

R, C = map(int, input().split())
A = []
for _ in range(R):
    A.append(input())

my = None
v, E = deque([]), []
INF = float('inf')
seen = [[INF] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if A[i][j] == 'E':
            v.append((i, j, 0))
        elif A[i][j] == 'S':
            my = (i, j)
        elif A[i][j] == 'T':
            seen[i][j] = 0
        else:
            c = int(A[i][j])
            if c > 0:
                E.append((i, j, c))

while v:
    r, c, d = v.popleft()
    if seen[r][c] <= d: continue
    seen[r][c] = d

    for r1, c1 in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr = r + r1
        nc = c + c1
        if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
        if seen[nr][nc] <= d + 1: continue
        v.append((nr, nc, d + 1))

ans = 0
d = seen[my[0]][my[1]]
for i, j, c in E:
    if seen[i][j] <= d:
        ans += c
print(ans)