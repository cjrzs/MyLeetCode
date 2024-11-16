import heapq
import sys
import threading
from collections import defaultdict, Counter, deque
from itertools import permutations, chain, combinations


# sys.setrecursionlimit(8 ** 10)
from typing import List, Set, Dict, Tuple

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def input_nums():
    return list(map(int, input().split(' ')))


n, pos = input_nums()
nums = [-1] + input_nums()
vis = [False] * (n + 1)
program = []
p = list(range(n + 1))
size = [1] * (n + 1)


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def merge(a, b):
    x = find(a)
    y = find(b)
    if x != y:
        p[y] = x
        size[x] += size[y]
        size[y] = 0


def dfs(u):
    start = u
    while nums[u]:
        u = nums[u]
        vis[i] = True
        merge(start, u)


pre_val = 0
for i in range(1, n + 1):
    if i == pos:
        res = 1
        u = i
        while nums[u]:
            res += 1
            u = nums[u]
        pre_val = res
        break

for i in range(1, n + 1):
    if not vis[i]:
        vis[i] = True
        dfs(i)

# print(p, size)
t = find(pos)
for i in range(1, n + 1):
    if size[i] != 0 and i != t:
        program.append(size[i])
ans = set()
ans.add(pre_val)
all_perms = [combinations(program, r) for r in range(1, len(program) + 1)]
for params in all_perms:
    for x in set(params):
        ans.add(sum(x) + pre_val)


ans = list(ans)
ans.sort()
for x in ans:
    print(x)
# # def main():
#
#
# # sys.setrecursionlimit(10 ** 6)
# threading.stack_size(1 << 27)
# thread = threading.Thread(target=main)
# thread.start()
# thread.join()
