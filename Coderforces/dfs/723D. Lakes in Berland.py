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


def topsort(indu: List[int], g: List[List[int]]) -> List:
    """
    把图g按照拓扑序列进行排序。
    :param indu: 图的入度
    :param g: 使用 defaultdict 进行建图。
    :return:
    """
    res = []
    q = deque()
    for i in range(26):
        if indu[i] == 0:
            q.append(i)
    # print(q, g)
    # print(indu)
    while q:
        u = q.popleft()
        res.append(chr(u + 97))
        for x in g[u]:
            indu[x] -= 1
            if not indu[x]:
                q.append(x)
    return res


def is_bipartite_graph(g: List[List[int]], n: int) -> bool:
    """
    染色法判断一个图是不是二分图
    :param g: 图，使用 defaultdict 进行建图。
    :param n: 图中点的数量
    :return:
    """
    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        color[i] = 1
        q = deque()
        q.append(i)
        while q:
            u = q.popleft()
            for x in g[u]:
                if not color[x]:
                    color[x] = 3 - color[u]
                    q.append(x)
                else:
                    if color[x] == color[u]:
                        return False
    return True


def input_nums():
    return list(map(int, input().split(' ')))


n, m, k = input_nums()
nums = []
for _ in range(n):
    nums.append(list(input().strip()))

vis = [[0] * (m + 1) for _ in range(n + 1)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
def check(a, b):
    if a == 1 and nums[a - 1][b] == '.':
        return False
    if a == n - 2 and nums[n - 1][b] == '.':
        return False
    if b == 1 and nums[a][b - 1] == '.':
        return False
    if b == m - 2 and nums[a][m - 1] == '.':
        return False
    return True

@bootstrap
def dfs(x, y):
    vis[x][y] = 1
    lake.append((x, y))
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if not vis[a][b] and 0 <= a < n and 0 <= b < m and nums[a][b] == '.':
            # print(a, b, check(a, b))
            if check(a, b):
                yield dfs(a, b)
            else:
                global flag
                flag = False
                yield dfs(a, b)
    yield


lakes = []
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if not vis[i][j] and nums[i][j] == '.':
            flag = True
            lake = []
            dfs(i, j)
            if flag:
                lakes.append(lake)
lakes.sort(key=lambda x: len(x))
print(lakes, len(lakes), k)
cnt = len(lakes) - k
if k < len(lakes):
    # print(cnt)
    for items in lakes[: cnt]:
        for x, y in items:
            nums[x][y] = '*'

print(cnt)
for lake in nums:
    print(''.join(lake))



