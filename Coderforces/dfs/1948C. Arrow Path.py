import sys
from collections import defaultdict

sys.setrecursionlimit(8 ** 10)


def solve():
    for i in range(1, n, 2):
        if nums[0][i] == "<" and (nums[1][i - 1] == "<" or i + 1 < n and nums[1][i + 1] == '<'):
            print("NO")
            return
    print("YES")

    # q = [(0, 0)]
    # dp[0][0] = True
    # while q:
    #     x, y = q.pop()
    #     for a, b in g[(x, y)]:
    #         if not dp[a][b]:
    #             q.append((a, b))
    #             dp[a][b] = True
    # if dp[1][-1]:
    #     print("YES")
    # else:
    #     print("NO")


d = ([-1, 0], [0, 1], [1, 0], [0, -1])
T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[False] * n for _ in range(2)]
    nums = []
    nums.append(list(input()))
    nums.append(list(input()))
    # g = {}
    # for i in range(2):
    #     for j in range(n):
    #         g[(i, j)] = []
    #         if (i + j) & 1:
    #             if nums[i][j] == '>':
    #                 if j + 1 < n:
    #                     g[(i, j)].append((i, j + 1))
    #             if nums[i][j] == '<':
    #                 if j - 1 >= 0:
    #                     g[(i, j)].append((i, j - 1))
    #         else:
    #             for x in d:
    #                 a, b = i + x[0], j + x[1]
    #                 if 0 <= a < 2 and 0 <= b < n:
    #                     g[(i, j)].append((a, b))

    solve()


