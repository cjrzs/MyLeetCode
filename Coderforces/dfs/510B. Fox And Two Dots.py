import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


n, m = input_nums()
nums = []
for _ in range(n):
    nums.append(list(input().strip()))
# print(nums)
vis = [[0] * m for _ in range(n)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]


def bfs(i, j):
    q = [(i, j, -1, -1)]
    vis[i][j] = 1
    s = nums[i][j]
    while q:
        x, y, px, py = q.pop()
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < n and 0 <= b < m and nums[a][b] == s and (a, b) != (px, py):
                if vis[a][b] == 1:
                    return True
                q.append((a, b, x, y))
                vis[a][b] = 1
    return False


for i in range(n):
    for j in range(m):
        if vis[i][j] == 0:
            if bfs(i, j):
                print("Yes")
                exit()
print("No")




