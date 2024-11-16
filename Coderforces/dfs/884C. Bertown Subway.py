import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def input_nums():
    return list(map(int, input().split(' ')))


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def merge(a, b):
    x, y = find(a), find(b)
    if x != y:
        p[y] = x

n = int(input())
if n == 1:
    print(1)
    exit()
if n == 2:
    print(4)
    exit()
p = list(range(n + 1))
nums = [0] + list(map(int, input().split(" ")))
vis = [0] * (n + 1)


def dfs(u):
    res = 0
    while nums[u] != 0:
        res += 1
        nums[u], u = 0, nums[u]
    return res


cnt = sorted([dfs(u) for u in nums[1: ]], reverse=True)
res = 0
# print(cnt)
for x in cnt[2: ]:
    res += x * x
res += (cnt[0] + cnt[1]) ** 2
print(res)






