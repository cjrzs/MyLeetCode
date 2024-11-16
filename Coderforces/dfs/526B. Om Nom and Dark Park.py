import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


n = int(input())
nums = input_nums()
res = 0


def dfs(u, level):
    global res
    if level > n:
        return 0
    l, r = dfs(u * 2, level + 1), dfs(u * 2 + 1, level + 1)
    res += abs((l - r) + (nums[u * 2 - 2] - nums[u * 2 - 1]))
    return max(l + nums[u * 2 - 2], r + nums[u * 2 - 1])

dfs(1, 1)
print(res)

