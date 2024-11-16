import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def merge(u, x):
    a, b = find(u), find(x)
    if a != b:
        p[a] = b


n, m = input_nums()
p = [0] * (n + 1)
group = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = i
for _ in range(m):
    nums = input_nums()
    if nums[0] > 0:
        start = nums[1]
        for x in nums[2:]:
            merge(x, start)


for i in range(1, n + 1):
    group[find(i)] += 1
for i in range(1, n + 1):
    print(group[find(i)], end=" ")
print()
# print(res)



