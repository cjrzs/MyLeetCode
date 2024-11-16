import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


k, n, m = input_nums()
nums = []
for i in range(k):
    t = []
    input()
    for _ in range(n):
        t.append(list(input()[:-1]))
    nums.append(t)
input()
x, y = input_nums()
# print(nums, x, y)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


def bfs():
    q = deque()
    q.append((x - 1, y - 1, 0))
    nums[0][x - 1][y - 1] = '#'
    res = 0
    while q:
        a, b, c = q.popleft()
        # print(a, b, c)
        res += 1
        for i in range(6):
            aa, bb, cc = a + dx[i], b + dy[i], c + dh[i]
            if 0 <= aa < n and 0 <= bb < m and 0 <= cc < k and nums[cc][aa][bb] == '.':
                nums[cc][aa][bb] = '#'
                q.append((aa, bb, cc))
    return res

print(bfs())







