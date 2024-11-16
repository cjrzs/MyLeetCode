import heapq
import sys
import threading
from collections import defaultdict, Counter, deque
from itertools import permutations, chain, combinations

from typing import List, Set, Dict, Tuple

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def input_nums():
    return list(map(int, input().split(' ')))


n, m, k = input_nums()
nums = []
q = deque()
for _ in range(n):
    nums.append(list(input().strip()))

vis = [[False] * m for _ in range(n)]
flag = True
t = 0
for i in range(n):
    for j in range(m):
        if nums[i][j] == '.':
            if flag:
                q.append((i, j))
                vis[i][j] = True
                flag = False
            else:
                t += 1
                nums[i][j] = 'X'
# print(q)
cnt = t - k
# print(cnt)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
while q:
    x, y = q.popleft()
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < n and 0 <= b < m and not vis[a][b] and nums[a][b] == 'X' and cnt:
            nums[a][b] = '.'
            cnt -= 1
            vis[a][b] = True
            q.append((a, b))

for i in range(n):
    print(''.join(nums[i]))



# def main():


# sys.setrecursionlimit(10 ** 6)
# threading.stack_size(1 << 27)
# thread = threading.Thread(target=main)
# thread.start()
# thread.join()
