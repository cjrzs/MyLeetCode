import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


n = int(input())
nums = input_nums()


t = {i + 1: x for i, x in enumerate(nums)}
nums.sort()
d = {x: i + 1 for i, x in enumerate(nums)}
res = []
vis = [0] * (n + 1)
for i, x in enumerate(nums):
    j = i + 1
    tmp = []
    while not vis[j]:
        # print(j)
        vis[j] = 1
        tmp.append(j)
        j = d[t[j]]
    # print('---')
    if tmp:
        res.append(tmp)
print(len(res))
for item in res:
    print(len(item), *item)





