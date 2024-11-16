import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def input_nums():
    return list(map(int, input().split(' ')))


n = int(input())
nums = []

s, t, i = {}, list(), 1
for _ in range(n):
    c, a, b = map(int, input().split())
    if c > 1:
        if b in s[a]:
            print('YES')
        else:
            print('NO')
    else:
        s[i] = {i}
        for j, (x,y) in enumerate(t, 1):
            if (x < a and a < y) or (x < b and b < y):
                s[i].update(s[j])
        r = set(j for j, (x, y) in enumerate(t, 1) if a < x < b or a < y < b)
        for j in range(1, len(t) + 1):
            if r & s[j]: s[j].update(s[i])
        t.append((a, b))
        i += 1
