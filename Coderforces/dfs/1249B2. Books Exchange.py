import sys
from collections import defaultdict

sys.setrecursionlimit(8 ** 10)


# 主要是能想出来， 当找到一个环之后， 整个环上的所有元素的答案都是这个环的元素数量。
def solve(nums):
    # dist = {}
    #
    # def dfs(u, cnt):
    #     # print("u, cnt: ", u, cnt)
    #     if (u, cnt) in dist:
    #         return dist[(u, cnt)]
    #     if u in vis:




    #         return cnt
    #     vis.add(u)
    #     dist[(u, cnt)] = dfs(nums[u], cnt + 1)
    #     return dist[(u, cnt)]
    # for i, x in enumerate(nums[1: ]):
    #     if i + 1 == x:
    #         print(1, end=" ")
    #     else:
    #         vis = set()
    #         print(dfs(x, 0), end=" ")
    a = [-1] * n
    for i in range(n):
        if a[i] == -1:
            vis = set()
            t = i
            while t not in vis:
                # print(t)
                vis.add(t)
                t = nums[t] - 1
            # print("vis", vis)
            for x in vis:
                a[x] = len(vis)
    print(*a, end=" ")

T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split(' ')))
    solve(nums)
    print(' ')
