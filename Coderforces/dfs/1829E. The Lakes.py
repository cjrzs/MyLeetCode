from collections import deque


def func(nums, n, m):
    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

    def bfs(x, y):
        res = nums[x][y]
        nums[x][y] = 0
        q = [(x, y)]
        while q:
            x, y = q.pop()
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if 0 <= a < n and 0 <= b < m and nums[a][b] != 0:
                    res += nums[a][b]
                    nums[a][b] = 0
                    q.append((a, b))
        return res
    res = 0
    for i in range(n):
        for j in range(m):
            if nums[i][j] != 0:
                res = max(res, bfs(i, j))
    return res


T = int(input())

for _ in range(T):
    n, m = list(map(int, str(input()).split(' ')))
    nums = []
    for _ in range(n):
        nums.append(list(map(int, str(input()).split(' '))))
    print(func(nums, n, m))


