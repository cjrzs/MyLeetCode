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
        p[x] = y
        size[y] += size[x]
        size[x] = 0


n, k = input_nums()
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = i
size = [1] * (n + 1)
for _ in range(n - 1):
    a, b, c = input_nums()
    if c == 0:
        merge(a, b)


res = pow(n, k, MOD)
for i in range(1, n + 1):
    if find(i) == i:
        res -= pow(size[i], k, MOD)
print(res % MOD)



