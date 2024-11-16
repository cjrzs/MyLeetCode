import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def input_nums():
    return list(map(int, input().split(' ')))


nums = []
dx = [0, 0, 0, -1, 1, -1, -1, 1, 1]
dy = [0, -1, 1, 0, 0, 1, -1, -1, 1]
vis = [[0] * 8 for _ in range(8)]
statues = 0
for i in range(8):
    t = []
    for j, x in enumerate(list(input().strip())):
        if x == 'S':
            vis[i][j] = 1
            statues += 1
        t.append(x)
    nums.append(t)


def dfs(s, x, y):
    # print(s, x, y)
    if s >= 7:
        return True
    for i in range(9):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < 8 and 0 <= b < 8:
            if 0 <= a - s < 8 and not vis[a - s][b] and  0 <= a - s - 1 < 8 and not vis[a - s - 1][b]:
                if dfs(s + 1, a, b):
                    return True
    return False

if dfs(0, 7, 0):
    print("WIN")
else:
    print("LOSE")







