import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


n, m = input_nums()
nums = []
vis = [[0] * m for _ in range(n)]
res = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(n):
    nums.append(input_nums())


def dfs(x, y):
    t = 0
    q = deque()
    q.append((x, y))
    vis[x][y] = 1
    while q:
        x, y = q.popleft()
        val = nums[x][y]
        t += 1
        # print(x, y, val)
        for i in range(4):
            # a, b = x + dx[i], y + dy[i]
            if val & 1 == 1 and dy[i] == -1:
                continue
            elif (val >> 1) & 1 == 1 and dx[i] == 1:
                continue
            elif (val >> 2) & 1 == 1 and dy[i] == 1:
                continue
            elif (val >> 3) & 1 == 1 and dx[i] == -1:
                continue
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < n and 0 <= b < m and vis[a][b] == 0:
                vis[a][b] = 1
                q.append((a, b))
    return t

for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            res.append(dfs(i, j))

res.sort(reverse=True)
print(*res, '')








