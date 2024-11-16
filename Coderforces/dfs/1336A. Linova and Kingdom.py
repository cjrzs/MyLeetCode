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


# def main():
n, k = input_nums()
g = defaultdict(list)
size = [0] * (n + 1)
q = []
heapq.heapify([])
for _ in range(n - 1):
    a, b = input_nums()
    g[a].append(b)
    g[b].append(a)


@bootstrap
def dfs(u, pre, deep):
    for x in g[u]:
        if x != pre:
            yield dfs(x, u, deep + 1)
            size[u] += size[x]
    # print(u, deep, size[u], -(deep - 1 - size[u]))
    heapq.heappush(q, -(deep - 1 - size[u]))
    size[u] += 1
    yield

dfs(1, -1, 1)
# print(q, size)
res = 0
for i in range(k):
    res += -(heapq.heappop(q))
print(res)

