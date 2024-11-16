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


def topsort(indu: List[int], g: defaultdict) -> List:
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


def is_bipartite_graph(g: defaultdict, n: int) -> bool:
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


@bootstrap
def dfs(u, parent):
    s[u] = 1
    f[u] = 0
    total = 0
    # dp[u] = max(dp[l] + s[r] - 1, dp[r] + s[l] - 1)
    for x in g[u]:
        if x != parent:
            yield dfs(x, u)
            s[u] += s[x]
            total += f[x]
    for x in g[u]:
        if x != parent:
            # total 是总的 先减去当前节点，就剩另一个节点，然后加上当前节点的数量。
            f[u] = max(f[u], total - f[x] + s[x] - 1)
    yield

for _ in range(int(input())):
    n = int(input())
    g = [[] for _ in range(n + 1)]
    f = [0] * (n + 1)
    s = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = input_nums()
        g[a].append(b)
        g[b].append(a)
    dfs(1, -1)
    print(f[1])



