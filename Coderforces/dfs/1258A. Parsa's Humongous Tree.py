import heapq
import sys
import threading
from collections import defaultdict, Counter, deque
from itertools import permutations, chain, combinations
from types import GeneratorType

from typing import List, Set, Dict, Tuple

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def bootstrap(f, stack=[]):
    def wrapped_func(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrapped_func


def input_nums():
    return list(map(int, input().split(' ')))


@bootstrap
def dfs(u, pre):
    for x in g[u]:
        if x != pre:
            yield dfs(x, u)
            f[u][0] += max(f[x][0] + abs(nums[u][0] - nums[x][0]), f[x][1] + abs(nums[u][0] - nums[x][1]))
            f[u][1] += max(f[x][0] + abs(nums[u][1] - nums[x][0]), f[x][1] + abs(nums[u][1] - nums[x][1]))
    yield


for _ in range(int(input())):
    n = int(input())
    nums = [(-1, -1)]
    for _ in range(n):
        l, r = input_nums()
        nums.append((l, r))
    g = defaultdict(list)
    for _ in range(n - 1):
        a, b = input_nums()
        g[a].append(b)
        g[b].append(a)
    f = [[0] * 2 for _ in range(n + 1)]
    dfs(1, -1)
    print(max(f[1][0], f[1][1]))


