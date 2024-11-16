import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

# input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

n = int(input())
p = [0] * (n + 26)

for i in range(26 + n):
    p[i] = i

for i in range(n):
    s = list(input())
    m = len(s)
    for x in s:
        c = ord(x) - 97
        p[find(c)] = i + 26
    print(p)

res = 0
for i in range(26, n + 26):
    if p[i] == i:
        res += 1
print(res)










