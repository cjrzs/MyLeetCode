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
        edges[y] += edges[x]
        edges[x] = 0


n, m, k = map(int, input().split(' '))
p = [0] * (n + 1)
edges = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = i
vis = list(map(int, input().split(' ')))
for _ in range(m):
    a, b = map(int, input().split(' '))
    merge(a, b)
for k, v in Counter(p):
    if k != 0:
        t = v * (v - 1) // 2 - edges[k]






